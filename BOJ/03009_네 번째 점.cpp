// 문제가 원하는 답이 이거였을까
// 두 직선 평행한 점 구해보라 거였을라나
#include <iostream>
using namespace std;

int main(){
  int a[1001] = { 0,};
  int b[1001] = { 0,};
  int tmp1, tmp2;
  int i = 3;

  while(i--){
    cin >> tmp1 >> tmp2;
    a[tmp1]++;
    b[tmp2]++;
  }
  for(int i=0; i<1000; i++){
    if(a[i] == 1)
      tmp1 = i;
    if(b[i] == 1)
      tmp2 = i;
  }
  cout << tmp1 << ' ' << tmp2 << endl;
}
