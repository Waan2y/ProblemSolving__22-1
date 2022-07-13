#include <bits/stdc++.h>
using namespace std;

long long int dp[1000001];

void make_f(){
	for(int i=1; i<1000001; i++){   // 100만 + 50만 + 33만 + ... +1 <  1억
		int j = 1;
		while(i*j<1000001){
			dp[i*j] += i;
			j++;
		}
	}
}
void make_g(){
	for(int i=1; i < 1000000; i++){   // 100만
		dp[i+1] += dp[i];
	}
}

// ---> 다해도 O(N) 일듯

int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);    cout.tie(NULL);

	make_f();
	make_g();

	int T;
	cin >> T;

	int n;
	while(T--){
		cin >> n;
		cout << dp[n] << '\n';
	}

	return 0;
}
