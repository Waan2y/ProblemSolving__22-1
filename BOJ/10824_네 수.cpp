#include <iostream>
#include <string>
using namespace std;

int main(){
  string a, b, c, d;          // string 으로 받음
  long long answer;           // 이어지면 int 범위 무조건 초과

  cin >> a >> b >> c >> d;    // 전체 입력

  a += b;                     // 두 string 연결
  c += d;                     //     ..
  answer = stoll(a) + stoll(c);  // long long으로 바꿔서 더해줌

  cout << answer << endl;
}
