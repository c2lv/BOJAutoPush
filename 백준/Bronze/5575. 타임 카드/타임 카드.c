#include <stdio.h>

int main(void)
{   
    int a[18], b;
    
    for (int i = 0; i < 18; i++)
        scanf("%d", &a[i]);
    for (int j = 0; j < 3; j++)
    {
        b = (a[6*j+3]*3600 + a[6*j+4]*60 + a[6*j+5]) - (a[6*j]*3600 + a[6*j+1]*60 + a[6*j+2]);
        a[3*j] = b/3600;
        a[3*j+1] = b%3600/60;
        a[3*j+2] = b%60;
    }
    for (int k = 0; k < 3; k++)
        printf("%d %d %d\n", a[3*k], a[3*k+1], a[3*k+2]);
    
    return 0;
}