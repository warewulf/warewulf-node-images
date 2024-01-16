# Warewulf node images

Example node container images for use with Warewulf v4.

https://warewulf.org

## Built examples

These containers are published on the [GitHub container registry][1].

[1]: https://github.com/orgs/warewulf/packages?repo_name=warewulf-node-images

* [Rocky Linux 8](rockylinux-8)
* [Rocky Linux 9](rockylinux-9)
* [openSUSE Leap](leap)

## Additional examples

Additional container definitions that are not actively built and published, but
may still be useful.

* [Rocky Linux 9 with SELinux](examples/rockylinux-9-selinux)
* [Rocky Linux 9 with Mellanox OFED](examples/rockylinux-9-mofed)

You can build any of these (or the other container definitions) locally for
import into Warewulf v4.

```shell

podman build examples/rockylinux-9-selinux \
  --file examples/rockylinux-9-selinux/Containerfile \
  --tag warewulf-rockylinux-selinux:9
podman save warewulf-rockylinux-selinux:9 --output warewulf-rockylinux-selinux-9.tar
wwctl container import warewulf-rockylinux-selinux-9.tar rockylinux-selinux-9
```
