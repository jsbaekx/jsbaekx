#include <stdio.h>
#define M_PI 3.14159265358979

#include <math.h>


int main(void)
{
	double x1, x2, y1, y2, r1, r2;
	double dis;
	double Rr;
	double a, b;
	double L, A;
	double temp;
	double pit;
	int LL, AA;

	scanf("%lf%lf%lf", &x1, &y1, &r1);
	scanf("%lf%lf%lf", &x2, &y2, &r2);

	if (r2 > r1)
	{
		temp = r1;
		r1 = r2;
		r2 = temp;

		temp = x1;
		x1 = x2;
		x2 = temp;

		temp = y1;
		y1 = y2;
		y2 = temp;
	}
	dis = sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1));
	Rr = fabs(r2 - r1);
	
	pit = sqrt(dis * dis - Rr * Rr);
	a = fabs(acos(Rr / dis));
	b = M_PI / 2 - a;
	
	L = 2 * M_PI * r1 * ((2 * M_PI - 2 * a) / (2 * M_PI)) + 2 * pit + 2 * M_PI * r2 * ((M_PI - 2 * b) / (2 * M_PI));
	A = pit * (r1 + r2) + (r1 * r1 * (2 * M_PI - 2 * a)) / 2 + (r2 * r2 * (M_PI - 2 * b)) / 2;

	LL = (int)floor(L);
	AA = (int)floor(A);
	printf("%d %d", LL, AA);
	return 0;
}