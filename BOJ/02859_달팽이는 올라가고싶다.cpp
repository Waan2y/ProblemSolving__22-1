#include <iostream>
#include <math.h>
using namespace std;

int main(){
  double A, B, V;
  cin >> A >> B >> V;
  long long T = ceil((V-A) / (A-B));
  cout << T + 1 << '\n';
}

// 시간제한 0.15s + 정수 범위보면 O(1)에 끝나야됨.
// 정상을 넘어서는 안내려옴
// == 한번에 A-B씩 오르다, V-A 에 도착하면
// 다음 날에 반드시 정상에 도착.
