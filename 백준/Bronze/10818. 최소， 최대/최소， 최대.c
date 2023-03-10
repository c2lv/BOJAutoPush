#include <stdio.h>

int main(void)
{
	int N;

	scanf("%d", &N);
	int num[N - 1];
	for (int i = 0; i < N; i++)
		scanf("%d", &num[i]);
	int max = num[0], min = num[0];
	for (int j = 1; j < N; j++)
	{
		if (num[j] > max)
			max = num[j];
		else if (num[j] < min)
			min = num[j];
	}
	printf("%d %d", min, max);
	return 0;
}