//what this is doing is that it is finding the divisors of the number n and storing them in a vector d. 
//The vector d is then used to find the number of divisors of n. 
//The number of divisors of n is equal to the product of the exponents of the prime factors of n plus 1. 
//For example, the number of divisors of 12 is equal to (2+1)*(1+1) = 6. 
//The number of divisors of 24 is equal to (3+1)*(1+1) = 8. The number of divisors of 36 is equal to (2+1)*(2+1) = 9. 
//The number of divisors of 48 is equal to (4+1)*(1+1) = 10. 
//The number of divisors of 60 is equal to (2+1)*(2+1)*(1+1) = 12. 
//The number of divisors of 72 is equal to (3+1)*(2+1) = 16. 
//The number of divisors of 84 is equal to (2+1)*(2+1)*(1+1) = 12. 
//The number of divisors of 96 is equal to (5+1)*(1+1) = 12. 
//The number of divisors of 108 is equal to (3+1)*(2+1)*(1+1) = 24. 
//The number of divisors of 120 is equal to (3+1)*(1+1)*(2+1) = 24. 
//The number of divisors of 132 is equal to (2+1)*(2+1)*(2+1) = 27. 
//The number of divisors of 144 is equal to (4+1)*(2+1) = 30. 
//The number of divisors of 156 is equal to (2+1)*(2+1)*(2+1)*(1+1) = 36. The number of divisors of 168 is equal to (3+1)*(2+1)*(2+1) = 48. The number of divisors of 180 is equal to (2+1)*(2+1)*(3+1) = 48. The number of divisors of 192 is equal to (6+1)*(1+1) = 14. The number of divisors of 204 is equal to (2+1)*(
#include <iostream>
#include <vector>
int main()
{
    int n;
    std::cin >> n;
    std::vector<int> d;
    for (int i = 2; i * i <= n; ++i)
    {
        if (n % i == 0)
        {
            d.push_back(i);
        }
    }
    return 0;
}