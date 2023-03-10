#include <stdio.h>

// X의 길이를 구하는 함수
int Len(int X)
{
	int Res = 1;

	while (9 < X)
	{
		X /= 10;
		Res++;
	}

	return Res;
}

// X의 모든 자리수를 역순으로 만드는 함수
int Rev(int X)
{
	int L = Len(X);
	int Pot = 10;
	int Res = 0;

	for (int i = 0; i < L; i++)
	{
		Res *= 10;
		Res += X % Pot;
		X /= Pot;
	}
	return Res;
}

int main(void)
{
	int X, Y;

	scanf("%d%d", &X, &Y);
	printf("%d", Rev(Rev(X) + Rev(Y)));

	return 0;
}