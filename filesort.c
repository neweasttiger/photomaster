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
	char p[100] = "python faces.py ";
	strcat(p, namelist[idx]->d_name);
  	system(p);
  }
  exit(0);
  
}
void upload()
{	int n;
	printf("how many people do you want to upload?\n");
	scanf("%d",&n);
	DIR *dir_info;
	struct dirent *dir_entry;
	dir_info = opendir(".");
	if(NULL!= dir_info)
	{
		while( dir_entry = readdir(dir_info))
		{
			if(strcmp(dir_entry->d_name, n) ==0)
			{
				// here upload code 
				// enter dir (cd n )
				// find image(.jpg , .jpg)
				// upload (python facebook~~ image)		
			}
		}
	}
	printf"No exit your choice\n");
}
int main(){
	int n;
	printf("1. auto sort 2. auto uproading SNS\n");
	scanf("%d",&n);
	switch(n)
	{
		case 1:
			facedetect();
			break;
		case 2:
			upload();
			break;
		default :
			printf("Input error\n");
			break;

	}
	return 0;
}
