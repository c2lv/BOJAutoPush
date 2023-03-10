#include <stdio.h>

int main(void)
{
	// scanf()가 값을 제대로 받는 동안만 출력하도록
	// 조건을 넣을 수도 있다.
	int A, B;

	while (scanf("%d %d", &A, &B) == 2)
	{
		printf("%d\n", A + B);
	}
	return 0;
}