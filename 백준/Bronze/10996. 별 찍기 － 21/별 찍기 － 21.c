#include <stdio.h>

int main(void)
{
	int N;

	scanf("%d", &N);	
	for (int i = 0; i < N * 2; i++)
	{
		for (int j = 0; j < N; j++)
		{
			if ((i + j) % 2 == 0)
				printf("*");
			else
				printf(" ");
		}
		if (N != 1)
			printf("\n");
	}
	return 0;
}