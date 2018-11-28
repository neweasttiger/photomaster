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
	char *p = "python faces.py ";
	strcat(p, namelist[idx]->d_name);
  	system(p);

  }
  
}


int main(){
	pid_t pid = fork();
	int cvalue;
	switch(pid){
	 case 0:
		facedetect();
	 default :
		wait(NULL);
	}
	
return 0;
}
