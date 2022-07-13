#include <bits/stdc++.h>
using namespace std;

int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);    cout.tie(NULL);

	int T;
	cin >> T;
	while(T--){
		int answer
		 = 0;
		int m, n, x, y;
		cin >> m >> n >> x >> y;

		int tmp = x;
		int cnt = 0;
		int calc = 0;
		while(true){
			if(tmp > (m*n)+1){
				answer = -1;
				break;
			}

			calc = (tmp % n)? (tmp % n) : n;
			if(calc == y){
				answer += (cnt * m);
				break;
			}
			tmp += m;
			cnt++;
		}

		if(answer == -1) cout << answer << '\n';
		else cout << answer + x << '\n';
	}

	return 0;
}
