#include <iostream>
using namespace std;

int main(){
  int n;
  cin >> n;

  int space = 0;
  for(int i=n; i>=1; i--){
    for(int j=0; j<space; j++)
      cout << " ";
    for(int k=0; k < 2*i-1; k++)
      cout << "*";

    cout << '\n';
    space++;
  }
}
