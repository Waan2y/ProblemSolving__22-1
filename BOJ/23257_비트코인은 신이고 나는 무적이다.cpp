// 조합으로 풀어야 하는건가 생각하다가
// 그냥 재귀적으로 풀어도 될 거 같았다

#include <iostream>
#include <set>
#include <math.h>
#include <algorithm>
using namespace std;

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);     cin.tie(NULL);

  set<int> A;       // set 1
  set<int> ans;     // set 2 (answer)
  set<int> tmp;     // 임시 set

  int N, M;
  cin >> N >> M;

  while(N--){            // 입력
    int Ai;
    cin >> Ai;
    A.insert(abs(Ai));
  }
  M--;         // M-1 번 실행할 거
  ans = A;     // 중복 포함 XOR 이니까 복사

  while(M--){                   // M -1 번 실행
    for(int i : A){             // A 전부 순회
      for(int j : ans){         // ans 전부 순회
        tmp.insert(abs(i^j));   // 내부 값 XOR 후 tmp에 insert
      }
    }
    ans = tmp;                  // ans 에 tmp 값 대입
    tmp.clear();                // tmp 는 다시 초기화
  }

  cout << *max_element(ans.begin(), ans.end()) << '\n';  // ans의 최대값이 답임

  return 0;
}
