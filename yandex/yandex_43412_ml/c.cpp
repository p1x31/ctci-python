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
    int n; cin >> n;
    int k;
    int p;
    cin >> k, p = (long long) inv(k) % MOD;
    int a = 1, b = 0;
    for (int i = 0; i < n; i++) {
        a = (long long) a * inv(p) % MOD;
        b = (long long) b * inv(p) % MOD;
        a = (a + (long long) (p - 1) * inv(p)) % MOD;
        b = (b - inv(p) + MOD) % MOD;
    }
    cout <<  (long long) (MOD - b) * inv(a) % MOD << "\n";
    return 0;
}