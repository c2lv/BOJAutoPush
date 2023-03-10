#include <stdio.h>

typedef long long int ull;

/*
n번째 피보나치 수를 백만으로 나눈 나머지가 0,
n + 1번째 피보나치 수를 백만으로 나눈 나머지가 1,
n + 2번째 피보나치 수를 백만으로 나눈 나머지가 1임을 만족하는
모든 n을 모두 출력하는 함수.
(n은 1000000000000000000보다 작거나 같은 자연수이다.)
해당 함수를 호출하면 1500000의 배수가 출력된다.
따라서, 1500000 간격으로 값이 반복된다고 볼 수 있다.
*/
void test()
{
	ull a = 0;
	ull b = 1;
	ull c = 1;

	for (ull i = 2; i <= 1000000000000000000; i++)
	{
		if (i != 2 && a == 0 && b == 1 && c == 1)
			printf("%llu\n", i - 2);
		c = a + b < 1000000 ? a + b : a + b - 1000000;
		a = b;
		b = c;
	}
}

int fibo_MOD_million(ull n, int before, int after)
{
	if (n == 0)
		return before;
	else if (n == 1)
		return after;
	else
		return fibo_MOD_million(n - 1, after, before + after < 1000000 ? before + after : before + after - 1000000);
}

int main(void)
{
	ull n;

	scanf("%llu", &n);

	printf("%d", fibo_MOD_million(n % 1500000, 0, 1));

	return 0;
}