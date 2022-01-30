#include <iostream>
using namespace std;

int main(){
  int ARR[1000];
  int cnt = 0;
  int i = 0;

  while(i < 1000){              // 수열 만들기
    cnt++;
    for(int j=0; j<cnt; j++){
      if(i == 1000)
        break;
      ARR[i] = cnt;
      i++;
    }
  }

  int A, B;
  int ans = 0;
  cin >> A >> B;

  for(int i=(A-1); i<=(B-1); i++)
    ans += ARR[i];
  cout << ans << endl;
}
