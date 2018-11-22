#include <stdio.h>

int main()
{
 int number;

 printf("자동 업로드 시스템 번호를 선택하세요\n");
 printf("1.풍경 사진 업로드\n2.얼굴이 나온 사진 업로드\n3.종료");
 scanf("%d", &number);


 while(1)
 {
  //분류된 사진에 풍경 업로드
  if(number ==3)
  {
    printf("종료\n");
    break;
  }
  else if(number == 1)
  {
   printf("인스타그램에 풍경사진 업로드\n");
   //sns에 업로드
  }
  else if(number == 2)
  {
   printf("인스타그램에 얼굴사진 업로드\n");
   //얼굴 사진 업로드
  }
 }

 return 0;
}
