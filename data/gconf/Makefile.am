## Process this file with automake to produce Makefile.in
#
# data/gconf/Makefile.am
#
# $Id: Makefile.am 538 2006-06-12 19:05:11Z erikg $
#

schemadir		= @GCONF_SCHEMA_FILE_DIR@
dist_schema_DATA	= revelation.schemas revelation-applet.schemas


install-data-hook:
if GCONF_SCHEMAS_INSTALL
	GCONF_CONFIG_SOURCE=$(GCONF_SCHEMA_CONFIG_SOURCE) \
	$(GCONFTOOL) --makefile-install-rule $(dist_schema_DATA)
endif

