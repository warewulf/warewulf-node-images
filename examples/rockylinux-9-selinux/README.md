# Rocky Linux 9 with SELinux

Warewulf can be used to boot an selinux-equipped node. This example installs
required packages and configures SELinux policy for the `wwclient` binary
(which communicates with the Warewulf server and receives runtime overlays).

```
podman build . --tag rockylinux-selinux:9
```

Booting a node image with selinux enabled requires (at least up to Warewulf
v4.4.1) setting `--root=tmpfs` on the relevant node and setting
`rootfstype=ramfs` as a kernel argument. For more information on these
settings, look at [wwinit/init][1].

[1]: https://github.com/hpcng/warewulf/blob/main/overlays/wwinit/init
