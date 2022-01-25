// 문제대로 구현
#include <iostream>
using namespace std;

int what_cpu(int a, int b){
  int a2[4] = { 6, 2, 4, 8 };   // 순환하는 일의 자리 미리 저장한 배열
  int a3[4] = { 1, 3, 9, 7 };
  int a4[2] = { 6, 4 };
  int a7[4] = { 1, 7, 9, 3 };
  int a8[4] = { 6, 8, 4, 2 };
  int a9[2] = { 1, 9 };

  int k = a % 10;
  switch(k){             // 입력된 a 의 일의 자리 보면 어떻게 순환할지 나옴
    case 0:
      return 10;
    case 1:
      return 1;
    case 2:
      return a2[b%4];
    case 3:
      return a3[b%4];
    case 4:
      return a4[b%2];
    case 5:
      return 5;
    case 6:
      return 6;
    case 7:
      return a7[b%4];
    case 8:
      return a8[b%4];
    case 9:
      return a9[b%2];
  }
  return -1;  // 여기 오면 뭔가 잘못된거
}


int main(){
  int T;
  cin >> T;

  for(int i=0; i<T; i++){
    int a, b;
    cin >> a >> b;
    cout << what_cpu(a,b) << endl;
  }
  return 0;
}
