#!/bin/sh
srcdir=`basename $0`
[ -z "$srcdir" ] && srcdir=.

PKG_NAME=mypackage
REQUIRED_AUTOMAKE_VERSION=1.7

if [ ! -f "$srcdir/somefile-that-is-only-in-mypackage" ]; then
 echo "$srcdir doesn't look like source directory for $PKG_NAME" >&2
 exit 1
fi

. gnome-autogen.sh
