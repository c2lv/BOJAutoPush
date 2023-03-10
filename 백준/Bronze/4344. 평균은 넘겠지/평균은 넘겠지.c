#include <stdio.h>

int main(void)
{
	int C;

	scanf("%d", &C);
	for (int i = 0; i < C; i++)
	{
		int N, over = 0;
		double num[1000] = { 0 }, average, sum = 0;

		scanf("%d", &N);
		for (int j = 0; j < N; j++)
		{
			scanf("%lf", &num[j]);
			sum += num[j];
		}
		average = sum / N;
		for (int k = 0; k < N; k++)
		{
			if (num[k] > average)
				over++;
		}

		printf("%.3lf%%\n", (double)over / (double)N * 100);
	}

	return 0;
}