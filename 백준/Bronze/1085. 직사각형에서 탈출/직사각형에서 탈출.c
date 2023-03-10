#include <stdio.h>

int main(void)
{
	int x, y, w, h, minimum;

	scanf("%d %d %d %d", &x, &y, &w, &h);
	int min[4] = {x, y, w - x, h - y};
	minimum = min[0];
	for (int i = 1; i <= 3; i++)
	{
		if (minimum > min[i])
			minimum = min[i];
	}
	printf("%d", minimum);
	return 0;
}