#include <stdio.h>

int main(void)
{   
    int s1[4], s2[4], S = 0, T = 0;

    for (int i = 0; i < 4; i++)
    {
        scanf("%d", &s1[i]);
        S += s1[i];
    }
    for (int j = 0; j < 4; j++)
    {
        scanf("%d", &s2[j]);
        T += s2[j];
    }
    if (S < T)
        printf("%d", T);
    else // (T <= S)
        printf("%d", S);

    return 0;
}