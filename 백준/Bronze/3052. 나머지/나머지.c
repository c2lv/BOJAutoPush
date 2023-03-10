#include <stdio.h>

int main(void)
{
	int N[10]; // 0~1000
	int cnt = 0;

	for (int i = 0; i < 10; i++)
		scanf("%d", &N[i]);

	for (int j = 0; j < 10; j++)
	{
		int isOverlap = 0; // 중복되면 1, 중복되지 않으면 0

		N[j] = N[j] % 42;
		for (int k = 0; k < j; k++)
		{
			if (N[j] == N[k])
				isOverlap = 1;
		}
		if (!isOverlap)
			cnt++;
	}
	printf("%d", cnt);

	return 0;
}