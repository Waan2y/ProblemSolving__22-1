#include <iostream>
#include <math.h>
#include <vector>
using namespace std;

vector<int> prime_set;
void make_prime_set(){                         // 먼저 소수 전부 찾음
  for(int i=2; i<10001; i++){
    bool flag = true;
    for(int j=2; j<int((sqrt(i)) + 1); j++){
      if((i % j) == 0){
        flag = false;
        break;
      }
    }
    if(flag)
      prime_set.push_back(i);
  }
}

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);    cout.tie(NULL);

  make_prime_set();

  int T;
  cin >> T;
  while(T--){
    int ans_i = 9999;
    int ans_j = 9999;

    int n;
    cin >> n;                       // n = i+j 인지 확인할거임
    for(auto i : prime_set){        // i : prime_set
      if(i >= ans_j)                // 현재 답인 j 이상인 i 부터는
        break;                      // 자리 바꿔서 더하는 거니까 안봐도 됨
      for(auto j : prime_set){      // j : prime_set
        if(n == (i+j)){             // 답을 만나면
          ans_i = i;                // 현재 답으로 최신화
          ans_j = j;                // 항상 이전 답보다 다음 답이 더 차이가 작음
          break;
        }
      }
    }
    cout << ans_i << " " << ans_j << endl;
  }
}
