#include <stdio.h>

int main(void)
{
	// W는 사용되지 않음
	// Y는 층 수, X는 엘리베이터에서부터 세었을 때의 번호
	int T, H, W, N, X = 1, Y = 1;

	scanf("%d", &T);
	for (int i = 0; i < T; i++)
	{
		scanf("%d %d %d", &H, &W, &N);
		for (int j = 1; j < N; j++)
		{
			// printf("%d: %d\n", j, 100 * Y + X);
			if (Y < H)
				Y++;
			else
			{
				Y = 1;
				X++;
			}
		}
		printf("%d\n", 100 * Y + X);
		X = 1;
		Y = 1;
	}
	return 0;
}