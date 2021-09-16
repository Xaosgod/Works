#include <iostream>
#include <math.h>
int main()
{
	double x, y,k,l;

	double c[100] = { 0 };

	for (int j = 0; j < 100; j++)
	{
		k = 0;
		l = 0;

		for (int i = 0; i < 1000; i++)
		{

			std::cin >> x >> y;
			if (((pow(x, 2)) + (pow(y, 2)) < 1) && (pow(x, 2)) + (pow(y, 2)) > (((2 / acos(-1)) - (1 / sqrt(2))) / 2))
				k = k + 1;
			if (((pow(x, 2)) + (pow(y, 2)) > 0) && (pow(x, 2)) + (pow(y, 2)) < (((2/acos(-1))-(1/sqrt(2)))/2))
				l=l+1;
		}

		std::cout << std::endl;
		if (k/l< 1)
			c[j] = 1;

	}
	for (int k = 0; k < 100; k++)
		if (c[k] == 1)
			std::cout << 2 << std::endl;
		else
			std::cout << 1 << std::endl;

	return 0;
}