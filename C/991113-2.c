#include <stdio.h> 

int InputNum;
int Max = 0;
int Min = 0;
int Ave = 0;
int SumNumbers = 0;
int Numbers[100];

int main() {
	
	for(int i=0;i<10;i++){
		scanf ("%d", &InputNum);
        Numbers[i] = InputNum;
	}
	
	// Calculating Max
	for(int j=0;j<10;j++){
	    Numbers[0] = Max;
	    if(Numbers[j]>Max){
	        Max = Numbers[j];
	    }
	}
	printf("Maximum of your input numbers is:"); 
    printf("%d", Max);
    printf("\n");

    // Calculating Min
	for(int j=0;j<10;j++){
	    Numbers[0] = Min;
	    if(Numbers[j]<Min){
	        Min = Numbers[j];
	    }
	}
	printf("Minimum of your input numbers is:"); 
    printf("%d", Min); 
    printf("\n");
        
	// Calculating Average
	for(int j=0;j<10;j++){
	    SumNumbers = SumNumbers + Numbers[j];
	}
	Ave = SumNumbers / 10;
    printf("Average of your input numbers is:"); 
    printf("%d", Ave); 
    printf("\n");

    return 0; 
} 
