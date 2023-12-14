# Rocky Linux with the Mellanox OFED

This container definition demonstrates building a Rocky Linux based container
incorporating the Mellanox OFED for InfiniBand support.

This definition requires that the [Mellanox OFED .tgz][1] for the desired
version be placed in the `rockylinux-9-mofed` directory.

[1]: https://network.nvidia.com/products/infiniband-drivers/linux/mlnx_ofed/

With that in place, the container may be built with Podman.

```shell

podman build . --volume $PWD:/mnt:ro --file Containerfile
```
