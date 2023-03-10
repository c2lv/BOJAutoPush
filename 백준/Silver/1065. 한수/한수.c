#include <stdio.h>

int ft_strlen(char *s)
{
	int len = 0;

	while (s[len] != 0)
		len++;
	
	return len;
}

// int 자료형 범위 내 양의 정수만 가능
int ft_atoi(char *s)
{
	int sum = 0;

	for (int i = 0; i < ft_strlen(s); i++)
	{
		sum *= 10;
		sum += s[i] - '0';
	}

	return sum;
}

int main(void)
{
	char X[5];
	int n, len, sum = 0;

	scanf("%s", X);

	n = ft_atoi(X);
	len = ft_strlen(X);
	if (len < 3)
		sum = n;
	else if (len == 3)
	{
		sum = 99;
		for (int i = n; 99 < i; i--)
		{
			if (X[0] - X[1] == X[1] - X[2])
				sum++;
			X[2]--;
			for (int j = 2; 0 < j; j--)
			{
				if (X[j] == '0' - 1)
				{
					X[j - 1]--;
					X[j] = '9';
				}
			}
		}
	}
	else
		sum = 144;
	printf("%d", sum);

	return 0;
}

/*
** 	1 ~ 99: 모두 한수
** 	100 ~ 1000:
** 	111, 123, 135, 147, 159
** 	210, 222, 234, 246, 258
** 	...
** 	951, 963, 975, 987, 999
*/