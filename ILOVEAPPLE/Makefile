
include = ./include/
libs = ./lib/

all : sort autoputo

sort : $(include)sort.c
	gcc -o sort $(include)sort.c

autoputo : $(include)autoputo.c $(lib)libsort.a 
	gcc -o ../autoputo $(include)autoputo.c -L./lib -lsort

libsort.a : $(include)filesort.o 
	ar rv $(libs)libsort.a $(include)filesort.o

filesort.o : $(include)filesort.c $(include)filesort.h
	gcc -c $(include)filesort.c $(include)filesort.h

