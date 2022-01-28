#include <iostream>
using namespace std;

void what_room(int H, int W, int N){
  int cnt = 0;

  for(int i=1; i<=W; i++){
    for(int j=1; j<=H; j++){
      cnt++;
      if(cnt == N){
        printf("%d%02d\n", j, i);
        return;
      }
    }
  }
}

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);    cout.tie(NULL);

  int T;
  int H, W, N;

  cin >> T;
  for(int i=0; i<T; i++){
    cin >> H >> W >> N;
    what_room(H, W, N);
  }
}
