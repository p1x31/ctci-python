//what this doing is that it is checking if the number is prime or not
//this will print the number of prime numbers between 20 and 200
//number of primes between 20 and 200 is 38
//output will be 38
#include <stdio.h>
int foo(int n)
{ 
    for (int i = 2; i * i <= n; ++i)
    {
        if (n % i == 0)
        {
            return 0;
        }
    }
    return 1;
}
int main(void)
{
    int result = 0;
    for (int i = 20; i <= 200; ++i)
        result += foo(i);
    printf("%d", result);
    return 0;
}