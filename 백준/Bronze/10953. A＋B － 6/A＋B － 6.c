#include <stdio.h>

int main(void)
{   
    int T, n;
    char s[4]; // null 문자 포함
    
    scanf("%d", &T);
    for (int i = 0; i < T; i++)
    {
        scanf("%s", s);
        n = s[0] + s[2] - '0' * 2;
        printf("%d\n", n);
    }
    
    return 0;
}