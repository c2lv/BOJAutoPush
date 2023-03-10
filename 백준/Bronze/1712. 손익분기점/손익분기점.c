#include <stdio.h>

int main(void)
{
	int A, B, C; // 고정 비용, 가변 비용, 노트북 가격(21억 이하의 자연수)

	scanf("%d%d%d", &A, &B, &C);
	if (!(B < C)) // 한 대당 판매 수입(C - B)이 양수가 아니면 손익분기점이 존재하지 않음
	{
		printf("%d", -1);
		return 0;
	}
	printf("%d", A / (C - B) + 1);
	return 0;
}