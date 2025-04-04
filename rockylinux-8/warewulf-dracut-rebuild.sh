#!/bin/sh

if rpm -q warewulf-dracut --quiet
then
	dracut --force --no-hostonly --add wwinit --regenerate-all
else
	echo 1>&2 "warewulf-dracut not found"
	exit -1
fi
