#include <iostream>
#include <algorithm>
using namespace std;



void print_2by3_matrix(int TwobyThree_Matrix[2][3]);
int calc_2by3_sums(int TwobyThree_Matrix[2][3]);

void print_3by2_matrix(int ThreebyTwo_Matrix[3][2]);
int calc_3by2_sums(int ThreebyTwo_Matrix[3][2]);

int main(){
	ios_base :: sync_with_stdio(false);
	cin.tie(NULL);	    cout.tie(NULL);

	int N, M;                                 // N * M 행렬 : arr[N][M]
	int tmp_val;


  int Matrix[501][501] = {-1, };
  int TwobyThree_Matrix[2][3] = {-1, };
  int ThreebyTwo_Matrix[3][2] = {-1, };
  int answer = 0;

	cin >> N >> M;

	for(int i=0; i<N; i++){
		for(int j=0; j<M; j++){
			cin >> tmp_val;
			Matrix[i][j] = tmp_val;
		}
	}

  // calc I blobk
  for(int horiz = 0; horiz < N; horiz++){
    for(int vert = 0; vert+3 < M; vert++){
      int tmp = Matrix[horiz][vert] + Matrix[horiz][vert+1] +
                    Matrix[horiz][vert+2] + Matrix[horiz][vert+3];
      answer = (answer < tmp)? tmp : answer;
    }
  }
  for(int horiz = 0; horiz+3 < N; horiz++){
    for(int vert = 0; vert< M; vert++){
      int tmp = Matrix[horiz][vert] + Matrix[horiz+1][vert] +
                    Matrix[horiz+2][vert] + Matrix[horiz+3][vert];
      answer = (answer < tmp)? tmp : answer;
    }
  }

  // make 2 x 3 Matrix
  for(int horiz = 0; horiz+1 < N; horiz++){
    for(int vert = 0; vert+2 < M; vert++){
      TwobyThree_Matrix[0][0] = Matrix[horiz][vert];
      TwobyThree_Matrix[0][1] = Matrix[horiz][vert+1];
      TwobyThree_Matrix[0][2] = Matrix[horiz][vert+2];

      TwobyThree_Matrix[1][0] = Matrix[horiz+1][vert];
      TwobyThree_Matrix[1][1] = Matrix[horiz+1][vert+1];
      TwobyThree_Matrix[1][2] = Matrix[horiz+1][vert+2];

      int tmp = calc_2by3_sums(TwobyThree_Matrix);
      answer = (answer < tmp)? tmp : answer;
    }
  }

  // make 3 x 2 Matrix
  for(int horiz = 0; horiz+2 < N; horiz++){
    for(int vert = 0; vert+1 < M; vert++){
      ThreebyTwo_Matrix[0][0] = Matrix[horiz][vert];
      ThreebyTwo_Matrix[0][1] = Matrix[horiz][vert+1];

      ThreebyTwo_Matrix[1][0] = Matrix[horiz+1][vert];
      ThreebyTwo_Matrix[1][1] = Matrix[horiz+1][vert+1];

      ThreebyTwo_Matrix[2][0] = Matrix[horiz+2][vert];
      ThreebyTwo_Matrix[2][1] = Matrix[horiz+2][vert+1];

      int tmp = calc_3by2_sums(ThreebyTwo_Matrix);
      answer = (answer < tmp)? tmp : answer;
    }
  }

  cout << answer << '\n';
	return 0;
}














// functions
void print_2by3_matrix(int TwobyThree_Matrix[2][3]){
  // print Matrix
  cout << '\n';
  for(int i=0; i<2; i++){
    for(int j=0; j<3; j++){
      cout << TwobyThree_Matrix[i][j] << " ";
    }
    cout << '\n';
  }
}

void print_3by2_matrix(int ThreebyTwo_Matrix[3][2]){
  // print Matrix
  cout << '\n';
  for(int i=0; i<3; i++){
    for(int j=0; j<2; j++){
      cout << ThreebyTwo_Matrix[i][j] << " ";
    }
    cout << '\n';
  }
}

