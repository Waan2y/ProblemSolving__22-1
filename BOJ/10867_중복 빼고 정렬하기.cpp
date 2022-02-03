#include <iostream>
#include <set>
using namespace std;

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);    cout.tie(NULL);

  set<int> num_set;
  int s;
  cin >> s;
  for(int i=0; i<s; i++){
    int tmp;
    cin >> tmp;
    num_set.insert(tmp);   // set 은 중복 입력 불가 + 입력시 정렬
  }

  for(int ans : num_set)
    cout << ans << ' ';
}
