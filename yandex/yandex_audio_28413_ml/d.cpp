#include <iostream>
#include <vector>
#include <limits.h>
#include <numeric>
#include <bits/stdc++.h>
#include <algorithm>

using namespace std;


int getIndex(vector<int> v, int K)
{
    auto it = find(v.begin(), v.end(), K);
  
    // If element was found
    if (it != v.end()) 
    {
      
        // calculating the index
        // of K
        int index = it - v.begin();
        return index;
    }
    else {
        // If the element is not
        // present in the vector
        return 0;
    }
}

int main() {

    int n, k;
    cin >> n >> k;
    std::vector<int> s;
    for(int i = 1; i <= n; i++)
    {
        int x;
        cin >> x;
        s.push_back(x);
    }

    std::vector<int> t(k); // vector with 100 ints.
    std::iota (std::begin(t), std::end(t), 1); // Fill with 0, 1, ..., 99.
    if (s.size() == 0 || k == 0) return 0;
    // std::vector<int> remaining(128, 0);
    int z = k + 1; 
    std::vector<int> remaining(z, 0); //
    // std::iota (std::begin(remaining), std::end(remaining), 1); // Fill with 0, 1, ..., 99.
    // int sum_of_elems = std::accumulate(s.begin(), s.end(), decltype(s)::value_type(0));
    int required = k;
    for (int i = 0; i < required; i++) remaining[t[i]]++;
    // left is the start index of the min-length substring ever found
    // int min_length = INT_MAX, left = 0,
    int minsum = INT_MAX, sum_subvector_length = 0, start = 0, i = 0;
    while(i <= s.size() && start < s.size()) {
        if(required) {
            if (i == s.size()) break;
            remaining[s[i]]--;
            // if (remaining[s[i]] > 0 && (std::find(t.begin(), t.end(), remaining[s[i]]) == t.end())) required--;
            if (remaining[s[i]] >= 0 && (t[s[i] - 1]) == s[i]) required--;
            i++;

        } else {
            // if (i - start < min_length) {
            //     min_length = i - start;
            //     left = start;
            // }
            for (int j = start; j < i; j++) {
                sum_subvector_length += s[j];
            }
            if (sum_subvector_length < minsum) {
                minsum = sum_subvector_length;
                // left = start;
            }
            remaining[s[start]]++;
            // if (remaining[s[start]] > 0 && (std::find(t.begin(), t.end(), remaining[s[start]]) == t.end())) required++;
            if (remaining[s[start]] >= 0 && (t[s[start] - 1]) == s[start]) required++;
            start++;
            sum_subvector_length = 0;
            
        }
    }
    //minsum = min(minsum, sum_subvector_length);
    cout << minsum;
}