int calc_2by3_sums(int TwobyThree_Matrix[2][3]){
  //  00 01 02
  //  10 11 12

  int top_sum = TwobyThree_Matrix[0][0] + TwobyThree_Matrix[0][1] + TwobyThree_Matrix[0][2];
  int bottom_sum = TwobyThree_Matrix[1][0] + TwobyThree_Matrix[1][1] + TwobyThree_Matrix[1][2];
  int mid_sum = TwobyThree_Matrix[0][1] + TwobyThree_Matrix[1][1];

  int O_sum1 = TwobyThree_Matrix[0][0] + TwobyThree_Matrix[1][0] + mid_sum;
  int O_sum2 = TwobyThree_Matrix[0][2] + TwobyThree_Matrix[1][2] + mid_sum;

  int L_sum1 = top_sum + TwobyThree_Matrix[1][0];
  int L_sum2 = top_sum + TwobyThree_Matrix[1][2];
  int L_sum3 = bottom_sum + TwobyThree_Matrix[0][0];
  int L_sum4 = bottom_sum + TwobyThree_Matrix[0][2];

  int T_sum1 = top_sum + TwobyThree_Matrix[1][1];
  int T_sum2 = bottom_sum + TwobyThree_Matrix[0][1];

  int Z_sum1 = mid_sum + TwobyThree_Matrix[1][0] + TwobyThree_Matrix[0][2];
  int Z_sum2 = mid_sum + TwobyThree_Matrix[0][0] + TwobyThree_Matrix[1][2];


  return max({O_sum1, O_sum2, L_sum1, L_sum2, L_sum3, L_sum4,
                Z_sum1, Z_sum2, T_sum1, T_sum2});
}

int calc_3by2_sums(int ThreebyTwo_Matrix[3][2]){
  //  00 01
  //  10 11
  //  20 21
  int left_sum = ThreebyTwo_Matrix[0][0] + ThreebyTwo_Matrix[1][0] + ThreebyTwo_Matrix[2][0];
  int right_sum = ThreebyTwo_Matrix[0][1] + ThreebyTwo_Matrix[1][1] + ThreebyTwo_Matrix[2][1];
  int mid_sum = ThreebyTwo_Matrix[1][0] + ThreebyTwo_Matrix[1][1];

  int O_sum1 = ThreebyTwo_Matrix[0][0] + ThreebyTwo_Matrix[0][1] + mid_sum;
  int O_sum2 = ThreebyTwo_Matrix[2][0] + ThreebyTwo_Matrix[2][1] + mid_sum;

  int L_sum1 = left_sum + ThreebyTwo_Matrix[0][1];
  int L_sum2 = left_sum + ThreebyTwo_Matrix[2][1];
  int L_sum3 = right_sum + ThreebyTwo_Matrix[0][0];
  int L_sum4 = right_sum + ThreebyTwo_Matrix[2][0];

  int T_sum1 = right_sum + ThreebyTwo_Matrix[1][0];
  int T_sum2 = left_sum + ThreebyTwo_Matrix[1][1];

  int Z_sum1 = ThreebyTwo_Matrix[0][0] + mid_sum + ThreebyTwo_Matrix[2][1];
  int Z_sum2 = ThreebyTwo_Matrix[0][1] + mid_sum + ThreebyTwo_Matrix[2][0];

  /*
  cout << "=====" << endl;
  cout << O_sum1 << endl;
  cout << O_sum2 << endl;
  cout << L_sum1 << endl;
  cout << L_sum2 << endl;
  cout << L_sum3  << endl;
  cout << L_sum4 << endl;

  cout << Z_sum1 << endl;
  cout << Z_sum2 << endl;
  cout << T_sum1 << endl;
  cout <<  T_sum2  << endl;
  */

  return max({O_sum1, O_sum2, L_sum1, L_sum2, L_sum3, L_sum4,
                Z_sum1, Z_sum2, T_sum1, T_sum2});
}
