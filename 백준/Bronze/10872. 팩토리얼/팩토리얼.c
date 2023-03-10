#include <stdio.h>

int fact(int n)
{
    int a = 1;

    while (n)
    {
        a *= n;
        n--;
    }
    
    return (a);
}

int main(void)
{
    int N;

    scanf("%d", &N);
    printf("%d", fact(N));

    return 0;
}