#include <stdio.h>

// 두 문자열이 같으면 1, 같지 않으면 0 리턴
int equal(char *a, char *b)
{
	int i = 0;

	while (a[i] == b[i])
	{
		if (a[i] == '\0')
			return 1;
		i++;
	}
	return 0;
}

int main(void)
{
	int T;
	double exchange[4] = { 2.2046, 0.4536, 0.2642, 3.7854 };
	char unit[5][3] = { "kg", "lb", "l", "g" };

	scanf("%d", &T);
	for (int i = 0; i < T; i++)
	{
		double num;
		char input[3];

		scanf("%lf %s", &num, input);
		for (int j = 0; j < 4; j++)
		{
			int n;

			if (equal(input, unit[j]))
			{
				n = j % 2 == 0 ? 1 : -1;
				printf("%.4lf %s\n", num * exchange[j], unit[j + n]);
			}
		}
	}

	return 0;
}