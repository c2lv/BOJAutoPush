#include <stdio.h>

int main(void)
{
    int score[5], sum = 0;

    scanf("%d %d %d %d %d", &score[0], &score[1], &score[2], &score[3], &score[4]);
    for (int i = 0; i < 5; i++)
    {
        if (score[i] < 40)
            score[i] = 40;
        sum += score[i];
    }
    printf("%d", sum / 5);
    return 0;
}