#include "function.h"

#include <exception>
#include <cmath>
#include <cstdlib>
#include <iostream>

// Next README
int binarySearchForZero(Function<int, int> *f, int low, int high);

class CountedIntFn: public Function<int, int> {
class Invokations: std::exception {};

int count;
const char *obj;

public: virtual int Invoke(int) = 0;
	CountedIntFn(const char *obj) : obj(obj) {}
	virtual int invoke(int n)
	{
		if (!(count > 0)) {
			throw Invokations();
		}
		count--;
		return Invoke(n);
	}
	void run(int low, int high, int ans, int maxInv)
	{
		int r;
		bool over_count = false;
		

		count = maxInv;
		try {
			r = binarySearchForZero(this, low, high);
		} catch (const Invokations& e) {
			over_count = true;
		}
		
		if (r != ans) {
			std::cerr << "wrong answer when doing bsearch" << obj
				<< ", expected = " << ans
				<< ", got " << r << "\n";
			std::exit(1);
		}
		if (over_count) {
			std::cerr << obj << "invoked object more than requirement";
			std::exit(1);
		}
	}
};
// Next README
class SinCheck : public CountedIntFn {
public:
	SinCheck() : CountedIntFn("SinFunction") {}
	
	virtual int Invoke(int n) {
		return 10000000 * (std::sin(n / 100000.0) - 0.5);
	}
};

class Linear : public CountedIntFn {
public:
	Linear() : CountedIntFn("Linear") {}
	virtual int Invoke(int n) {return n;}
};

int main()
{
	//Next README
	SinCheck().run(0, 150000, 52359, 20); 

	Linear().run(-1, 5, 1, 2);
	Linear().run(0, 0, 0, 0);
	Linear().run(1, 2, 3, 4);
	Linear().run(-2, -3, -4, -5);
	
}
