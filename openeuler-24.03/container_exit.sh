#!/bin/sh
set -x
LANG=C
LC_CTYPE=C
export LANG LC_CTYPE
dnf clean all
rm -f /etc/machine-id /var/lib/dbus/machine-id
