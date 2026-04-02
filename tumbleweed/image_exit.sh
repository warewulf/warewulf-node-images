#!/bin/bash
export LANG=C LC_CTYPE=C
set -x
zypper clean -a
rm -f /var/lib/dbus/machine-id
truncate -s0 /etc/machine-id
