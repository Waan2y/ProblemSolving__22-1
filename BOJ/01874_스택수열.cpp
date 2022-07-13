#include <bits/stdc++.h>
using namespace std;

int main(){
	vector<int> nums;
	vector<int> stack;
	string ans = "";
	int push_num = 1;

	int n;
	cin >> n;
	while(n--){
		int tmp;
		cin >> tmp;

		while(push_num <= tmp){
			stack.push_back(push_num);
			ans += "+";
			push_num++;
		}

		if(stack.back() == tmp){
			ans += "-";
			stack.pop_back();
		}

		else{
			ans.clear();
			ans = "NO";
			break;
		}
	}

	if(ans == "NO") cout << "NO";
	else{
		for(auto i : ans)
			cout << i << '\n';
	}
	return 0;
}
