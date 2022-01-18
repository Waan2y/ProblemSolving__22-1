/*     ***   my first answer : WA   ***     */
// 처음 제출한 code가 계속해서 testcase 18, 22에서 WA가 나왔다.
// 계속 생각 했는데 문제는 여기 있었다.
// In case '*' :
if(T == '*'){
  int tmp1 = 0;
  int tmp2 = 0;

  tmp1 = score.back();
  score.pop_back();

  if(!score.empty()){
    tmp2 = score.back();
    score.pop_back();
  }
    score.push_back((tmp1 + tmp2) * 2);
}
// * 이면 앞에 score를 pop 해서 2배해서 push 하면 되겠다 생각 했다
// 그러면 2S2D*2D* 과 같은 형태로 주어지면 결국 3번의 기회 모두에 대해
// 2배를 하게된다.


/*     ***   my second answer : AC   ***     */
#include <string>
#include <vector>
#include <math.h>
using namespace std;

int solution(string dartResult){
    int answer = 0;     // answer
    int num = -1;       // score
    int flag = 0;       // flag
    vector<int> score;  // vector for score result

    for(auto T : dartResult){
      if(isdigit(T)){
        num = ((T == '0') && flag) ? 10 : (T - 48);    // ASCII | 0 : 48
        flag = num;                                    // for detect 10
      }

      else{
        flag = 0;  // end chance , reset flag

        if(T == 'S')
          score.push_back(num);
        if(T == 'D')
          score.push_back(pow(num,2));
        if(T == 'T')
          score.push_back(pow(num,3));

        if(T == '*'){
          int tmp1 = 0;    //score[-1]
          int tmp2 = 0;    //score[-2]

          tmp1 = score.back();  // pop score[-1]
          score.pop_back();

          if(!score.empty()){      // if not '*' comes first ?
            tmp2 = score.back();   // pop score[-2]
            score.pop_back();
            score.push_back(tmp2 *2);   // double score
          }
            score.push_back(tmp1 *2);   // double score
        }

        if(T == '#'){
          int tmp;

          tmp = score.back();
          score.pop_back();
          score.push_back(tmp * (-1));
        }
      }
    }
    // calc answer
    for(auto i : score)
      answer += i;

    return answer;
}


// 다른 정답을 보니 sstream 이라는 라이브러리를 사용했던데
// 처음 보는 라이브러리라 한번 공부해봐야겠다
