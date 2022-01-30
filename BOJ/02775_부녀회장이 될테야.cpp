#include <iostream>
using namespace std;

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);    cout.tie(NULL);
                              // APT 만들기
                              // i 층의 j 호 거주민 ==
                              // 같은 층 이전 호 + 아래 층 같은 호
  int APT[15][15];
  for(int k=0; k<15; k++){    // 0층 채우기
    APT[0][k] = k;            // 0층의 k 호에는 k 명 이 거주
    APT[k][0] = 0;            // 1호에서 이전 호에 접근하면
                              // 배열범위 밖이니까 모든 층에 가상의 0호에 0명 거주
  }
  for(int i=1; i<15; i++)                      // i 층
    for(int j=1; j<15; j++)                    // j 호
      APT[i][j] = APT[i][j-1] + APT[i-1][j];   // 규칙대로 입력

  int T;
  cin >> T;
  for(int i=0; i<T; i++){
    int tmp1, tmp2;
    cin >> tmp1 >> tmp2;
    cout << APT[tmp1][tmp2] << endl;
  }
}
