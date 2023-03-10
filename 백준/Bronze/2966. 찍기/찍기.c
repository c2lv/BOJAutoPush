#include <stdio.h>

// 인자 중 가장 큰 값을 리턴
int ft_max(int a, int b, int c)
{
	if (b <= a && c <= a)
		return a;
	else if (a <= b && c <= b)
		return b;
	else
		return c;
}

int main(void)
{
	int N, i = 0, sum[3] = { 0, }, max = 0;
	char ans[101], guess[4][7] = { "ABC", "BABC", "CCAABB" }, id[4][7] = { "Adrian", "Bruno", "Goran" };

	scanf("%d%s", &N, ans);

	while (i < N)
	{
		if (ans[i] == guess[0][i % 3])
			sum[0]++;
		if (ans[i] == guess[1][i % 4])
			sum[1]++;
		if (ans[i] == guess[2][i % 6])
			sum[2]++;
		i++;
	}
	max = ft_max(sum[0], sum[1], sum[2]);
	printf("%d\n", max);
	i = 0;
	while (i < 3)
	{
		if (sum[i] == max)
			printf("%s\n", id[i]);
		i++;
	}

	return 0;
}