#include <stdio.h>

int fibo(int n, int before, int now)
{
	if (n == 0)
		return before;
	else if (n == 1)
		return now;
	else
		return fibo(n - 1, now, before + now);
}

int main(void)
{
	int n;

	scanf("%d", &n);

	printf("%d", fibo(n, 0, 1));

	return 0;
}