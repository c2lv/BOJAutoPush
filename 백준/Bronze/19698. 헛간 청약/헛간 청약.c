#include <stdio.h>

int main(void)
{
    int N, W, H, L, width = 0, height = 0, max;

    scanf("%d %d %d %d", &N, &W, &H, &L);
    while (W >= width * L)
        width++;
    while (H >= height * L)
        height++;
    max = (width - 1) * (height - 1);
    if (max > N)
        max = N;
    printf("%d", max);
    return 0;
}