#include <stdio.h>

int main(void)
{   
    short a1, a2, a3, b1, b2, a, b;
    
    scanf("%hd%hd%hd%hd%hd", &a1, &a2, &a3, &b1, &b2);
    if (a1 <= a2 && a1 <= a3)
        a = a1;
    else if (a2 <= a1 && a2 <= a3)
        a = a2;
    else // (a3 <= a1 && a3 <= a2)
        a = a3;
    if (b1 < b2)
        b = b1;
    else // (b1 >= b2)
        b = b2;
    printf("%hd", a + b - 50);
    
    return 0;
}