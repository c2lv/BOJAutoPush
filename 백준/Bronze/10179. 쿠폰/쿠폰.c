#include <stdio.h>

int main(void)
{   
    int T;
    double d;
    
    scanf("%d", &T);
    for (int i = 0; i < T; i++)
    {
        scanf("%lf", &d);
        printf("$%.2lf\n", d * 0.8);
    }
    
    return 0;
}