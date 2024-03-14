#include <stdio.h>

int main(void) {

    int n;

    scanf("%d", &n);

    while (n > 1) {

        int i = 2;

        while (1) {

            if (n % i == 0) {

                printf("%i\n", i);

                n /= i;

                break;

            }

            i++;

        }

    }

    return 0;

}