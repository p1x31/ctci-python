#include <stdio.h>
long long func(long long a, long long n)
{
    if (n == 0)
        return 1;
    if (n & 1)
        return func(a, n & -2) * a;
    else
    {
        long long b = func(a, n >> 1);
        return b * b;
    }
}
// if given input is 12 4 then output should be 20736
int main()
{
    long long a, b;
    scanf("%lld%lld", &a, &b);
    printf("%lld", func(a, b));
    return 0;
}
       
