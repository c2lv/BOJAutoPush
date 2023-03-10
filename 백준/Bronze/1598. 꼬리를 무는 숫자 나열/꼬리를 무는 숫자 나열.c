#include <stdio.h>

/*  x   0 1  2  3  4  5
**  y -----------------
**  0 | 1 5  9 13 17 21 ...
**  1 | 2 6 10 14 18 22 ...
**  2 | 3 7 11 15 19 23 ...
**  3 | 4 8 12 16 20 24 ...
*/

// n의 절댓값을 리턴하는 함수
int abs(int n)
{
	return 0 < n ? n : -n;
}

int main(void)
{
	int n1, n2, x1, x2, y1, y2;

	scanf("%d%d", &n1, &n2);

	x1 = (n1 - 1) / 4;
	y1 = (n1 - 1) % 4;
	x2 = (n2 - 1) / 4;
	y2 = (n2 - 1) % 4;
	printf("%d", abs(x2 - x1) + abs(y2 - y1));

	return 0;
}