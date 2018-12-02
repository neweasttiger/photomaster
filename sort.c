#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <dirent.h>

int main (int argc, char *argv[]){
	char mk[40] = "mkdir ";
	char cp[30] = "cp ";
	struct dirent dir;

	strcat(mk,argv[1]);
	
	system(mk);
	
	strcat(cp,argv[2]);
	strcat(cp," ");
	strcat(cp,"./");
	strcat(cp,argv[1]);
	strcat(cp,"/");
	strcat(cp,argv[2]);

	system(cp);
	return 0;
}

