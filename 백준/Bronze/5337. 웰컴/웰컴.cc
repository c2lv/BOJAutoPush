#include <unistd.h>

int main(void)
{
	write(1, ".  .   .\n", 9);
	write(1, "|  | _ | _. _ ._ _  _\n", 22);
	write(1, "|/\\|(/.|(_.(_)[ | )(/.", 22);
	return 0;
}