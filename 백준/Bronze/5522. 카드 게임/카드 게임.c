#include <stdio.h>

int main (void) {
	int num1, num2, num3, num4, num5;
	int sum = 0;

	scanf("%d\n", &num1);
	scanf("%d\n", &num2);
	scanf("%d\n", &num3);
	scanf("%d\n", &num4);
	scanf("%d", &num5);

	sum = num1 + num2 + num3 + num4 + num5;

	printf("%d", sum);

}