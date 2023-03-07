//what this is doing is that it is finding the gcd of two numbers and also the values of x and y such that ax + by = gcd(a, b)
// this will print 200 11 1600
//the x is equal to 11 and the y is equal to -200
// result will be 1600
#include <stdio.h>
int foo(int a, int b, int *x, int *y)
{
    if (a == 0)
    {
        *x = 0;
        *y = 1;
        return b;
    }
    int x1, y1;
    int d = foo(b % a, a, &x1, &y1);
    *x = y1 - (b / a) * x1;
    *y = x1;
    return d;
}
int main()
{
    int a = 13;
    int b = 41;
    int x, y;
    int res = foo(a, b, &x, &y);
    printf("%d %d %d", x, y, res);
    int z = a*x + b*y;
    // 19 * 13 - 6 *41 = 1
    // 5 * 13 - 2 * 41 = 1
    printf("%d", z);
    return 0;
}