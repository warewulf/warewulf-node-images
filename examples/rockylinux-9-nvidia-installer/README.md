# Rocky Linux with the Nvidia driver (.run installer)

This container definition demonstrates building a Rocky Linux based container
incorporating the Nvidia driver from the `.run` installer.

The container may be built with Podman.

```shell

podman build --volume <local .run installer>:/mnt/NVIDIA-Linux.run . --tag rockylinux-9-nvidia-installer
```

This can then be imported directly into Warewulf.

```
wwctl container import $(podman image mount rockylinux-9-nvidia-installer) rockylinux-9-nvidia-installer
podman image unmount rockylinux-9-nvidia-installer
```

The host that builds the container does _not_ need to have a GPU installed.
