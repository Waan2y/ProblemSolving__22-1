/*     ***   my first answer : AC   ***     */
// 문제대로 구현했는데 이게 맞나 싶었다
#include <string>
#include <vector>
using namespace std;

int solution(string s) {
    string answer = "";         // answer : string
    int i = 0;                  // index

    while(i<s.size()){          // string s _traversal
      if(s[i] == 'z'){          // case 0
        answer += '0';          // answer append '0'
        i += 4;                 // index +4 ; "zero".length == 4
      }
      else if(s[i] == 'o'){    // case 1
        answer += '1';         // .. same as case 0
        i += 3;                // ..
      }
      else if(s[i] == 't' && s[i+1] == 'w'){   // case 2
        answer += '2';
        i += 3;
        continue;
      }
      else if(s[i] == 't' && s[i+1] == 'h'){   // case 3
        answer += '3';
        i += 5;
      }
      else if(s[i] == 'f' && s[i+1] == 'o'){   // case 4
        answer += '4';
        i += 4;
      }
      else if(s[i] == 'f' && s[i+1] == 'i'){   // case 5
        answer += '5';
        i += 4;
      }
      else if(s[i] == 's' && s[i+1] == 'i'){   // case 6
        answer += '6';
        i += 3;
      }
      else if(s[i] == 's' && s[i+1] == 'e'){   // case 7
        answer += '7';
        i += 5;
      }
      else if(s[i] == 'e'){                    // case 8
        answer += '8';
        i += 5;
      }
      else if(s[i] == 'n'){                    // case 9
        answer += '9';
        i += 4;
      }
      else{                                    // case nums (0 to 9)
        answer += s[i];
        i++;
      }
    }

    return stoi(answer);  // convert string to int
}


/*     ***   another answer   ***     */
// 정규 표현식을 사용한 풀이이다.
// C++11 부터 표준에 포함되었다고 한다
// 새로 알게된 내용이고 C++ 에서 문자열 다룰 때 매우 유용한 것 같다
#include <bits/stdc++.h>
using namespace std;

int solution(string s) {
    s = regex_replace(s, regex("zero"), "0");
    s = regex_replace(s, regex("one"), "1");
    s = regex_replace(s, regex("two"), "2");
    s = regex_replace(s, regex("three"), "3");
    s = regex_replace(s, regex("four"), "4");
    s = regex_replace(s, regex("five"), "5");
    s = regex_replace(s, regex("six"), "6");
    s = regex_replace(s, regex("seven"), "7");
    s = regex_replace(s, regex("eight"), "8");
    s = regex_replace(s, regex("nine"), "9");
    return stoi(s);
}
