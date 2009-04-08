## Process this file with automake to produce Makefile.in
#
# data/mime/Makefile.am
#
# $Id: Makefile.am 607 2007-01-11 01:22:35Z erikg $
#

desktopdir		= $(datadir)/applications
nodist_desktop_DATA	= revelation.desktop

mimedir			= $(datadir)/mime/packages
dist_mime_DATA		= revelation.xml

CLEANFILES		= revelation.desktop
EXTRA_DIST		= revelation.desktop.in


revelation.desktop: revelation.desktop.in
	sed \
		-e "s|\@VERSION\@|$(VERSION)|" \
		revelation.desktop.in > revelation.desktop


install-data-hook:
if HAVE_FDO_MIME
	$(UPDATE_MIME_DATABASE) "$(datadir)/mime"
endif

if HAVE_FDO_DESKTOP
	$(UPDATE_DESKTOP_DATABASE)
endif

