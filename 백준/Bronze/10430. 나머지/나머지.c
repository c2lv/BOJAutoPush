#include <stdio.h>

int main(void)
{
	/*
	나머지 연산자의 분배 법칙:
	각각 %를 취한 후 다시 전체적으로 %를 구한다.
	나눗셈에 대한 나머지 연산은 분배 법칙이 적용되지 않는다.
	https://goodteacher.tistory.com/133
	*/
	int A, B, C;

	scanf("%d %d %d", &A, &B, &C);
	printf("%d\n", (A + B) % C);
	printf("%d\n", ((A % C) + (B % C)) % C);
	printf("%d\n", (A * B) % C);
	printf("%d", ((A % C) * (B % C)) % C);
	return 0;
}