#include <iostream>
using namespace std;

int main(){
  int A, B, C;
  cin >> A >> B >> C;
  int ans = (A ^ B);

  if((C%2) != 0)
    cout << ans;
  else
    cout << (ans ^ B);
}
