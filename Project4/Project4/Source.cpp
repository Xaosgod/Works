#include <iostream>;
#include <math.h>
#include <vector>
int main()
{
	double x1, x2, x3, x4, x5, x6, a1, a2, a3, a4, a5, a6;
	int h, m, u, mmmm;
	long long p;
	double k, i;
	long double l,t;


	k = 0;
	std::cin >> x1 >> x2 >> x3 >> x4 >> x5 >> x6;
	std::cin >> k;
	l = 0;
	//const long long pp = pow(6, k);
	//std::vector < std::vector <double> > a(pp, std::vector <double>(k));


	long long x[6];
	long double a[6];
	long long y[6];
		x[0] = x1;
	x[1] = x2;
	x[2] = x3;
	x[3] = x4;
	x[4] = x5;
	x[5] = x6;
	
	for (int i = 0; i < 6; i++)
		y[i] = 1;
	
	int y1, y2, y3, y4, y5, y6;
	for(int j=0;j<6;j++)
	for (int i = j; i < 5; i++)
		if (x[j] == x[i + 1])
		{
			if (y[j] != 0)
			{
			
			y[j] = y[j] + 1;
			a[i + 1] = 0;
			y[i + 1] = 0;
		}
}
	//a[0] = x1 *y[0]* (pow(6, k - 1));
	//a[1] = x2 * y[1]*(pow(6, k - 1));
	//a[2] = x3 * y[2]*(pow(6, k - 1));
	//a[3] = x4 * y[3]*(pow(6, k - 1));
	//a[4] = x5 * y[4]*(pow(6, k - 1));
	//a[5] = x6 * y[5]*(pow(6, k - 1));
	//for (int i = 0; i < k - 1; i++)
		for(int j=0;j<6;j++)
	a[j] = x[j]*y[j]*(6*k-k*y[j]+y[j]);
	//a2 = a2 + x2 * y[i]*(pow(6, k - 1) - y2*pow(6, k - 2));
	//a3 = a3 + x3 * y3*(pow(6, k- 1)-y3*pow(6, k - 2));
	//a4 = a4 + x4 * y4*(pow(6, k- 1) - y4*pow(6, k - 2));
	//a5 = a5 + x5 * y5*(pow(6, k - 1) - y5*pow(6, k - 2));
	//a6 = a6 + x6 * y6*(pow(6, k - 1) - y6*pow(6, k - 2));
   
	t = a[1] + a[2] + a[3] + a[4] + a[5] + a[0];
	t = t*pow(6,-2);
	std::cout << t;
}