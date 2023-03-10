#include <stdio.h>

int fibonacci(int n, int before, int after)
{
	if (n == 0)
		return before;
	else if (n == 1)
		return after;
	else
		return fibonacci(n - 1, after, before + after);
}

int main(void)
{
	int n;

	scanf("%d", &n);

	printf("%d", fibonacci(n, 0, 1));

	return 0;
}