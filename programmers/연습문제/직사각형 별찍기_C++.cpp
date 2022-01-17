/*     ***   my first answer : AC   ***     */
#include <iostream>
using namespace std;

int main(void){
    int column, raw;
    cin >> column >> raw;

    for(int i=0; i<raw; i++){
      for(int j=0; j<column; j++)
        printf("*");
      printf("\n");
    }
    return 0;
}
