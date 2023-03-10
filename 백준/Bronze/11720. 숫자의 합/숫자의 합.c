#include <stdio.h>

int main(void)
{
	// 여기서 숫자는 10개의 숫자를 의미
	// (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
	// 둘째 줄은 최대 100자리가 주어지므로 문자열로 받는다.

	int N;
	char M[101];

	int sum = 0;
	scanf("%d", &N);
	scanf("%s", M);
	for (int i = N; i > 0; i--)
	{
		M[i - 1] -= '0'; // 문자를 숫자로 변환
		sum += M[i - 1];
	}
	printf("%d\n", sum);
}