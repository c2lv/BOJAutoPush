#include <stdio.h>

int main(void)
{
	int N;

	scanf("%d", &N);

	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j <= i; j++)
			printf("*");
		for (int k = 0; k < 2 * (N - 1) - 2 * i; k++)
			printf(" ");
		for (int l = 0; l <= i; l++)
			printf("*");
		printf("\n");
	}
	for (int i = 0; i < N - 1; i++)
	{
		for (int j = 0; j < N - 1 - i; j++)
			printf("*");
		for (int k = 0; k < 2 * i + 2; k++)
			printf(" ");
		for (int l = 0; l < N - 1 - i; l++)
			printf("*");
		printf("\n");
	}

	return 0;
}