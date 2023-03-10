#include <stdio.h>

int main(void)
{
	// 2nd - 3rd = 1st - 2nd
	// 1st = 2 * 2nd - 3rd

	int first, second, third;

	scanf("%d", &third);
	scanf("%d", &second);
	first = 2 * second - third;
	printf("%d", first);
	return 0;
}