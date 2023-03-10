#include <stdio.h>

// a, b 중 큰 수 리턴, 같을 경우 b 리턴
int max(double a, double b)
{
	return b < a ? (int)a : (int)b;
}

int main(void)
{
    double A, B, C;

    scanf("%lf %lf %lf", &A, &B, &C);
    printf("%d", max(A * B / C, A / B * C));

	return 0;
}