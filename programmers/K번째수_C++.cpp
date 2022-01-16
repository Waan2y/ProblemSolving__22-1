/*     ***   my first answer : AC   ***     */
// 단순히 배열로 구현하면 된다
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

vector<int> solution(vector<int> array, vector<vector<int>> commands){
    vector<int> answer;  // answer
    vector<int> tmp;     // vector to use temporarily

    for(int i = 0; i < commands.size(); i++){  // loop : commands size
      tmp = { };                               // reset tmp vector;
      for(int j = commands[i][0] - 1; j < commands[i][1]; j++) // make tmp vector
        tmp.push_back(array[j]);

      sort(tmp.begin(), tmp.end());               // sorting
      answer.push_back(tmp[commands[i][2] - 1]);  // make answer
    }
    return answer;
}


/*     ***   another answer   ***     */
// 다른 풀이와 유사하다
// 크게 다른 점 :
temp = array;
sort(temp.begin() + commands[i][0] - 1, temp.begin() + commands[i][1]);
// 위와 같이 구현하여 이중 for문을 사용하지 않고 구현하는 방법
