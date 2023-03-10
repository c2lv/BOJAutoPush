#include <stdio.h>

void swap(int *a, int *b)
{
	int temp;

	temp = *a;
	*a = *b;
	*b = temp;
}

int main(void)
{
	int A, B, C;
	char s[4];

	scanf("%d%d%d", &A, &B, &C);
	scanf("%s", s);

	if (A > B && A > C)
		swap(&A, &C);
	else if (B > A && B > C)
		swap(&B, &C);

	if (A > B)
		swap(&A, &B);

	for (int i = 0; i < 3; i++)
	{
		if (s[i] == 'A')
			printf("%d ", A);
		else if (s[i] == 'B')
			printf("%d ", B);
		else // (s[i] == 'C')
			printf("%d ", C);
	}

	return 0;
}