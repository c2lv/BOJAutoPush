#include <stdio.h>

int main(void)
{
	int N[9], max = 1, index = 0;

	for(int i = 0; i < 9; i++)
	{	
		scanf("%d", &N[i]);
		// printf("N[%d]: %d\n", i, N[i]);
	}
	for(int j = 0; j < 9; j++)
	{
		if (N[j] > max)
		{
			max = N[j];
			index = j;
		}
	}
	printf("%d\n%d", max, index + 1);
	return 0;
}