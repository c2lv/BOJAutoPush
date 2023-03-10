#include <stdio.h>

int main()
{
    short N; // 1 ≤ N ≤ 11,172
	char hangul[3] = {-22, -80, -128}; // 한글 유니코드(UCS) 0xAC00(가) ~ 0xD7A3(힣) 11172자를 UTF-8 인코딩으로 변환 / 초깃값은 "가"
	char input[3]; // 한글 유니코드(UCS) 0xAC00(가) ~ 0xD7A3(힣) 11172자를 UTF-8 인코딩으로 변환 / 초깃값은 "가"

	scanf("%c%c%c", &input[0], &input[1], &input[2]);
    N = 4096 * (input[0] - hangul[0]) + 64 * (input[1] - hangul[1]) + (input[2] - hangul[2]) + 1;
    printf("%hd", N);

	return 0;
}