#include <stdio.h>

int main(void)
{
	int in1, in2;
	int ou1, ou2, ou3, result;

	scanf("%d", &in1);
	scanf("%d", &in2);
	ou1 = in1 * ((in2 % 100) % 10);
	ou2 = in1 * ((in2 % 100) / 10);
	ou3 = in1 * (in2 / 100);
	
	result = in1 * in2;

	printf("%d\n", ou1);
	printf("%d\n", ou2);
	printf("%d\n", ou3);
	printf("%d\n", result);
	
	return 0;
}