#include <stdio.h>
#define _USE_MATH_DEFINES
#include <math.h>

int main(void)
{
    int R;

    scanf("%d", &R);

    printf("%.6lf\n", (double)(M_PI * R * R));
    printf("%.6lf", (double)(2 * R * R));

    return 0;
}