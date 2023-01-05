#include <stdio.h>

int main(void)
{
	int H, M;

	scanf("%d %d", &H, &M);

	if ((M < 60) && (M >= 45) && (H >= 0))
		M = M - 45;
	else if ((M < 45) && (M >= 0))
	{
		if (H == 0)
			H = 23;
		else if (H > 0)
			H = H - 1;

		M = M + 60 - 45;	
	}
	printf("%d %d\n", H, M);
	return 0;
}