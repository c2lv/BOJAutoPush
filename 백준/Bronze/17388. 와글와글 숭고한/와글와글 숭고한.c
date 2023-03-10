#include <stdio.h>

int main(void)
{
	int S, K, H;

	scanf("%d %d %d", &S, &K, &H);
	if (100 <= S + K + H)
		printf("OK");
	else if (S < K && S < H)
		printf("Soongsil");
	else if (K < S && K < H)
		printf("Korea");
	else // if (H < S && H < K)
		printf("Hanyang");
	return 0;
}