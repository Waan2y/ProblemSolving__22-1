// 처음에 모든 경우를 다 구하는 건가 했다
// OR 연산이랑 연속한 구간이라는 점을 생각하며
// 다른 방법으로 구현했다
#include <iostream>
#include <vector>
using namespace std;

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);    cout.tie(NULL);

  vector<int> A;
  int N, K;
  cin >> N >> K;

  int s = 0;
  int ans = 0;
  for(int i=0; i<N; i++){   // 배열 만들기
    int tmp;
    cin >> tmp;
    A.push_back(tmp);
  }

  for(int i=0; i<N; i++){
    if((~K) & A[i]){        // A[i]가 K에 없는 bit를 가지고 있는지
      s = i+1;              // A[i]는 연속 구간에 시작이 될 수 없음
      ans = 0;              // 현재까지 연속구간 answer 초기화
      continue;
    }
    else{                   // A[i]는 K에 없는 bit가 없음
      ans |= A[i];          // 현재 연속구간 anwer 에 OR
      if(ans == K){         // answer ?
        cout << s+1 << ' ' << i+1 << '\n';
        return 0;
      }
    }
  }
  cout << -1 << '\n';
  return 0;
}
