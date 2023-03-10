#include <stdio.h>

int main(void)
{
	int A, B, C; // 5분, 1분, 10초
	int T; // 요리해야 할 시간(초, 1 ≤ T ≤ 10,000)

	scanf("%d", &T);

	A = T / 300;
	B = T % 300 / 60;
	C = T % 60 / 10;
	if (T % 10)
	{
		printf("-1");
		return 0;
	}
	printf("%d %d %d", A, B, C);

	return 0;
}