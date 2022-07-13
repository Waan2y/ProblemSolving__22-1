/*
~ n-1   | 1  인 타일 채우는 경우의 수 : dp[n-1]  (2x1 로 채우는 법 하나는 그냥 결정됨 )
ㅁㅁㅁㅁ | ㅁ
ㅁㅁㅁㅁ | ㅁ

~ n-2   | 2  인 타일 채우는 경우의 수 : dp[n-1] + ?
ㅁㅁㅁㅁ | ㅁㅁ
ㅁㅁㅁㅁ | ㅁㅁ
dp[n-1] + (2x2 를 1x2 로 채우는 법은 하나로 결정, 2x1 로 채우는 법은 위에서 이미 포함함)

점화식 : dp[n] = dp[n-1] + dp[n-2]

*/

#include <iostream>
using namespace std;

int dp[1001] = {0, };     // dp[n] == 2xn 크기 직사각형 채우는 경우의 수

int get_answer(int n){
  if(n == 1) return dp[1];
  else if(n == 2) return dp[2];
  else if(dp[n]) return dp[n];
  else return dp[n] = ((get_answer(n-1) + get_answer(n-2)) % 10007);
}


int main(){
  ios_base :: sync_with_stdio(false);
  cin.tie(NULL);      cout.tie(NULL);

  dp[1] = 1;
  dp[2] = 2;

  int n = 0;
  cin >> n;
  cout << get_answer(n);
}
