/*     ***   my first answer : AC   ***     */
#include <string>
#include <vector>
#include <math.h>
using namespace std;

int solution(int n){
  int answer = 0;
  vector<int> base_3;

  char tmp;
  int i = 0;

  while(n > 0){              // make base 3 (reverse)
    tmp = n % 3;
    base_3.push_back(tmp);
    n = int(n / 3);
  }

  i = pow(3, base_3.size() - 1);
  for(auto a : base_3){     // make base_3 to base_10
    answer += a * i;
    i /= 3;
  }
  return answer;
}
