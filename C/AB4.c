#include <stdio.h>

int
main (){
  //Mod3511();
  //IsLeapYear();
  //RightTriangle();
  //Power2Divide2();
  return 0;
}

int Power2Divide2 (){
  int InputNum;
  int InputNumD2;
  int InputNumP2;
  
  printf ("Aada ra vared konid:");
  printf ("\n");
  scanf ("%d", &InputNum);
  
  if (InputNum % 2 == 0)
    {
      printf ("Even");
      printf ("\n");
      
      InputNumD2 = InputNum / 2;
      
      printf ("%d", InputNumD2);
      printf ("\n");
    }
  else
    {
      printf ("odd");
      printf ("\n");
      
      InputNumP2 = InputNum * InputNum;
      
      printf ("%d", InputNumP2);
      printf ("\n");
    }
}

int RightTriangle(){
    
  int Edge1, Edge2, Edge3;
  int E1P2, E2P2, E3P2;
  int Area, Perimeter;
  
  printf ("Enter Edge1:\n");
  scanf ("%d", &Edge1);
  
  printf ("Enter Edge2:\n");
  scanf ("%d", &Edge2);
  
  printf ("Enter Edge3:\n");
  scanf ("%d", &Edge3);
  
  E1P2 = Edge1 * Edge1;
  E2P2 = Edge2 * Edge2;
  E3P2 = Edge3 * Edge3;
  
  if (E1P2 == (E2P2 + E3P2)){
      // Right triangle hypotenuse E1
      printf ("Right Triangle hypotenuse E1\n");
      Area = (Edge2 * Edge3) / 2;
      printf("Your Triangle's Area is: \n");
      printf("%d", Area);
    }
    
  else if (E2P2 == (E1P2 + E3P2)){
      // Right triangle hypotenuse E2
      printf ("Right Triangle hypotenuse E2\n");
      Area = (Edge1 * Edge3) / 2;
      printf("Your Triangle's Area is: \n");
      printf("%d", Area);
    }
    
  else if (E3P2 == (E2P2 + E1P2)){
      // Right triangle hypotenuse E3
        printf("Right Triangle hypotenuse E3\n");
        Area = (Edge2 * Edge1) / 2;
        printf("Your Triangle's Area is: \n");
        printf("%d", Area);
    }
    
    else{
        Perimeter = Edge1 + Edge2 + Edge3;
        printf("Your Triangle's Perimeter is: \n");
        printf("%d", Perimeter);
    }
}

IsLeapYear(){
    
  int InputYear;
  int LeapYear = 1399;
  int Diff;
  
  printf ("Enter Year: \n");
  scanf ("%d", &InputYear);
  Diff = LeapYear - InputYear;
  
  if (Diff % 4 == 0){
      printf("Your input year is the Leap Year.");
  }
  
  else{
      printf("Your input year is NOT the Leap Year.");
  }
  
}

int Mod3511(){
      
  int Input3511;
  int Counter = 0;
  
  printf ("Enter a Number: \n");
  scanf ("%d", &Input3511);
  
  if(Input3511 % 3 == 0){
      Counter = Counter + 1;
  }
  
  if(Input3511 % 5 == 0){
      Counter = Counter + 1;    
  }
  
  if(Input3511 % 11 == 0){
      Counter = Counter + 1;
  }

  if(Counter == 2){
      printf("YES");
  }
  
  else {
      printf("NO");
  }
  
}
