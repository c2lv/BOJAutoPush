#include <stdio.h>

// 매개변수 둘 중 작은 값을 리턴하는 함수
int min(int n1, int n2)
{
	return n1 < n2 ? n1 : n2;
}

int main(void)
{
	int N; // 집의 수(2 ≤ N ≤ 1,000)
	int R, G, B; // 빨강, 초록, 파랑으로 칠하는 비용
	int before[3]; // before[n]: 처음부터 직전까지의 집을 n(0: 빨강, 1: 초록, 2: 파랑)으로 칠하기까지 든 비용의 최솟값
	int now[3] = { 0, }; // now[n]: 처음부터 지금까지의 집을 n(0: 빨강, 1: 초록, 2: 파랑)으로 칠하기까지 든 비용의 최솟값

	scanf("%d", &N);
	for (int i = 0; i < N; i++)
	{
		scanf("%d%d%d", &R, &G, &B);

		for (int j = 0; j < 3; j++)
			before[j] = now[j];
		now[0] = min(before[1], before[2]) + R;
		now[1] = min(before[0], before[2]) + G;
		now[2] = min(before[0], before[1]) + B;
	}
	printf("%d", min(min(now[0], now[1]), now[2]));

	return 0;
}