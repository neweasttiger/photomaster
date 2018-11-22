#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>


void facedetect(){
    
  system("python faces.py face_example.jpg ");
 
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
