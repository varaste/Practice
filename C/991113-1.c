#include <stdio.h> 

int Sum = 0;

int main() {
	for(int i=1;i<100;i++){
		if((i%7)==0){
		    printf("%d", i); 
		    printf(", "); 
			Sum = Sum + i;
		}
	}
	printf("\n");
	printf("\n");
    printf("%d", Sum); 
    return 0; 
} 
