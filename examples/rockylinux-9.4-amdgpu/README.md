# Rocky Linux with the AMD GPU driver

https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/amdgpu-install.html

This container definition demonstrates building a Rocky Linux based container
incorporating the AMDGPU driver for AMD GPU support.

The container may be built with Podman.

```shell

podman build .
```

The host that builds the container does _not_ need to have a GPU installed.
