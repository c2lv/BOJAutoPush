#include <stdio.h>

int fibocnt(int n, int before, int after)
{
	if (n == 0)
		return before;
	else if (n == 1)
		return after;
	else
		return fibocnt(n - 1, after, before + after);
}

int main(void)
{
	int T, N;

	scanf("%d", &T);
	for (int i = 0; i < T; i++)
	{
		scanf("%d", &N);

		printf("%d %d\n", fibocnt(N, 1, 0), fibocnt(N, 0, 1));
	}

	return 0;
}