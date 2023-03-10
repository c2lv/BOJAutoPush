#include <stdio.h>

int N;

void headfoot()
{
	for (int i = 0; i < N; i++)
		printf("*");
	for (int i = 0; i < 2 * N - 3; i++)
		printf(" ");
	for (int i = 0; i < N; i++)
		printf("*");
}

void middle()
{
	for (int j = 0; j < N - 2; j++)
		printf(" ");
	printf("*");
}

int main(void)
{
	scanf("%d", &N);

	headfoot();
	printf("\n");
	for (int i = 0; i < 2 * N - 3; i++)
	{
		if (i < N - 1)
		{
			for (int j = 0; j < i + 1; j++)
				printf(" ");
		}
		else
		{
			for (int j = i; j < 2 * N - 3; j++)
				printf(" ");
		}
		printf("*");
		middle();
		if (i != N - 2)
		{
			if (i < N - 2)
			{
				for (int j = 0; j < 2 * (N - i) - 5; j++)
					printf(" ");
			}
			else
			{
				for (int j = 0; j < 2 * (i - N) + 3; j++)
					printf(" ");
			}
			printf("*");
		}
		middle();
		printf("\n");
	}
	headfoot();
	return 0;
}