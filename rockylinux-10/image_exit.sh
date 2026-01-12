#!/bin/sh

echo "
The Rocky Linux community provides updates for the latest point release of
Rocky Linux 10. If you need to remain on a specific point release (e.g., Rocky
Linux 10.0) you may want to engage with a commercial support provider for
long-term support.

https://rockylinux.org/support
"

export LANG=C LC_CTYPE=C

set -x
dnf clean all
rm -f /var/lib/dbus/machine-id
truncate -s0 /etc/machine-id
