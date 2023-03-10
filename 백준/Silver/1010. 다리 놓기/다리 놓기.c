#include <stdio.h>

int main(void)
{
	int T, N, M;
	unsigned long long noc; // Number of cases

	scanf("%d", &T);
	for (int i = 0; i < T; i++)
	{
		scanf("%d%d", &N, &M);

		noc = 1;
		if (M < N * 2)
			N = M - N;
		for (int j = M; M - N < j; j--)
			noc *= j;
		for (int j = 2; j < N + 1; j++)
			noc /= j;
		printf("%llu\n", noc);
	}

	return 0;
}