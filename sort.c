#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <dirent.h>
void remove_image (char *image)
{	char path[50];
	strcat(path, "./");
	strcat(path,image);
	if(remove(path) !=0)
		printf("remove error \n");
}
	
int main (int argc, char *argv[]){
	char mk[30] = "mkdir ";
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
						
				if(system(cp)!=0){
					printf("cp error\n");
				}

				remove_image(argv[2]);
				return 0;
			}
		}
	}
	
	strcat(mk,argv[1]);
	system(mk);
	
	strcat(cp,argv[2]);
	strcat(cp," ");
	strcat(cp,"./");
	strcat(cp,argv[1]);
	strcat(cp,"/");
	strcat(cp,argv[2]);
						
	if(system(cp)!=0){
		printf("cp error\n");
	}

	remove_image(argv[2]);
	closedir(dir_info);

	return 0;
}

