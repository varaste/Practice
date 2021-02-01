3)


#include <stdio.h>
#include <string.h>
 
main() {
    
    int Smallest;
    int Secondsmallest;
    int array[100];
    int size
    int i;
    
    printf("\n How many elements do you want to enter: ");
    scanf("%d", &size);
    printf("\nEnter %d elements: ", size);
    for (int i = 0 ; i < size; i++)
        scanf("%d", &array[i]);
    if (array[0] < array[1]) {
        Smallest = array[0];
        Secondsmallest = array[1];
    }
    else {
      Smallest = array[1];
      Secondsmallest = array[0];
    }
    for (i = 2; i < size; i++) {
        if (array[i] < Smallest) {
        Secondsmallest = Smallest;
        Smallest = array[i];
        }
        else if (array[i] < Secondsmallest) {
            Secondsmallest = array[i];
        }
    }
    printf(" \nSecond smallest element is %d", Secondsmallest);
}
