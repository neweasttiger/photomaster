#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <dirent.h>
#include <string.h>

int pictur(const struct dirent *info){
	char *ext;
	ext = strrchr(info->d_name, '.');
	if(ext ==NULL){
		return 0;
	}
	if(strcmp(ext, ".jpg") == 0){
		return 1;
	}
	if(strcmp(ext, ".jpeg") == 0){
		return 1;
	}else 
		return 0;
}
void facedetect(){
  struct dirent **namelist;
  int count;
  int idx;
  char file_path[1024];
  const char *path =".";
  count  = scandir(path, &namelist, pictur,alphasort);
  for (idx =0 ; idx< count; idx++){
	char p[100] = "python ILOVEAPPLE/faces.py ";
	strcat(p, namelist[idx]->d_name);
  	system(p);
  }
  exit(0);
  
}
void upload()
{	char n[20];
	char ss[500];
	printf("what do you want to upload? (Input dir name)\n");
	scanf("%s",n);
	
	printf("Input comments to upload\n");
	scanf("%[^\n]s",ss);
	DIR *dir_info;
	struct dirent *dir_entry;
	dir_info = opendir(".");
	FILE *f = fopen("path.txt","wt");
	if(NULL!= dir_info)
	{
		while( dir_entry = readdir(dir_info))
		{
			if(strcmp(dir_entry->d_name, n) ==0)
			{	char path[20] ="./";
				strcat(path,dir_entry->d_name);
				strcat(path,"\n");
				fwrite(path,strlen(path),1,f);
				fwrite(ss,strlen(ss),1,f);
				return ;
			}
		}
	}
	printf("No exit your choice\n");
}
