#include <stdio.h>

int main(void)
{
	long N, M, output;

	scanf("%ld %ld", &N, &M);
	output = N - M;
	if (output < 0)
		output *= -1;
	printf("%ld", output);
	return 0;
}