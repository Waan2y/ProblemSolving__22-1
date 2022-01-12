#include <string>
#include <vector>
using namespace std;

vector<int> solution(vector<int> lottos, vector<int> win_nums) {
    vector<int> answer;   // vector : answer
    int zero_count = 0;   // count 0
    int coin = 0;         // count coincidence
    int rank_max = 0;     // rank 0
    int rank_min = 0;     //  ..  1

    for(int i=0; i<6; i++){                    // in lottos
        if(lottos[i] == 0){                    // if 0 ?
            zero_count++;                      // count0 ++
            continue;
        }
        else{                                   // not 0 ;
            for(int j=0; j<6; j++){             // in win_nums
                if(lottos[i] == win_nums[j]){   // coincidence ?
                    coin++;                     // count coincidence ++
                    break;
                }
            }
        }
    }
    // calculate rank 
    rank_max = (coin + zero_count) != 0 ? 7 -(coin + zero_count) : 6;
    rank_min = coin != 0 ? 7 -(coin) : 6;

    // set answer
    answer = { rank_max, rank_min };
    return answer;
}
