# Rocky Linux 10

A Warewulf container definition based on Rocky Linux 10.

```
wwctl container import docker://ghcr.io/warewulf/warewulf-rockylinux:10 rockylinux-10
```

Also available are definitions for individual point releases (e.g., Rocky Linux
10.0). To generate these Containerfiles, run `make`.

The Rocky Linux community provides updates for the current point release of
Rocky Linux 10. If you need to remain on a specific point release you may want
to engage with a commercial support provider for long-term support.

**Note:** These container images are configured to minimize size. If you desire for
man-pages and other documentation to be available to users, e.g. on login-nodes, 
the `/etc/yum.conf` and `/etc/dnf/dnf.conf` flag `tsflags=nodocs` needs 
to be removed before installing additional packages. 

https://rockylinux.org/support
