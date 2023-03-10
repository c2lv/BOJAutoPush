#include <stdio.h>

void swap(char *a, char *b)
{
	char temp;

	temp = *a;
	*a = *b;
	*b = temp;
}

char *ft_strrev(char *string)
{
	int len = 0;

	while (string[len])
		len++;
	if (len == 0)
		return 0;
	for (int i = 0; i < len / 2; i++)
		swap(&string[i], &string[len - 1 - i]);

	return string;
}

int main(void)
{
	int N, M; // 0~10
	char s[11][11];

	scanf("%d%d", &N, &M);

	if (M == 0)
		return 0;
	for (int i = 0; i < N; i++)
	{
		scanf("%s", s[i]);
		printf("%s\n", ft_strrev(s[i]));
	}

	return 0;
}