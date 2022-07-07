#include <iostream>
#include <vector>
#include <limits.h>
#include <numeric>
//#include <bits/stdc++.h>
//#include <algorithm>

//using namespace std;

int main() {

    int n, k;
    std::cin >> n >> k;
    std::vector<int> s;
    for(int i = 1; i <= n; i++)
    {
        int x;
        std::cin >> x;
        s.push_back(x);
    }

    std::vector<int> t(k); // vector with 100 ints.
    std::iota (std::begin(t), std::end(t), 1); // Fill with 1, ..., 99.
    if (s.size() == 0 || k == 0) return 0;
    int z = k + 1; 
    std::vector<int> remaining(z, 0); //
    int required = k;
    for (int i = 0; i < required; i++) remaining[t[i]]++;
    int minsum = INT_MAX, sum_subvector_length = 0, start = 0, i = 0;
    while(i <= s.size() && start < s.size()) {
        if(required) {
            if (i == s.size()) break;
            remaining[s[i]]--;
            if (remaining[s[i]] >= 0 && (t[s[i] - 1]) == s[i]) required--;
            i++;

        } else {
            for (int j = start; j < i; j++) {
                sum_subvector_length += s[j];
            }
            if (sum_subvector_length < minsum) {
                minsum = sum_subvector_length;
            }
            remaining[s[start]]++;
            if (remaining[s[start]] >= 0 && (t[s[start] - 1]) == s[start]) required++;
            start++;
            sum_subvector_length = 0;
            
        }
    }
    std::cout << minsum;
}

