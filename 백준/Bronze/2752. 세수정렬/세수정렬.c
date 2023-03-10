#include <stdio.h>

void swap(int *n1, int *n2)
{
    int temp;

    temp = *n1;
    *n1 = *n2;
    *n2 = temp;
}

int main(void)
{
    int n1, n2, n3;

    scanf("%d%d%d", &n1, &n2, &n3);
    if (n1 > n2 && n1 > n3)
        swap(&n1, &n3);
    else if (n2 > n1 && n2 > n3)
        swap(&n2, &n3);
    if (n1 > n2)
        swap(&n1, &n2);
    printf("%d %d %d", n1, n2, n3);
}