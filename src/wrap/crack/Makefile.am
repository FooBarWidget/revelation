## Process this file with automake to produce Makefile.in
#
# src/wrap/crack/Makefile.am
#
# $Id: Makefile.am 535 2006-06-11 18:17:22Z erikg $
#

module_PROGRAMS	= crack.so
moduledir	= $(pyexecdir)/revelation
CLEANFILES	= crack.c
EXTRA_DIST	= crack.c.in

crack.c: crack.c.in
	sed \
		-e "s|\@CRACK_DICTPATH\@|@CRACK_DICTPATH@|" \
		crack.c.in >crack.c

crack.o: crack.c
	$(CC) -pthread -fno-strict-aliasing -fPIC -I${PYTHON_INCLUDE} -c crack.c -o crack.o

crack.so: crack.o
	$(CC) -Wl --export-dynamic -pthread -shared crack.o -lcrack -o crack.so

