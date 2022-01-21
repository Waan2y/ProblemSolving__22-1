/*     ***   my first answer : AC   ***     */
// set 은 중복이 허용되지 않는 점을 가지고 구현 하였다.
#include <vector>
#include <set>
using namespace std;

int solution(vector<int> nums){
    int answer = 0;
    int comp = nums.size() / 2;     // comp : I can get
    set<int> pokémon;               // : nums of diff pokémons

    for (int i : nums)              // make set
      pokémon.insert(i);

    // ans = diff pokémons < I can get ?
    answer = (pokémon.size() < comp) ? pokémon.size() : comp;
    return answer;
}

/*     ***   another answer   ***     */
// set 은 값이 입력, 삭제 될때 자동으로 정렬을 한다.
// 혹시나 시간초과를 줄이기 위해 unordered_set 을 사용한 것 같다.
#include <bits/stdc++.h>
using namespace std;

int solution(vector<int> nums){
    unordered_set<int> s(nums.begin(), nums.end());

    return min(nums.size() / 2, s.size());
}
