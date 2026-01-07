#!/usr/bin/env python3

import argparse
import logging
import os
import re
import subprocess
import sys
#from lib.libimage import *

registry_url = 'registry.access.redhat.com'
ubi8 = 'ubi8/ubi@sha256:7d7ca86d832d1dc7aba4583414475c15686291b1c2cf75fe63ca03526c3b89ae'
ubi8_mini = 'ubi8/ubi-minimal@sha256:a670c5b613280e17a666c858c9263a50aafe1a023a8d5730c7a83cb53771487b'
default_ubi_version = ubi8_mini

default_os_version='8'

comment_re = re.compile(r'^([^#]*)#.*$')

def get_logger(name):

    logger = logging.getLogger(name)
    logger.setLevel('DEBUG')

    stderr_handler = logging.StreamHandler()
    stderr_handler.setLevel('INFO')

    stderr_formatter = logging.Formatter('{asctime}:{levelname}:{name}[{process}]: {message}', style='{', datefmt='%Y-%m-%d %H:%M')
    stderr_handler.setFormatter(stderr_formatter)

    logger.addHandler(stderr_handler)

    return logger

def parse_args():

    parser = argparse.ArgumentParser(description=f'{os.path.basename(sys.argv[0])}: generate a Warewulf importable podman image archive from an UBI container')

    parser.add_argument('-v', dest='ubi_version', default=default_ubi_version, metavar='ubi-version', help=f'default: {default_ubi_version}')
    parser.add_argument('-y', dest='yes_to_all', action='store_true', help='yes to all')
    parser.add_argument('-o', dest='os_version', default=default_os_version, metavar='os-version', help='os version as known by RH Satellite (default: 8)')
    parser.add_argument('-p', dest='pkglist_path', metavar='pkglist-path', help='pkglist file path')
    parser.add_argument('-i', dest='import_chroot', action='store_true', help='import image into Warewulf')
    parser.add_argument('--name', dest='chroot_name', metavar='chroot-name', help='chroot name (default: basename(archive-path)')
    parser.add_argument('--force', dest='force_import', action='store_true', help='force import')
    parser.add_argument('-r', dest='remove_archive', action='store_true', help='remove archive after import')
    parser.add_argument('archive_path', metavar='archive-path', help='archive path')

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(0)

    return parser.parse_args()

'''
Reads a file consisting of one package name / line (comments allowed)
and returns a space separated str of packages
'''

def read_pkglist(path):

    with open(path, 'r') as f:
        # lines stripped from comments and '\n'
        pkglist = [ re.sub(comment_re, r'\1', p.rstrip('\n')) for p in f.readlines() ]

    # only non empty lines
    return [ p for p in pkglist if p ]

def main():

    args = parse_args()

    # where to get the base image
    ubi_url = os.path.join(registry_url, args.ubi_version)

    # where to commit container
    img_ns = 'localhost/archive' 
    archive_name = os.path.basename(args.archive_path)
    img_fidn = os.path.join(img_ns, archive_name + ':latest')

    # where to save image
    img_archive_path = args.archive_path

    # in UBI redhat.repo pulled by subscription-manager plugin has BaseOS and AppStream disabled
    config_manager_args = f"--set-enabled '*'" 

    pkglist = read_pkglist(args.pkglist_path)

    cntr = subprocess.run(f'buildah from {ubi_url}', shell=True, capture_output=True, text=True).stdout
    if cntr:
        cntr = cntr.rstrip('\n')

    cntr_rootfs = subprocess.run(f'buildah mount {cntr}', shell=True, capture_output=True, text=True).stdout
    if cntr_rootfs:
        cntr_rootfs = cntr_rootfs.rstrip('\n')

    # ubi-minimal only has microdnf
    has_dnf = os.path.isfile(f'os.path.join({cntr}, usr/bin/dnf)')
    if has_dnf:
        cmds = []
    else:
        logger.info('Will try to use microdnf to install dnf')
        cmds = [ f'buildah run {cntr} /bin/bash -c "microdnf install dnf"', ] 

    subprocess.run(f'buildah umount {cntr}'.split())

    cmds += [

       # ubi.repo would duplicate baseos and appstream and force to choose
       # which one we want with --enablerepo/--disablerepo
       f'buildah run {cntr} /bin/bash -c "rm /etc/yum.repos.d/ubi.repo"',

       f'buildah run {cntr} /bin/bash -c "mkdir -p /etc/dnf/vars/releasever"',

       # redhat.repo pulled by ubi subsription-manager plugin uses $releasever which may differ from what the host uses (ex: 8 vs 8.8), so set releasever to match Satellite urls
       f'buildah run {cntr} /bin/bash -c "echo {args.os_version} > /etc/dnf/vars/releasever"',

       f'buildah run {cntr} /bin/bash -c "dnf clean all"',
        
       f'buildah run {cntr} /bin/bash -c "dnf config-manager {config_manager_args}"',
        
       f'buildah run {cntr} /bin/bash -c "dnf upgrade -y"',
        
       f'buildah run {cntr} /bin/bash -c "dnf install -y --allowerasing {' '.join(pkglist)}"',

        f'buildah commit {cntr} {os.path.join(img_ns, archive_name)}',

        f'buildah rm {cntr}',

        f'podman image save {img_fidn} > {img_archive_path}',
    
        f'podman image rm {img_fidn}',
    ]

    for cmd in cmds:
        logger.info(f'Running {cmd}')
        subprocess.run(cmd, shell=True)
    
    chroot_name = args.chroot_name if args.chroot_name else os.path.basename(img_archive_path)
    import_options = '--force' if args.force_import else ''

    if args.import_chroot:
        print(f'running wwctl image import {import_options} {img_archive_path} {chroot_name}')
        subprocess.run(f'wwctl image import {import_options} {img_archive_path} {chroot_name}', shell=True)

        print(f'removing {img_archive_path}')
        os.remove(img_archive_path)

logger = get_logger(f'{os.path.basename(sys.argv[0])}')

if __name__ == '__main__':

    main()
