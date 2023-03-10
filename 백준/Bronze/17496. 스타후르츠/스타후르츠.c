#include <stdio.h>

int main(void)
{
	int N, T, C, P, harvest;

	harvest = 0;
	scanf("%d %d %d %d", &N, &T, &C, &P);
	for (int i = 1; i * T + 1 <= N; i++)
		harvest++;
	printf("%d", harvest * C * P);
	return 0;
}