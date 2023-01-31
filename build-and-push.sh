#!/bin/bash


REPOSITORY="${REPOSITORY:-docker.io/warewulf}"
IMAGE_PREFIX="${IMAGE_PREFIX}"


function main
{
	podman build --tag "${REPOSITORY}/${IMAGE_PREFIX}centos:7" centos-7
	podman push "${REPOSITORY}/${IMAGE_PREFIX}centos:7"
	podman build --tag "${REPOSITORY}/${IMAGE_PREFIX}rockylinux:8" rockylinux-8
	podman push "${REPOSITORY}/${IMAGE_PREFIX}rockylinux:8"
	podman push "${REPOSITORY}/${IMAGE_PREFIX}rockylinux:8" "${REPOSITORY}/${IMAGE_PREFIX}rockylinux:latest"
}


main "$@"
