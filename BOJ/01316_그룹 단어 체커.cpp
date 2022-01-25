#include <iostream>
#include <string>
using namespace std;

int is_group(string s){    // 그룹단어임 ?
  char now;                // now : 현재 연속중인 값
  string tmp;              // tmp : 이전에 연속되던 값

  for(char a : s){         // string 전체 순회
    if(a != now){          // now 아니고 새로운 값 ?
      for(char b: tmp)     // tmp 순회
        if(a == b)         // tmp 안에 같은 값이 있다 ? ( 이전에 연속된 적 있다 )
          return 0;        // 그룹 단어 아님
                           // 이전에 연속된적 없던 새로운 값이다 ?
      tmp += now;          // a 이전까지 연속되던 now 를 tmp에 저장
      now = a;             // a 가 지금부터 연속중인 값
    }
  }
  return 1;
}

int main(){
  int N = 0;
  int ans = 0;
  string s = "";
  cin >> N;

  for(int i=0; i<N; i++){
    cin >> s;
    ans += is_group(s);
  }
  cout << ans << endl;
}
