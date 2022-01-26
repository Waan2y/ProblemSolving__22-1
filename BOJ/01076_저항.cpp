#include <iostream>
#include <string>
#include <math.h>
using namespace std;

int main(){
  string res[10] = { "black", "brown", "red", "orange", "yellow",
                     "green", "blue", "violet", "grey", "white" };
  string color[3];
  long long answer = 0;

  for(int i=0; i<3; i++){
    string tmp;
    cin >> tmp;
    for(int j=0; j<10; j++){
      if(tmp == res[j]){
        if(i == 2){
          answer *= pow(10, j);
        }
        else{
          answer += (j * pow(10, 1-i));
        }
      }
    }
  }
  cout << answer << endl;

  return 0;
}
