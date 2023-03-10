#include <stdio.h>
#include <string.h>

int main(void)
{
	int T;

	scanf("%d", &T);
	for (int i = 0; i < T; i++)
	{
		char s[80];
		int count = 0, sum = 0;

		scanf("%s", s);
		for (int j = 0; j < strlen(s); j++)
		{
			if (s[j] == 'O')
			{
				count += 1;
				sum += count;
			}
			else
				count = 0;
		}
		printf("%d\n", sum);
	}
	return 0;
}