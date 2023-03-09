#include <math.h>
#include "circle.hpp"

void Circle::move(double dx, double dy)
{
	center.move(dx, dy);
}

inline double angle(double a, double b, double c)
{
	return std::acos((a*a + b*b - c*c) / (2.0*a*b));
}

inline double area(double r, double theta)
{
	return 0.5 * r*r * (theta - std::sin(theta));
}

double Circle::intersectionArea(const Circle &other)
{
	double d = center.distanceFrom(other.center);
	double r1 = this->radius;
	double r2 = other.radius;

	if (r1 + r2 <= d) {
		
		return 0.0;
	}
	if (r1 > r2) {
		double temp = r1;
		r1 = r2;
		r2 = temp;
	}

	if (d <= r2 - r1) {
		
		return M_PI * r1 * r1;
	}
	
	double m, n;
	m = 2.0 * angle(r1, d, r2);
	n = 2.0 * angle(r2, d, r1);
	return area(r1, m) + area(r2, n);
}
