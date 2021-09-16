#include <iostream>
#include <math.h>
int main()
{
	double x, y, a, b;

	double c[100] = { 0 };

	for (int j = 0; j < 100; j++)
	{

		for (int i = 0; i < 1000; i++)
		{

			std::cin >> x >> y;

			b = (atan(y / x) / (2 * acos(-1)));
			a = x / cos(b * 2 * acos(-1));

			if ((a > 1) || (b > 1))
				c[j] = 1;
		}
		std::cout << std::endl;
	}
		for (int k=0;k<100;k++)
		if (c[k] == 1)
			std::cout << 2<< std::endl;
		else
			std::cout << 1 << std::endl;
	
		return 0;
}