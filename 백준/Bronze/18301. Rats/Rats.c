#include <stdio.h>

int main(void)
{
    int n1, n2, n12, N;
    
    scanf("%d %d %d", &n1, &n2, &n12);
    N = (n1 + 1) * (n2 + 1) / (n12 + 1) - 1;
    printf("%d", N);
    return 0;
}