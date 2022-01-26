#include <iostream>
#include <string>
using namespace std;

int main(){
  ios_base::sync_with_stdio(false);     // cin cout 속도 향상
  cin.tie(NULL);                        //       ..
  cout.tie(NULL);                       //       ..

  int bits = 0;

  int M;
  cin >> M;
  while(M--){
    string cmd;
    int x;
    cin >> cmd;

    if(cmd == "add"){
      cin >> x;
      bits |= (1<<x);
    }
    else if(cmd == "remove"){
      cin >> x;
      bits &= ~(1<<x);
    }
    else if(cmd == "check"){
      cin >> x;
      if(bits & (1<<x))
        cout << "1\n";
      else
        cout << "0\n";
    }
    else if(cmd == "toggle"){
      cin >> x;
      bits ^= (1<<x);
    }
    else if(cmd == "all"){
      bits = ((1<<21) -1);    // (1<<n) -1 : n bit 아래 모두 1
    }
    else
      bits = 0;
  }
  return 0;
}
