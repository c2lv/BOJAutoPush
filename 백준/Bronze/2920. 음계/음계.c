#include <stdio.h>

int main(void)
{
	int num[8];

	for (int i = 0; i < 8; i++)
		scanf("%d", &num[i]);
	for (int j = 0; j < 8; j++)
	{
		if (num[j] != j + 1)
			break ;
		if (j == 7 && num[j] == j + 1)
		{
			printf("ascending");
			return 0;	
		}
	}
	for (int j = 0; j < 8; j++)
	{
		if (num[j] != 8 - j)
			break ;
		if (j == 7 && num[j] == 8 - j)
		{
			printf("descending");
			return 0;	
		}
	}
	printf("mixed");
	return 0;
}