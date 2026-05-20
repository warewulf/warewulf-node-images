# RHEL image and RH subscriptions

Using host RHEL subscription for a non RHEL image is possible but may or may not be supported by RHEL
This example describes a way to go the full RHEL route.

In order to create a full RHEL image, access to usual RedHat repos must be achieved, which basically means to be `registered` to either RHEL CDN or a RHEL Satellite server

Here's a proof of concept of what's could be done for this matter (in the context of a RHEL Satellite server providing RHEL repos) - the CDN case should be similar

At first, a method could consist in creating the chroot from repos present in ISO releases:

.. code-block:: bash

    dnf install -y --disablerepo=\* --repofrompath=BaseOS,"$ISO_DIR/$DVD_DIR/BaseOS" --repofrompath=AppStream,"$ISO_DIR/$DVD_DIR/AppStream" --nogpgcheck --installroot "$CHROOT_DIR" basesystem bash chkconfig coreutils e2fsprogs ethtool filesystem findutils gawk grep initscripts iproute iputils net-tools nfs-utils pam psmisc rsync sed setup shadow-utils rsyslog tzdata util-linux words zlib tar less gzip which util-linux openssh-clients openssh-server dhclient pciutils vim-minimal shadow-utils strace cronie crontabs cpio wget redhat-release ipmitool yum  NetworkManager subscription-manager bind-utils kernel python3.12 dracut-network

However `dnf --installroot` is not the same as `chroot dnf install` which could lead for packages adding a user setting related files ownership to `uid:gid` of the host user instead of the chroot

On the OCI side, RHEL provides RHEL Universal Base Image (UBI) images engines like `Podman` and `Buildha` to use them.
An imported `ubi` image makes a valid Warewulf chroot but only comes with the `ubi.repo` repo file pointing conceptually basically to a subset of RHEL repos. Those full fledge repos would not be accessible from a `wwctl image shell` because the chroot would not be **registered**

When ran via above engines on a host running the same OS version, `ubi` containers automatically benefit through clever bind mounts from the host subscription, so another strategy could consist in using this feature to install all wanted packages **before** the import into Warewulf

This requires the following steps:

Caveats:

* `ubi-minimal` does not include (as ubi does) `dnf` but `microdnf`, so if using this container, `dnf must first be installed`

* `redhat.repo` does not initially exist inside the container but is pulled by `subscription-manager` `dnf` plugin (running in so called `container-mode`), usually `BaseOS` and `AppStream` being disabled (they're enabled in the `ubi.repo` file), so they'll have to be reenabled and `ubi.repo` will have to be deleted

* `$releasever` inside `ubi` might be different that the releasever used in the `baseurl` of `redhat.repo` (ex: `8.8` vs `8`), so this is safer to explicitly set it

Steps:

(edited from an actual Python script running those commands, assuming `pkglist` is a list of (initial) packages we want to provision the future image with)

```
# buildah from {ubi_url}
# buildah run {cntr} /bin/bash -c "microdnf install dnf" # [if ubi-minimal only]
# buildah run {cntr} /bin/bash -c "rm /etc/yum.repos.d/ubi.repo"
# buildah run {cntr} /bin/bash -c "mkdir -p /etc/dnf/vars/releasever"
# buildah run {cntr} /bin/bash -c "echo {os_version} > /etc/dnf/vars/releasever"
# buildah run {cntr} /bin/bash -c "dnf clean all"
# buildah run {cntr} /bin/bash -c "dnf config-manager --set-enabled '*'"
# buildah run {cntr} /bin/bash -c "dnf upgrade -y"
# buildah run {cntr} /bin/bash -c "dnf install -y --allowerasing {pkglist}"
# buildah commit {cntr} {archive_name}'
# buildah rm {cntr}
# podman image save {img_fidn} > {img_archive_path}
# podman image rm {img_fidn}
# wwctl image import {img_archive_path} {chroot_name}
```

Note: if repos are "snapshot" (version frozen - the "version" concept of RedHat Satellite), care must be taken to use an ubi image hash making ubi repos version **older or as current** as Redhat ones (otherwise packages would be downgraded)

