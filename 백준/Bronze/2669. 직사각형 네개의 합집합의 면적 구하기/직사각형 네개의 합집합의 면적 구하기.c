#include <stdio.h>

int main(void)
{
	int T = 4, area[100][100] = { 0, }, x1, x2, y1, y2, surface = 0;

	while (T)
	{
		scanf("%d%d%d%d", &x1, &y1, &x2, &y2);

		for (int i = y1; i < y2; i++)
		{
			for (int j = x1; j < x2; j++)
				area[i][j]++;
		}
		T--;
	}
	for (int i = 1; i < 100; i++)
	{
		for (int j = 1; j < 100; j++)
		{
			if (area[i][j])
				surface++;
		}
	}
	printf("%d", surface);

	return 0;
}