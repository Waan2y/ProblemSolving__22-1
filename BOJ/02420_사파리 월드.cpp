#include <iostream>
#include <math.h>
using namespace std;

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);    cout.tie(NULL);
  long long N, M;
  cin >> N >> M;
  cout << abs(N-M) << '\n';

  return 0;
}
