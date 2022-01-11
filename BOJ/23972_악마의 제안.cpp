#include <stdio.h>
#include <math.h>
int main(){
	long K, N;
	long X = 0;

	scanf("%ld %ld", &K, &N);

	if (N == 1)
		X = -1;

	else{
		long i = ceil(double(K) / double(N-1));
		X = K + i;
	}

	printf("%ld", X);
	return 0;
}
