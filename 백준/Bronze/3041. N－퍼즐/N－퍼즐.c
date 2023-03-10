#include <stdio.h>

int max(int a, int b)
{
	return a < b ? b : a;
}

int main(void)
{
	int degree = 0;
	char answer[5][5] = {"ABCD", "EFGH", "IJKL", "MNO."}, puzzle[5][5];

	for (int i = 0; i < 4; i++)
		scanf("%s", puzzle[i]);

	for (int i = 0; i < 15; i++)
	{
		int x1, x2, y1, y2;
		char ans;
		
		x1 = i % 4, y1 = i / 4;
		ans = answer[y1][x1];
		for (int j = 0; j < 16; j++)
		{
			x2 = j % 4, y2 = j / 4;
			if (ans == puzzle[y2][x2])
				break;
		}
		degree += max(x2 - x1, x1 - x2) + max(y2 - y1, y1 - y2);
	}
	printf("%d", degree);

	return 0;
}