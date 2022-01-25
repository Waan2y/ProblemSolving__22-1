#include <iostream>
#include <string.h>
using namespace std;

int main(){
  string s;
  string ans = "";
  string tmp = "";
  bool flag = false;  // reverse 할지(0) 말지(1) 결정

  getline(cin, s);

  for(char c : s){
    if(c == '<'){       // 태그 시작됨
      flag = true;      // 태그 안에서는 reverse 안함
      tmp += '<';       // tmp에 < 추가
      continue;         // 내려가면 중복되니까 바로 다음 c로
    }

    else if(c == '>'){  // 태그 끝남
      flag = false;     // 태그 끝났으니까 이제 reverse 할거임
      tmp += '>';       // tmp에 > 추가
      ans += tmp;       // ans 에 tmp 연결
      tmp = "";         // tmp 초기화
      continue;         // 다음 c으로
    }

    if(c == ' '){  // 공백 입력시 (공백 기준 묶음이 구분됨)
      tmp += ' ';  // tmp에 공백 추가
      ans += tmp;  // 지금 tmp를 ans 에 연결
      tmp = "";    // tmp 초기화
    }
    else if(flag)  // flag:1  just append
      tmp += c;
    else           // flag:0  append reverse
      tmp = c + tmp;
  }

  ans += tmp;      // 띄어쓰기 없이 종료되더라도 tmp에 남은 값 ans에 연결해야댐
  cout << ans << endl;
}
