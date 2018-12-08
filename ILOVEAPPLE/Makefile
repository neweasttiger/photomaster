
autoputo : autoputo.c libsort.a 
	gcc -o autoputo autoputo.c -L. -lsort

libsort.a : filesort.o 
	ar rv libsort.a filesort.o

filesort.o : filesort.c filesort.h
	gcc -c filesort.c filesort.h

