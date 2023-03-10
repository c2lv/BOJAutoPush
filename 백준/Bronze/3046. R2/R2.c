#include <stdio.h>

int main(void)
{
	// S = (R1 + R2) / 2
	// R2 = 2 * S - R1
	int R1, S;

	scanf("%d %d", &R1, &S);
	printf("%d", 2 * S - R1);
	return 0;
}