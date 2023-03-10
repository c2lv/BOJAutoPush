#include <stdio.h>

int main(void)
{
	char word[1000001] = "", maxalpha = '?';
	int i = 0, alpha[26] = { 0 }, max = 0;

	scanf("%s", word);

	while (word[i])
	{
		for (int j = 0; j < 26; j++)
		{
			if (word[i] == 'a' + j || word[i] == 'A' + j)
			{
				alpha[j]++;
				break;
			}
		}
		i++;
	}
	for (i = 0; i < 26; i++)
	{
		if (max < alpha[i])
		{
			max = alpha[i];
			maxalpha = 'A' + i;
		}
	}
	for (i = 0; i < 26; i++)
	{
		if (max == alpha[i] && maxalpha != 'A' + i)
		{
			maxalpha = '?';
			break;
		}
	}
	printf("%c", maxalpha);

	return 0;
}