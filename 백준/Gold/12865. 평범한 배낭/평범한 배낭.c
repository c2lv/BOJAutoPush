#include <stdio.h>

int max(int n1, int n2)
{
	return n2 < n1 ? n1 : n2;
}

int main(void)
{
	static int DP[101][100001]; // DP[i][j]: 0 ~ i번째 물건을 최대 j만큼의 무게만을 넣을 수 있는 배낭에 넣을 때 넣을 수 있는 물건들의 가치합의 최댓값(같은 번째 물건은 하나만 넣을 수 있음)
	int N; // 물품의 수(1 ≤ N ≤ 100)
	int K; // 준서가 버틸 수 있는 무게(1 ≤ K ≤ 100,000)
	int W[101]; // W[i]: i번째 물건의 무게(1 ≤ W[i] ≤ 100,000)
	int V[101]; // V[i]: i번째 물건의 가치(0 ≤ V[i] ≤ 1,000)

	scanf("%d%d", &N, &K);
	for (int i = 1; i <= N; i++)
		scanf("%d%d", &W[i], &V[i]);

	for (int i = 0; i <= N; i++)
	{
		for (int j = 0; j <= K; j++)
		{
			if (i == 0 || j == 0) // 0번째 물건은 없음 / 물건의 무게는 최소 1이므로 최대 0만큼의 무게만을 넣을 수 있는 배낭에는 아무것도 넣을 수 없음
				DP[i][j] = 0;
			else if (j < W[i]) // 배낭의 무게 한도보다 i번째 물건이 더 무거운 경우 해당 믈건은 담을 수 없음
				DP[i][j] = DP[i - 1][j];
			else // W[i] <= j
				DP[i][j] = max(DP[i - 1][j], DP[i - 1][j - W[i]] + V[i]);
		}
	}
	printf("%d", DP[N][K]);

	return 0;
}