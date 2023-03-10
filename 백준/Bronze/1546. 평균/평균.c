#include <stdio.h>

int main(void)
{
	int N, j = 0;
	double s[1000] = { 0 }, sum = 0, M = 0;

	scanf("%d", &N);
	for (int i = 0; i < N; i++)
		scanf("%lf", &s[i]);

	while (j < N)
	{
		if (M < s[j])
			M = s[j];
		j++;
	}
	j = 0;
	while (j < N)
	{
		s[j] = s[j] / M * 100;
		sum += s[j];
		j++;
	}

	printf("%lf", sum / (double)N);

	return 0;
}