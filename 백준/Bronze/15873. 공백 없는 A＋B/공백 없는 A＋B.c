#include <stdio.h>

int ft_strlen(char *s)
{
	int i = 0;

	while (s[i] != 0)
		i++;

	return i;
}

int main(void)
{
	char AB[4];
	int sum;

	scanf("%s", AB);

	if (ft_strlen(AB) == 2)
		sum = (AB[0] - '0') + (AB[1] - '0');
	else if (ft_strlen(AB) == 3)
	{
		if (AB[1] == '0')
			sum = 10 + AB[2] - '0';
		else // (AB[1] == '1')
			sum = AB[0] - '0' + 10;
	}
	else // (ft_strlen(AB) == 4)
		sum = 20;
	printf("%d", sum);

	return 0;
}