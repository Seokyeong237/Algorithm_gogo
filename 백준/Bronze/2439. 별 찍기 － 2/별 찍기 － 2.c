#include <stdio.h>

int main(void)
{
	int N;

	scanf("%d", &N);

	for (int j = 1; j <= N; j++)
	{
		for (int i = 1; i <= N - j; i++)
			printf(" ");
		for (int k = 1; k <= j; k++)
			printf("*");
		printf("\n");
	}

	return 0;
}