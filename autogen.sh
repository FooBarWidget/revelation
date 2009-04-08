#!/bin/sh
srcdir=`dirname "$0"`
[ -z "$srcdir" ] && srcdir=.

PKG_NAME=revelation
REQUIRED_AUTOMAKE_VERSION=1.7

if [ ! -f "$srcdir/src/revelation.in" ]; then
 echo "$srcdir doesn't look like source directory for $PKG_NAME" >&2
 exit 1
fi

. gnome-autogen.sh
