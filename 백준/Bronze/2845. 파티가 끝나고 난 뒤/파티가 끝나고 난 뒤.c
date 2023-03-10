#include <stdio.h>

int main(void)
{
	int L, P, N1, N2, N3, N4, N5;

	scanf("%d %d", &L, &P);
	scanf("%d %d %d %d %d", &N1, &N2, &N3, &N4, &N5);
	printf("%d %d %d %d %d", N1 - L*P, N2 - L*P, N3 - L*P, N4 - L*P, N5 - L*P);
}