#include <stdio.h>

int main(void)
{   
    int H, M, minute;

    scanf("%d %d", &H, &M);

    minute = H * 60 + M - 45;
    if (minute < 0)
        minute = 60 * 24 + minute;
    H = minute / 60;
    M = minute % 60;
    printf("%d %d", H, M);

    return 0;
}