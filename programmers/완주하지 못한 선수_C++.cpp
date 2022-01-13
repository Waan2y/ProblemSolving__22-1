/*     ***   my first answer : TLE   ***     */
// 단순히 생각나는 대로 구현했더니 시간 초과 났다
// 전부 값을 변경하면서 순회해서 O(n^2)이라 그런듯
#include <string>
#include <vector>
using namespace std;

string solution(vector<string> participant, vector<string> completion) {
    string answer = "";            // answer
    for(auto& i: participant){     // participant traversal
      for(auto& j: completion){    // completion  traversal
        if(i == j){                // if same ?
          i = "0";                 // set "0"
          j = "0";                 //   ..
        }
      }
    }

  // set answer
  for(auto& i: participant)  // participant traversal
    if(i != "0")             // if not "0" ?
      answer = i;            // It is answer

  return answer;
}


/*     ***   my Second answer : AC   ***     */
// 전부 정렬되어있다면 중복되더라도 반드시 같은 순서에 같은 값임
// 만약 순서상 가장 마지막이 답이면 두 vector 크기가 다르므로 연산불가
// 정렬된 completion vector 에 "0" 을 추가
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

string solution(vector<string> participant, vector<string> completion) {
    string answer = "";  // answer
    int i = 0;           // index

    sort(participant.begin(), participant.end());  // sort participant
    sort(completion.begin(), completion.end());    // sort completion
    completion.push_back("0");                     // append "0" at completion

    while(true){
      if(participant[i] == completion[i])    // if same?
        i++;                                 // index++
      else                                   // if not same ?
        return participant[i];               // It is answer
    }
}

/*     ***   another answer   ***     */
// hash map 을 사용해서 푸는 방법도 있다
// 더 간단하고 직관적으로 구현되는 방법인 듯
#include <string>
#include <vector>
#include <unordered_map>
using namespace std;

string solution(vector<string> participant, vector<string> completion){
    string answer = "";                // answer
    unordered_map<string, int> temp;   // hash map

    for (string name : participant)    // participant traversal : name
        temp[name]++;                  // key : name  value++

    for (string name : completion)     // completion traversal : name
      temp[name]--;                    // key : name  value--

    for (auto pair : temp){            // completion traversal : pair
      if (pair.second > 0){            // if pair.value > 0
        answer = pair.first;           // This pair.name is answer
        break;
      }
    }
    return answer;
}
