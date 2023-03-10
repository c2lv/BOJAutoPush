#include <stdio.h>

int main(void)
{
	int N, num[1000], temp = 0;

	scanf("%d", &N);
	for (int i = 0; i < N; i++)
		scanf("%d", &num[i]);

	for (int j = N - 1; j > 0; j--)
	{
		for (int k = 0; k < j; k++)
		{
			if (num[k] > num[k + 1])
			{
				temp = num[k];
				num[k] = num[k + 1];
				num[k + 1] = temp;
			}
		}
	}
	for (int l = 0; l < N; l++)
		printf("%d\n", num[l]);
	return 0;
}