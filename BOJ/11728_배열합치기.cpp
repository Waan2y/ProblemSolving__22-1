#include <bits/stdc++.h>
using namespace std;

int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);    cout.tie(NULL);
	int n;
	int m;
	cin >> n >> m;

	vector<int> A(n);
	for(int i=0; i<n; i++) cin >> A[i];
	for(int i=0; i<m; i++){
		int tmp;
		cin >> tmp;
		A.push_back(tmp);
	}

	sort(A.begin(), A.end());
	for(int i=0; i<n+m; i++) cout << A[i] << ' ';

	return 0;
}
