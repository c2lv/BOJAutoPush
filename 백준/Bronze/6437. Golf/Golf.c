#include <stdio.h>

int main(void)
{
	int p; // 0, 3, 4, 5
	int s; // 1 <= s < 20
	int i = 1;

	while (1)
	{
		scanf("%d%d", &p, &s);

		if (p == 0)
			break;
		printf("Hole #%d\n", i);
		if (s == 1)
			printf("Hole-in-one.\n\n");
		else if (s == p - 3)
			printf("Double eagle.\n\n");
		else if (s == p - 2)
			printf("Eagle.\n\n");
		else if (s == p - 1)
			printf("Birdie.\n\n");
		else if (s == p)
			printf("Par.\n\n");
		else if (s == p + 1)
			printf("Bogey.\n\n");
		else // (s == p + 2)
			printf("Double Bogey.\n\n");
		i++;
	}

	return 0;
}