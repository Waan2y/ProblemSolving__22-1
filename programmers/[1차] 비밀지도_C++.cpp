/*     ***   my first answer : AC   ***     */
// 문제대로 구현 하였다. 처음에 단순한 생각에
// 2로 나누다가 1보다 작아지는 상황을 따로 처리해야하나 했는데
// 그냥 int 에서 무조건 0이다
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

vector<string> solution(int n, vector<int> arr1, vector<int> arr2) {
    vector<string> answer;

    for(int i=0; i<n; i++){
      string tmp = "";                            // String use temp

      for(int j=0; j<n; j++){
        if(((arr1[i]%2) || (arr2[i]%2)) == 1)     // If "OR" is 0
         tmp += "#";                              // #
        else
          tmp += " ";                             // else " "

        arr1[i] = int(arr1[i]/2);                 // next bit
        arr2[i] = int(arr2[i]/2);                 //    ..
      }
      reverse(tmp.begin(), tmp.end());            // reverse string
      answer.push_back(tmp);                      // push answer
    }
    return answer;
}


/*     ***   another answer   ***     */
// 미리 OR 를 하고 한비트씩 확인하는 것이 더 좋아보인다.
// string을 뒤집을 생각을 했는데 그냥 앞에 붙이면 되는건데 생각을 못했다
// 시프트 연산자를 사용한 점은 멋있다. 실행시간상 이득인가 ?
#include <string>
#include <vector>
using namespace std;

vector<string> solution(int n, vector<int> arr1, vector<int> arr2) {
    vector<string> answer;
    for(int i=0; i <n; i++){
        arr1[i] = arr1[i]|arr2[i];
        string ans = "";
        for(int j = 0; j<n; j++){
            if(arr1[i] % 2 == 0) ans = " " + ans;
            else ans = "#" + ans;
            arr1[i] = arr1[i] >> 1;
        }
        answer.push_back(ans);
    }
    return answer;
}
