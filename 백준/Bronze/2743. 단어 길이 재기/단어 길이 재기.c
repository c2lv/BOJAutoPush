#include <stdio.h>

int ft_strlen(char *string)
{
	int len = 0;

	while (string[len] != '\0')
		len++;

	return len;
}

int main(void)
{
	char str[101];

	scanf("%s", str);
	printf("%d", ft_strlen(str));

	return 0;
}