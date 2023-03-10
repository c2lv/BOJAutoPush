#include <stdio.h>

int main(void)
{
	int i = 0;
	char s[101];

	scanf("%s", s);
	while (s[i])
	{
		if ('a' <= s[i] && s[i] <= 'z')
			s[i] -= 32;
		else // ('A' <= s[i] && s[i] <= 'Z')
			s[i] += 32;
		i++;
	}
	printf("%s", s);

	return 0;
}