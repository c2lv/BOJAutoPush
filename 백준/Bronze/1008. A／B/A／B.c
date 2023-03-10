#include <stdio.h>

int main() {
	// 실수형 double은 메모리 크기 8 byte, 
	// 표현 가능한 소수점 이하 자리수가 소수점 이하 15자리이다.
	// 소수점 이하 10자리에서 반올림한 값을 출력하도록 하여(.9)
	// 실제 정답과 출력값의 오차 범위를 10^-9로 맞췄다.
	double A, B;

	scanf("%lf %lf", &A, &B);
	printf("%.9lf", A/B);
	return 0;
}