#!/bin/sh
set -x
LANG=C
LC_CTYPE=C
export LANG LC_CTYPE
zypper clean --all
