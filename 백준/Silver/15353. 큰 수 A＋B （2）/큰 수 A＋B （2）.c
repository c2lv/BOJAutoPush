#include <unistd.h>
#include <string.h>

int main(void)
{
    char a[10001], b[10001];
    char s[10002] = "";
    int up_n, len_a, len_b, max_len, num_a, num_b;

    scanf("%s %s", a, b);
    up_n = 0;
    len_a = strlen(a);
    len_b = strlen(b);
    max_len = len_a > len_b ? len_a : len_b;

    for (int i = 0; i < max_len; i++)
    {
        num_a = i >= len_a ? 0 : a[len_a - 1 - i] - '0';
        num_b = i >= len_b ? 0 : b[len_b - 1 - i] - '0';

        if (num_a + num_b + up_n < 10)
        {
            s[i] = num_a + num_b + up_n + '0';
            up_n = 0;
        }
        else
        {
            s[i] = num_a + num_b + up_n - 10 + '0';
            up_n = 1;
        }
    }
    if (up_n)
        s[max_len] = '1';

    for (int i = max_len; i >= 0; i--)
    {
        if (s[i] != '\0')
            printf("%c", s[i]);
    }
    
    return 0;
}