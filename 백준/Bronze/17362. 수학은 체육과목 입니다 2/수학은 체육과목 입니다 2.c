#include <stdio.h>

int main(void)
{
	int n;

	scanf("%d", &n);
	if ((n + 7) % 8 == 0)
		printf("1");
	if (n % 8 == 0 || (n + 6) % 8 == 0)
		printf("2");
	if ((n + 1) % 4 == 0)
		printf("3");
	if ((n + 4) % 8 == 0 || (n + 2) % 8 == 0)
		printf("4");
	if ((n + 3) % 8 == 0)
		printf("5");
	return 0;
}