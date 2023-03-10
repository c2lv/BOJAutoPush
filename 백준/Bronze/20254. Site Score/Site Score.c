#include <stdio.h>

int main(void)
{
    short UR, TR, UO, TO;

    scanf("%hd%hd%hd%hd", &UR, &TR, &UO, &TO);
    printf("%hd", 56*UR+24*TR+14*UO+6*TO);

    return 0;
}