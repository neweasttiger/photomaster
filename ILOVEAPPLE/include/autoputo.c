#include <stdio.h>
#include <stdlib.h>
#include "filesort.h"

int main(){
	int n;
	while(1){

	printf("1. Auto sort 2. Auto uproad 3. exit\n");
	scanf("%d",&n);
	fflush(stdin);
	switch(n)
	{
		case 1:
			facedetect();
			break;
		case 2:
			upload();
			break;
		case 3:
			printf("Good Bye :)\n");
			return 0;
		default :
			printf("Input error\n");
			break;

	}
	}
	return 0;
}
