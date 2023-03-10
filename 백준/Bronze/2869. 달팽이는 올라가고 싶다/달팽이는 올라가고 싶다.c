#include <stdio.h>

int main(void)
{
	int A, B, V;

	scanf("%d%d%d", &A, &B, &V);

	printf("%d", (V - B) % (A - B) != 0 ? (V - B) / (A - B) + 1 : (V - B) / (A - B));

	return 0;
}