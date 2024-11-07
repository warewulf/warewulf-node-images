# Red Hat Enterprise Linux 9

Warewulf can be used to boot a RHEL node,
but building such an image typically requires access to a Red Hat subscription.
This subscription can be accessed from the host environment
by mounting subscription files.


```
podman build \
    --volume=/etc/pki/entitlement:/run/secrets/entitlement:ro \
    --volume=/etc/rhsm:/run/secrets/rhsm:ro \
    --volume=/etc/yum.repos.d/redhat.repo:/run/secrets/redhat.repo:ro \
    . --tag rhel:9
```

For more information,
see https://access.redhat.com/solutions/5870841.
