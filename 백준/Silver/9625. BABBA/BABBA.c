#include <stdio.h>

void BABBA(int K, int A, int B)
{
	if (K < 2)
		printf("%d %d", A, B);
	else
		BABBA(K - 1, B, A + B);
}

int main(void)
{
	int K;

	scanf("%d", &K);

	BABBA(K, 0, 1);

	return 0;
}