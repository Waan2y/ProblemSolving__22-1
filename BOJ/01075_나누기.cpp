#include <iostream>
#include <math.h>
using namespace std;

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);    cout.tie(NULL);

  string N;
  string tmp = "";

  int F;
  int num;

  cin >> N >> F;

  for(int i=0; i<N.length()-2; i++)
    tmp += N[i];
  tmp += "00";
  num = stoi(tmp);
  while(true){
    if(num % F == 0){
      break;
    }
    else{
      num++;
    }
  }

  tmp = "";
  tmp =  to_string(num);
  cout << tmp[tmp.length()-2] << tmp[tmp.length()-1] << '\n';
  return 0;
}
