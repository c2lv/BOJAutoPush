#include <stdio.h>

// 두 문자열이 같으면 1, 아니면 0을 리턴하는 함수
int equal(char *a, char *b)
{
	int i = 0;

	while (a[i] != '\0' || b[i] != '\0')
	{
		if (a[i] != b[i])
			return 0;
		i++;
	}
	if (a[i] == b[i])
		return 1;
	else
		return 0;
}

int main(void)
{
	char res[11][7] = {
		"black",
		"brown",
		"red",
		"orange",
		"yellow",
		"green",
		"blue",
		"violet",
		"grey",
		"white"
	};
	long long val = 0;

	for (int i = 0; i < 3; i++)
	{
		char input[7];
		scanf("%s", input);

		for (int j = 0; j < 10; j++)
		{
			if (equal(input, res[j]))
			{
				if (i < 2)
				{
					val *= 10;
					val += j;
				}
				else // (i == 2)
				{
					for (int k = 0; k < j; k++)
						val *= 10;
				}
				break;
			}
		}
	}
	printf("%lld", val);

	return 0;
}