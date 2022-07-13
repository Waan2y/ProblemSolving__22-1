/*
	P : 1 1 1 2 2 3 4 5 7 9 12 ...
	            1 1 1 2 2 3

	P(k) = P(k-1) + P(k-5) ... k >= 6
*/

#include <bits/stdc++.h>
using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);	  cout.tie(NULL);

	vector<uint64_t> P = {0, 1, 1, 1, 2, 2};
	for(int i=6; i<101; i++)
		P.push_back(P[i-1] + P[i-5]);

	int T;
	int n;
	cin >> T;

	while(T--){
	cin >> n;
	cout << P[n] << '\n';
	}
}
