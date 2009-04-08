## Process this file with automake to produce Makefile.in
#
# data/cracklib/Makefile.am
#
# $Id: Makefile.am 535 2006-06-11 18:17:22Z erikg $
#

dictdir		= $(datadir)/revelation
dict_DATA	= pwdict.hwm pwdict.pwd pwdict.pwi
CLEANFILES	= pwdict.hwm pwdict.pwd pwdict.pwi
EXTRA_DIST	= pwdict


pwdict.hwm pwdict.pwd pwdict.pwi: pwdict
	$(CRACK_FORMAT) pwdict | $(CRACK_PACKER) pwdict

