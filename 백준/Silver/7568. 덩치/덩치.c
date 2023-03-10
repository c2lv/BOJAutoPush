#include <stdio.h>

int main(void)
{
	int N; // 2 ≤ N ≤ 50
	int x[50], y[50]; // 10 ≤ x, y ≤ 200
	int rank[50]; // 덩치 등수

	scanf("%d", &N);
	for (int i = 0; i < N; i++)
		scanf("%d%d", &x[i], &y[i]);

	for (int i = 0; i < N; i++)
		rank[i] = 1;
	for (int i = 0; i < N - 1; i++)
	{
		for (int j = i; j < N - 1; j++)
		{
			if (x[i] < x[j + 1] && y[i] < y[j + 1])
				rank[i]++;
			else if (x[i] > x[j + 1] && y[i] > y[j + 1])
				rank[j + 1]++;
		}
	}
	for (int i = 0; i < N; i++)
		printf("%d ", rank[i]);

	return 0;
}