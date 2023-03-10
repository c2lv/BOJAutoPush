#include <stdio.h>

int main(void)
{
	int N;

	scanf("%d", &N);

	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j <= i; j++)
			printf("*");
		printf("\n");
	}
	for (int i = N; i < 2 * N - 1; i++)
	{
		for (int j = 2 * N - 1; i < j; j--)
			printf("*");
		printf("\n");
	}

	return 0;
}