#include <stdio.h>

int main(void)
{
	int N, M;

	scanf("%d %d", &N, &M);
	if (M == 1 || M == 2)
		printf("NEWBIE!");
	else if (3 <= M  && M <= N)
		printf("OLDBIE!");
	else if (N < M)
		printf("TLE!");
	return 0;
}