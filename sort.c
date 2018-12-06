#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <dirent.h>

int main (int argc, char *argv[]){
	char mk[40] = "mkdir ";
	char cp[30] = "cp ";
	DIR *dir_info;
	struct dirent *dir_entry;
	
	dir_info =opendir(".");

	if( NULL!= dir_info)
	{
		while( dir_entry = readdir(dir_info))
		{	
			if(strcmp(dir_entry->d_name,argv[1]) ==0)
			{
				strcat(cp,argv[2]);
				strcat(cp," ");
				strcat(cp,"./");
				strcat(cp,argv[1]);
				strcat(cp,"/");
				strcat(cp,argv[2]);
				
				
				system(cp);
				return 0;
			}
		}

	}
	strcat(mk,argv[1]);
	int s = system(mk);
	while(s!=0){}
	strcat(cp,argv[2]);
	strcat(cp," ");
	strcat(cp,"./");
	strcat(cp,argv[1]);
	strcat(cp,"/");
	strcat(cp,argv[2]);

	system(cp);
	
	closedir(dir_info);
	return 0;
}

