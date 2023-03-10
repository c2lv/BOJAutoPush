#include <stdio.h>

int main(void)
{
	int side[3];

	while (1)
	{
		scanf("%d %d %d", &side[0], &side[1], &side[2]);
		if (side[0] == side[1] && side[1] == side[2] && side[2] == 0)
			break;
		for (int i = 0; i < 3; i++)
			side[i] *= side[i];
		(side[0] == side[1] + side[2] || side[1] == side[2] + side[0] || side[2] == side[0] + side[1]) ? printf("right\n") : printf("wrong\n");
	}
	return 0;
}