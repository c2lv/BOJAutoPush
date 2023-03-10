#include <stdio.h>

// 알파벳이면 1, 아니면 0 리턴
int isAlpha(int c)
{
	return (('A' <= c && c <= 'Z') || ('a' <= c && c <= 'z'));
}

int main(void)
{
	char s[1000001] = ""; // 모든 항목 0으로 초기화
	int cnt = 0, i = 0;

	scanf("%[^\n]s", s);

	while (s[i] != '\0')
	{
		if (isAlpha(s[i]) && (s[i + 1] == ' ' || s[i + 1] == '\0'))
			cnt++;
		i++;
	}

	printf("%d", cnt);

	return 0;
}