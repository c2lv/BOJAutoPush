#include <stdio.h>

int main(void)
{   
    int a1, a2, a3;

    scanf("%d%d%d", &a1, &a2, &a3);

    if (a1 + a2 + a3 == 180)
    {
        if (a1 == 60 && a2 == 60) // a3 == 60
            printf("Equilateral");
        else if (a1 == a2 || a1 == a3 || a2 == a3)
            printf("Isosceles");
        else
            printf("Scalene");
    }
    else // (a1 + a2 + a3 != 180)
        printf("Error");

    return 0;
}