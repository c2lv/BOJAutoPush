#include <stdio.h>

int honeycomb(int N)
{
	int i = 1;
	int a = 0, b = 1;

	if (N == 1)
		return i;
	else
	{
		i++;
		while (1)
		{
			if (6 * a + 2 <= N && N <= 6 * b + 1)
				return i;
			else
			{
				a = b;
				b += i;
				i++;
			}
		}
	}
}

int main(void)
{
	int N;

	scanf("%d", &N);

	printf("%d", honeycomb(N));

	return 0;
}