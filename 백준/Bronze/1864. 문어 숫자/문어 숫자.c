#include <stdio.h>

int main(void)
{
    char octo_num[10] = "/-\\(@?>&%"; // -1 ~ 8
    
    while (1)
    {
		char s[9] = "\0\0\0\0\0\0\0\0\0";
        scanf("%s", s);
        if (s[0] != '#')
        {
            int result = 0;
            
            for (int i = 0; i < 8; i++)
            {
                for (int j = 0; j < 10; j++)
                {
                    if (s[i] == octo_num[j] && s[i] != '\0')
                    {
                        result *= 8;
                        result += j;
                        result -= 1;
                        // printf("%d\n", result);
                    }
                }
            }
            printf("%d\n", result);
        }
        else
            break;
    }
    return 0;
}