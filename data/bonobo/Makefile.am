## Process this file with automake to produce Makefile.in
#
# data/bonobo/Makefile.am
#
# $Id: Makefile.am 535 2006-06-11 18:17:22Z erikg $
#

serverdir		= $(libdir)/bonobo/servers
server_DATA		= GNOME_RevelationApplet.server
CLEANFILES		= GNOME_RevelationApplet.server
EXTRA_DIST		= GNOME_RevelationApplet.server.in

GNOME_RevelationApplet.server: GNOME_RevelationApplet.server.in
	sed \
		-e "s|\@libexecdir\@|$(libexecdir)|" \
		GNOME_RevelationApplet.server.in >GNOME_RevelationApplet.server

