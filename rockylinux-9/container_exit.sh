#!/bin/sh

echo "
The Rocky Linux community provides updates for the latest point release of
Rocky Linux 9. If you need to remain on a specific point release (e.g., Rocky
Linux 9.2) you may want to engage with a commercial support provider for
long-term support.

https://rockylinux.org/support
"

export LANG=C LC_CTYPE=C

set -x
dnf clean all
