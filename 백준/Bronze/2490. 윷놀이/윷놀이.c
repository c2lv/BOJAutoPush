#include <stdio.h>

int main(void)
{
    int yut; // 등의 개수
    char res = 'D';

    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 4; j++)
        {
            scanf("%d", &yut);
            if (yut && res != 'A')
                res--;
            else if (yut && res == 'A')
                res = 'E';

        }
        printf("%c\n", res);
        res = 'D';
    }
    return 0;
}