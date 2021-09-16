#include <iostream>
#include <math.h>
#include <fstream>
using namespace std;
int main()
{
	double x, y, k, l;

	double c[100] = { 0 };
	ifstream in("input.txt");
	ofstream out("output.txt");

	for (int j = 0; j < 100; j++)
	{
		k = 0;
		l = 0;

		for (int i = 0; i < 1000; i++)
		{

			in >> x >> y;
			if (((pow(x, 2)) + (pow(y, 2)) < 1) && (pow(x, 2)) + (pow(y, 2)) > (((2 / acos(-1)) - (1 / sqrt(2))) / 2))
				k = k + 1;
			if (((pow(x, 2)) + (pow(y, 2)) > 0) && (pow(x, 2)) + (pow(y, 2)) < (((2 / acos(-1)) - (1 / sqrt(2))) / 2))
				l = l + 1;
		}

		out << std::endl;
		if (k / l < 1)
			c[j] = 1;

	}
	for (int k = 0; k < 100; k++)
		if (c[k] == 1)
			out << 2 << std::endl;
		else
			out << 1 << std::endl;

	return 0;
}