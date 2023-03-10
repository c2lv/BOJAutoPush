#include <stdio.h>

int main(void)
{
	int i = 0, sum = 0;

	while (i < 8)
	{
		int j;
		char row[9];

		scanf("%s", row);

		j = i % 2 == 0 ? 0 : 1;
		while (j < 8)
		{
			if (row[j] == 'F')
				sum++;
			j += 2;
		}
		i++;
	}
	printf("%d", sum);

	return 0;
}