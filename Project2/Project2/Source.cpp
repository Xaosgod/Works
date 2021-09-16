#include <iostream>;
#include <math.h>
#include <vector>
int main()
{
	double x1, x2, x3, x4, x5, x6;
	int h,m,u,mmmm;
	long long p;
	double k;
	long double l;
	
	
	k = 0;
	std::cin >> x1 >> x2 >> x3 >> x4 >> x5 >> x6; 
	std::cin >> k;
	l = 0;
	const long long pp = pow(6, k);
	 std::vector < std::vector <double> > a(pp, std::vector <double>(k));
	
	//long double* a = new  double[pp][1000];
	//double a [pp][1000];
	long long x[6];
	x[0] = x1;
	x[1] = x2;
	x[2] = x3;
	x[3] = x4;
	x[4] = x5;
	x[5] = x6;
		h = 0;
		m = pow(6, k - 1);
		u= k;
		for (int n = 0; n < k; n++)
		{
			for (int j = 0; j < 6; j++)
			{

				for (int i = 0; i < pow(6, h); i++)
				{
					for (p = j * (pow(6, u - 1)) + m * i; p < (j + 1) * (pow(6, u - 1)) + m * i; p++)
					{
						a[p][n] = x[j];
					//	std::cout << a[p, n];
					}

				}
			}
			u = u - 1;
			m = pow(6, u);
			h = h + 1;
		}
		for (long long j = 0; j < (pow(6, k)); j++)
		{
			for (int i = k - 1; i >= 1; i--)
				if (a[j][i] != a[j][i - 1])
				{
					l = a[j][i] + l;
					
				}
			l = l + a[j][0];
		}
		l = l / (pow(6, k));
		std::cout.precision(10);
		std::cout <<l;
	
	//delete[]a;






}