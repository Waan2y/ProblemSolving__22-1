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
  for(int i=0; i<N; i++){
    int tmp;
    cin >> tmp;
    A.push_back(tmp);
  }

  for(int i=0; i<N; i++){
    if((~K) & A[i]){
      s = i+1;
      ans = 0;
      continue;
    }
    else{
      ans |= A[i];
      if(ans == K){
        cout << s+1 << ' ' << i+1 << '\n';
        return 0;
      }
    }
  }
  cout << -1 << '\n';
  return 0;
}
