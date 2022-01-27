#include <iostream>
using namespace std;

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);    cout.tie(NULL);

  int N;
  int bits = 0;
  int cnt = 0;

  cin >> N;             // N
  bits = (~N) + 1;      // N 의 2의보수
  bits ^= N;            // N 과 N의 2의보수의 서로 다른 비트를 찾으려면
                        // N 과 N의 2의보수를 XOR 하고 1 만 count 하면 됨
                        // XOR 은 서로 다를 때 1 이니까

  for(int i=0; i<32; i++){  // 32bit 까지만
    if(bits & (1<<i))       //  현재 bit 가 1이면 ?
      cnt++;                // cnt++
  }

  cout << cnt << endl;
}
