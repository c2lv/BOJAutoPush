#include <stdio.h>

int baseb2dec(char *s, int b)
{
	int sum = 0; // 0~1000000000
	int len = 0, i = 0;

	while (s[len] != '\0')
	{
		i = 0;
		while (i < b)
		{
			if (i < 10 && s[len] == '0' + i)
				break;
			if (9 < i && s[len] == 'A' + i - 10)
				break;
			i++;
		}
		sum = sum * b + i;
		len++;
	}

	return sum;
}

int main(void)
{
	char N[31];
	int B; // 2~36

	scanf("%s %d", N, &B);
	printf("%d", baseb2dec(N, B));

	return 0;
}