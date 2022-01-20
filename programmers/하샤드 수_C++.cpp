/*     ***   my first answer : AC   ***     */
#include <string>
#include <vector>
using namespace std;

bool solution(int x) {
    bool answer = false;
    string s_x = to_string(x);   // convert x to string
    int tmp = 0;                 // tmp for sum(digits)

    for(auto i : s_x)            // calc sum(digits)
      tmp += int(i-48);

    if(x % tmp == 0)             // check true?
      answer = true;

    return answer;
}


/*     ***   another answer   ***     */
#include <string>
#include <vector>
using namespace std;

bool solution(int x) {
    bool answer = true;
    int nTemp = x;
    int nSum = 0;
    while (nTemp > 0)
    {
        nSum += nTemp % 10;
        nTemp /= 10;
    }
    return x % nSum == 0 ? true : false;
}
