#include <stdio.h>

int main(void)
{
	int result;

    scanf("%d", &result);

	switch (result)
    {
	    case 60 ... 69:
            printf("D");
            break;
	    case 70 ... 79:
            printf("C");
            break;
	    case 80 ... 89:
            printf("B");
            break;
	    case 90 ... 100:
            printf("A");
            break;
    	default:
            printf("F");
            break;
	}

    return 0;
}