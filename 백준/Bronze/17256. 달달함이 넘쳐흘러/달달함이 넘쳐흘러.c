#include <stdio.h>

struct cake_number
{
	int x, y, z;
};


int main(void)
{
	struct cake_number a, b, c;

	scanf("%d %d %d", &a.x, &a.y, &a.z);
	scanf("%d %d %d", &c.x, &c.y, &c.z);
	// (a.z + b.x, a.y × b.y, a.x + b.z) = (c.x, c.y, c.z)
	// (b.x, b.y, b.z) = (c.x - a.z, c.y / a.y, c.z - a.x)
	b.x = c.x - a.z;
	b.y = c.y / a.y;
	b.z = c.z - a.x;
	printf("%d %d %d", b.x, b.y, b.z);
	
	return 0;
}