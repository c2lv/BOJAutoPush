#include <stdio.h>

int main(void)
{
	int A, B, C, mid;

	scanf("%d%d%d", &A, &B, &C);

	if (B <= A && C <= A)
	{
		if (C <= B)
			mid = B;
		else
			mid = C;
	}
	else if (A <= B && C <= B)
	{
		if (A <= C)
			mid = C;
		else
			mid = A;
	}
	else // (A <= C && B <= C)
	{
		if (A <= B)
			mid = B;
		else
			mid = A;
	}
	printf("%d", mid);

	return 0;
}