#include <stdio.h>

int main(void)
{
	int N; // 카드의 개수 (3 ≤ N ≤ 100)
	int M; // 한도 (10 ≤ M ≤ 300,000)
	int card[100]; // 카드에 쓰여 있는 수(100,000을 넘지 않는 양의 정수)
	int sum = 0; // M을 넘지 않으면서 M에 가장 가까운 카드 3장의 합
	int temp; // 카드 3장의 합을 임시로 저장할 변수

	scanf("%d%d", &N, &M);
	for (int i = 0; i < N; i++)
		scanf("%d", &card[i]);

	for (int i = 0; i < N - 2; i++)
	{
		for (int j = i + 1; j < N - 1; j++)
		{
			for (int k = j + 1; k < N; k++)
			{
				temp = card[i] + card[j] + card[k];
				if (sum < temp && temp <= M)
					sum = temp;
			}
		}
	}
	printf("%d", sum);

	return 0;
}