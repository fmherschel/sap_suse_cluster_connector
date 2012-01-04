#
# build shared library
#

all:	libsapha.so.1.1.0

libsapha.so.1.1.0: sapha.o
	gcc -shared -Wextra,-Wall,-pedantic,-soname,libsapha.so.1 -o libsapha.so.1.1.0  sapha.o
	ln -s -f libsapha.so.1.1.0 libsapha.so.1
	ln -s -f libsapha.so.1.1.0 libsapha.so

sapha.o: sapha.c
	gcc -Wextra -Wall -c -fPIC sapha.c -o sapha.o
#
# build test binary and run basic tests
#
test: all
	bash -c "LD_LIBRARY_PATH=. ./fhsaphatest"


distclean: 
	rm libsapha.so libsapha.so.1 libsapha.so.1.1.0 sapha.o fhsaphatest
