#include <stdio.h>

int main(void)
{
	while (1)
	{
		int n, k, sum, stamp;

		if (scanf("%d%d", &n, &k) == EOF)
			break;
		sum = n;
		stamp = n;
		while (stamp / k)
		{
			sum += stamp / k;
			stamp = stamp / k + stamp % k;
		}

		printf("%d\n", sum);
	}

	return 0;
}