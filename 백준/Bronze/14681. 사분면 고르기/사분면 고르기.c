#include <stdio.h>

int main(void)
{   
    short x, y, q;
    
    scanf("%hd%hd", &x, &y);
    if (x > 0 && y > 0)
        q = 1;
    else if (x < 0 && y > 0)
        q = 2;
    else if (x < 0 && y < 0)
        q = 3;
    else // (x > 0 && y < 0)
        q = 4;
    printf("%hd", q);
    
    return 0;
}