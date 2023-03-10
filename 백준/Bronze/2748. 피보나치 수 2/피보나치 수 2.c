#include <stdio.h>

typedef unsigned long long ull;

ull fibonacci(ull n, ull before, ull after)
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
	ull n;

	scanf("%llu", &n);

	printf("%llu", fibonacci(n, 0, 1));

	return 0;
}