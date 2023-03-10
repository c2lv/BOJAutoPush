#include <stdio.h>
#include <math.h>

int main(void)
{
	int n, flag = 0, l = 0, num[5];

	while (1)
	{
		scanf("%d", &n);
		if (!n) break;
		for (int i = 0; i < 5; i++)
		{
			if (pow(10, i) <= n && n <= pow(10, i + 1) - 1)
				l = i + 1;
		}
		for (int j = 0; j < l; j++)
		{
			num[j] = n / pow(10, l - j - 1);
			n = n % (int)pow(10, l - j - 1);
		}
		for (int k = 0; k < l / 2; k++)
		{
			if (num[k] != num[l - k - 1])
				flag++;
		}
		flag ? printf("no\n") : printf("yes\n");
		flag = 0;
	}
	return 0;
}