#include <stdio.h>

int main(void)
{
    int n;
    
    scanf("%d", &n);
    printf("%u", 4 * n); // 4 * n의 최댓값은 40억이므로 int로 출력해서는 안 됨.
    return 0;
}