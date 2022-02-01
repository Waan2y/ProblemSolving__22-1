#include <iostream>
using namespace std;

int main(){
  long long N, R;
  cin >> N >> R;
  if(R==1)
    cout << N+R << endl;
  else{
    cout << N + 2*R -1 << endl;
  }
}

// N 종류 중에 1개 짝을 맞추려면
// N종류를 하나씩 뽑고, 이후 아무데서나 하나 뽑아도
// 반드시 1개 짝이 이루어짐.
// 같은 방식으로 R 개 짝 맞추기
