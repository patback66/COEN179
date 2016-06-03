#include<iostream>
#include<math.h>
#include<iomanip>

using namespace std;

double fcn(double x, double a)
{
    return (x+a/x)/2;
}

int main()
{
 long long steps = 0;
 double epsilon = 1e-6; // 3-digit precision
 double  a, b=1;

 cout.setf(ios::fixed);
 cout.setf(ios::showpoint);
 cout.precision(6);     // 3-digit precision

 cout << "Input number ";
 cin >> a;

 while(fabs(fcn(b,a)-b) > epsilon) {
   b=fcn(b,a);
   steps++;
 }

 cout << b << endl;
 cout << steps << endl;

 return 0;
}
