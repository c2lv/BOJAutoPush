#include <stdio.h>

int main(void)
{
	int T = 0, i = 0;

	scanf("%d", &T);
	int num[T * 2];
	for (int j = T; j > 0; j--)
	{
		scanf("%d %d", &num[i], &num[i + 1]);
		i += 2;
	}
	i = 0;
	for (int k = T; k > 0; k--)
	{
		printf("%d\n", num[i] + num[i + 1]);
		i += 2;
	}
	return 0;
}