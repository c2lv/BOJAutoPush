#include <stdio.h>

// n의 길이 반환 함수
int numlen(int n)
{
	int len = 1;

	while (9 < n)
	{
		n /= 10;
		len++;
	}

	return len;
}

// n을 문자열 s로 변환하는 함수
void ft_itoa(int n, char *s)
{
	int len = numlen(n), pot = 1, sum = 0;

	for (int i = 1; i < len; i++)
		pot *= 10;
	for (int i = 0; i < len; i++)
	{
		if (i == 0)
			s[i] = n / pot + '0';
		else
			s[i] = n / pot - sum * 10 + '0';
		sum *= 10;
		sum += s[i] - '0';
		pot /= 10;
	}
}

// n과 n의 각 자리수를 더한 값을 반환하는 함수
int d(int n)
{
	int sum = 0;
	char s[11];

	ft_itoa(n, s);
	sum += n;
	for (int i = 0; i < numlen(n); i++)
		sum += s[i] - '0';

	return sum;
}

int main(void)
{
	int self_number[10035], sn;

	for (int i = 1; i < 10000; i++)
		self_number[i] = i;
	for (int i = 1; i < 10000; i++)
	{
		sn = d(i);
		self_number[sn] = 0;
	}
	for (int i = 1; i < 10000; i++)
	{
		if (self_number[i] != 0)
			printf("%d\n", self_number[i]);
	}

	return 0;
}