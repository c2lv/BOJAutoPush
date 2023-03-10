#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
#include <math.h>

int	main(void)
{
	char hex[7]; // 입력받은 16진수 저장할 문자열
	int dec = 0; // 16진수를 10진수로 변환한 값
	int pos = 0; // 지수

	scanf("%s", &hex);
	for (int i = strlen(hex) - 1; i >= 0; i--)
	{
		char ch = hex[i];

		if ('0' <= ch && ch <= '9')
			dec += (ch - '0') * pow(16, pos);
		else if ('A' <= ch && ch <= 'F')
			dec += (10 + ch - 'A') * pow(16, pos);
		pos++;
	}
	printf("%d", dec);
	return (0);
}