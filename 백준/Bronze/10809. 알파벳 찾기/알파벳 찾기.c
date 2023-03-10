#include <stdio.h>

int main(void)
{
    char S[100];
    int alpha[26], j = 0;

    scanf("%s", S);
    for (int i = 0; i < 26; i++)
        alpha[i] = -1;
    while (S[j] != '\0')
    {
        if (alpha[S[j] - 'a'] == -1)
            alpha[S[j] - 'a'] = j;
        j++;
    }
    for (int k = 0; k < 26; k++)
        printf("%d ", alpha[k]);
    return 0;
}