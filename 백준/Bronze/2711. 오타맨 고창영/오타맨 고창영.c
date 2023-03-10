#include <stdio.h>

int main(void)
{
	int T;

	scanf("%d", &T);
	for (int i = 0; i < T; i++)
	{
		int wrong, i = 0;
		char str[81];

		scanf("%d%s", &wrong, str);
		
		while (str[i])
		{
			if (i != wrong - 1)
				printf("%c", str[i]);
			i++;
		}
		printf("\n");
	}

	return 0;
}