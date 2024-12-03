# Rocky Linux with the Mellanox OFED

This container definition demonstrates building a Rocky Linux based container
incorporating the Mellanox OFED for InfiniBand support.

This definition requires that the [Mellanox OFED .tgz][1] for the desired
version be placed in the `rockylinux-8-mofed` directory.

[1]: https://network.nvidia.com/products/infiniband-drivers/linux/mlnx_ofed/

With that in place, the container may be built with Podman.

For Rocky Linux 8.10 (aarch64):

```shell

podman build . --volume $PWD:/mnt:ro --build-arg MOFED_TGZ=MLNX_OFED_LINUX-24.10-0.7.0.0-rhel8.10-aarch64.tgz --file Containerfile-8
```

For Rocky Linux 9.4 (aarch64):

```shell
podman build . --volume $PWD:/mnt:ro --build-arg MOFED_TGZ=MLNX_OFED_LINUX-24.10-0.7.0.0-rhel9.4-aarch64.tgz --file Containerfile-9
```
