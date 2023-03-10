#include <stdio.h>

int main(void)
{
    unsigned int S;
    int i = 1;
    unsigned long long int sum = 0;

    scanf("%d", &S);
    
    while (1)
    {
        sum += i;
        if (S < sum)
            break;
        i++;
    }
    printf("%d", i - 1);

    return (0);
}