#include <iostream>
#include <math.h>
using namespace std;

void min_move(int x, int y){
  int distance = y-x;
  int n = 1;

  while(distance >= pow(n,2))
    n++;
  n -= 1;

  if(distance == pow(n,2))
    cout << 2*n -1 << '\n';
  else if(distance <= n*(n+1))
    cout << 2*n << '\n';
  else
    cout << 2*n +1<< '\n';
}
//   이동 거리  | 이동 형태            | 작동 횟수
//     (n^2)   | 1 2 ...  n  ... 2 1  | 2n-1
//   (n^2 + n) | 1 2 ... n n ... 2 1  | 2n
//   ((n+1)^2) | 1 2 ... n+1 ... 2 1  | 2(n+1)-1 == 2n+1
// 위와 같은 규칙이 성립

int main(){
  int T, tmp1, tmp2;
  cin >> T;

  for(int i=0; i<T; i++){
    cin >> tmp1 >> tmp2;
    min_move(tmp1, tmp2);
  }
}
