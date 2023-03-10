#include <stdio.h>

int main(void)
{
	int K; // 과자 한 개의 가격(1,000 이하의 양의 정수)
	int N; // 사려고 하는 과자의 개수(1,000 이하의 양의 정수)
	int M; // 현재 동수가 가진 돈(10만 이하의 양의 정수)
	int R; // 동수가 부모님께 받아야 하는 돈의 액수

	scanf("%d%d%d", &K, &N, &M);
	R = K * N - M;
	printf("%d", 0 < R ? R : 0);

	return 0;
}