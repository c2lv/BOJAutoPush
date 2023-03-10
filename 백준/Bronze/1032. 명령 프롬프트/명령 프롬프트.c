#include <stdio.h>

int main(void)
{
	int N, same;
	char name[51][51];

	scanf("%d", &N);
	for (int i = 0; i < N; i++)
		scanf("%s", name[i]);

	for (int j = 0; j < 50; j++)
	{
		if (name[0][j] == '\0')
			break;
		same = 1;
		for (int i = 0; i < N - 1; i++)
		{
			if (name[i][j] != name[i + 1][j])
			{
				same--;
				break;
			}
		}
		if (same)
			printf("%c", name[0][j]);
		else
			printf("?");
	}
	return 0;
}