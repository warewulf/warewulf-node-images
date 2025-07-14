#!/bin/sh

echo "
The AlmaLinux community provides updates for the latest point release of
AlmaLinux 8. If you need to remain on a specific point release (e.g.,
AlmaLinux 8.8) you may want to engage with a commercial support provider for
long-term support.

https://almalinux.org/support
"

export LANG=C LC_CTYPE=C

set -x
dnf clean all
rm -f /etc/machine-id /var/lib/dbus/machine-id
