#!/bin/bash
export LANG=C LC_CTYPE=C
set -x
zypper clean -a
rm -f /etc/machine-id /var/lib/dbus/machine-id
