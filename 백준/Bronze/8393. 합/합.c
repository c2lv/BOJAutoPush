#include <stdio.h>

int main(void)
{
	int n, sum;

	sum = 0; // 초기화 해줘야 함
	scanf("%d", &n);
	for (int i = n; i > 0; i--)
		sum += i;
	printf("%d", sum);
	return 0;
}