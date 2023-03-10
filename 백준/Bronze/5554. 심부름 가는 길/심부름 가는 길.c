#include <stdio.h>

int main(void)
{
	int htos, stop, ptoa, atoh, sum, x, y;
	
	scanf("%d", &htos);
	scanf("%d", &stop);
	scanf("%d", &ptoa);
	scanf("%d", &atoh);
	sum = htos + stop + ptoa + atoh;
	x = sum / 60;
	y = sum % 60;
	printf("%d\n%d", x, y);
	return 0;
}