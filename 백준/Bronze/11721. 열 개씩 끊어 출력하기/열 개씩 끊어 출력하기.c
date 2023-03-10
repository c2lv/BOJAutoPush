#include <stdio.h>

int main(void)
{
	int i = 0;
	char word[101] = ""; // 배열 0으로 초기화

	scanf("%s", word);

	while (word[i])
	{
		for (int j = 0; j < 10; j++)
		{
			if (word[i + j] == 0)
				return 0;
			printf("%c", word[i + j]);
		}
		printf("\n");
		i += 10;
	}

	return 0;
}