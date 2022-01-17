/*     ***   my first answer : AC   ***     */
#include <string>
#include <vector>
using namespace std;

vector<long long> solution(int x, int n){
    vector<long long> answer;
    int tmp;

    for(int i=1; i<n+1; i++){
        tmp = x * i;
        answer.push_back(tmp);
    }
    return answer;
}
