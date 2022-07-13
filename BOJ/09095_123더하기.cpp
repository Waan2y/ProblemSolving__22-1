/*
[n] = 1,2,3 으로 n 을 표현하는 방법의 수

[1] => 1 | _ | _                                                                      1 0 0 | 1
[2] => 11 | 2 | _                                                                     1 1 0 | 2
[3] => 111 12 | 21 | 3                                                                2 1 1 | 4
[4] => 1111 112 121 13 | 211 22 | 31                                                  4 2 1 | 7
[5] => 11111 1112 1121 1211 122 123 132 | 2111 212 221 23 | 311 32                    7 4 2 | 13
[6] => 111111 11112 11121 11211 12111 1122 1211 1221 1113 1131 1311 123 132          13 7 4 | 24
        | 21111 2211 2121 2112 222 231 213 | 3111 321 312 33

=> 1을 1, 2, 3 으로만 나타내니까
[n] 을 표현할라면 (1 + [n-1]) + (2 + [n-2]) + (3 + [n-3]) ... 점화식
*/

#include <iostream>
using namespace std;

int dp[11] = {0, };

int get_answer(int n){
  if(n == 1) return dp[1];
  else if(n ==2) return dp[2];
  else if(n ==3) return dp[3];
  else if(dp[n]) return dp[n];
  else return dp[n] = (get_answer(n-1) + get_answer(n-2) + get_answer(n-3));
}


int main(){
  ios_base :: sync_with_stdio(false);
  cin.tie(NULL);      cout.tie(NULL);

  dp[1] = 1;
  dp[2] = 2;
  dp[3] = 4;

  int T = 0;
  int n = 0;

  cin >> T;
  while(T--){
    cin >> n;
    cout << get_answer(n) << '\n';
  }

  return 0;
}
