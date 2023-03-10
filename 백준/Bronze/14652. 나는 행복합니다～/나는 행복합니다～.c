#include <stdio.h>

int main(void)
{
	int N, M, K, n, m;

	scanf("%d %d %d", &N, &M, &K);
	n = K / M;
	m = K - n * M;
	printf("%d %d", n, m);
	return 0;
}