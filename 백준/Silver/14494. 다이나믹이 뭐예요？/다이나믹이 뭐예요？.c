#include <stdio.h>

int main(void)
{
	int n, m;
	unsigned long long D[1000][1000] = { 0, };

	scanf("%d %d", &n, &m);

	for (int i = 0; i < 1000; i++)
	{
		D[0][i] = 1;
		D[i][0] = 1;
	}
	for (int i = 1; i < m; i++)
	{
		for (int j = 1; j < n; j++)
		{
			D[i][j] = (D[i - 1][j] + D[i][j - 1] + D[i - 1][j - 1]) % 1000000007;
		}
	}
	printf("%llu", D[m - 1][n - 1]);

	return 0;
}