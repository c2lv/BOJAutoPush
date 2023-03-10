#include <stdio.h>

int main(void)
{
	char id[51];
	char surprise[4] = "??!";

	scanf("%s", &id);
	printf("%s%s", id, surprise);
	return 0;
}