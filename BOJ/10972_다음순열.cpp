#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);    cout.tie(NULL);

  int N = 0;
  cin >> N;

  vector<int> p(N, 0);

  for(int i=0; i<N; i++){
    int tmp = 0;
    cin >> tmp;
    p[i] = tmp;
  }
  if(next_permutation(p.begin(), p.end()))
    for(int tp : p)
      cout << tp << ' ';
  else
    cout << -1;
}
