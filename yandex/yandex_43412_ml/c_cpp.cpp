#include <bits/stdc++.h>
using namespace std;

const int MOD = 1000000007;

int inv(int a) {
    int r = 1, t = a, k = MOD - 2;
    while (k) {
        if (k & 1) r = (long long) r * t % MOD;
        t = (long long) t * t % MOD;
        k >>= 1;
    }
    return r;
}

int main() {
    int n, k;
    cin >> n >> k;

    vector<int> p(n, k);

    int a = 1, b = 0;
    for (int i = 0; i < n; i++) {
        a = (long long) a * inv(p[i]) % MOD;
        b = (long long) b * inv(p[i]) % MOD;
        a = (a + (long long) (p[i] - 1) * inv(p[i])) % MOD;
        b = (b - inv(p[i]) + MOD) % MOD;
    }
    cout << (long long) (((MOD - b) * inv(a) % MOD) / (k + 1) * k) << "\n";
    return 0;
}