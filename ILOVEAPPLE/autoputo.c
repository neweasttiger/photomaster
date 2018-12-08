#include <stdio.h>
#include <stdlib.h>
#include "filesort.h"

int main(){
	int n;
	printf("1. auto sort 2. auto uproading SNS\n");
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
		default :
			printf("Input error\n");
			break;

	}
	return 0;
}
