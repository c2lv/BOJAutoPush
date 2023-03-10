#include <stdio.h>

int main()
{
	int N; // 1 ≤ N ≤ 11,172
	char hangul[3]; // 한글 유니코드(UCS) 0xAC00(가) ~ 0xD7A3(힣) 11172자를 UTF-8 인코딩으로 변환

	scanf("%d", &N);
	hangul[0] = (N + 3071) / 4096 - 22;
	hangul[1] = ((N + 3071) / 64) % 64 - 128;
	hangul[2] = (N - 1) % 64 - 128;
	printf("%c%c%c\n", hangul[0], hangul[1], hangul[2]);

	return 0;
}