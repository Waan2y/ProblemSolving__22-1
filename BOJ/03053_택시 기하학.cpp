#include <iostream>
#include <math.h>
using namespace std;

int main(){
  double R;
  cin >> R;
  printf("%6f\n",  M_PI * pow(R,2));
  printf("%6f\n",  2 * pow(R,2));
}
// 택시 기하학에서 D 는 절댓값 차의 합
// D(1,0) == D(0,1) == D(-1,0) == D(0,-1) == D(1/2, 1/2) ...
// 반지름이 R 이면, 넓이 == 2*R^2
