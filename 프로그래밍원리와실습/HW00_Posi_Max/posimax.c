#include <stdio.h>

int main(void)
{
	int c, i, num, M;
	M = -10000;
	scanf("%d", &c);
	for (i = 0; i < c; i++)
	{
		scanf("%d", &num);
		if (num > M)
			M = num;
	}
	if (M <= 0)
	{
		printf("None");
		return 0;
	}
	printf("%d", M);
	return 0;
}