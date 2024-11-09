#include <iostream>
#include <vector>

using namespace std;

long long minEnd(int n, int x)
{
    long long ans = x;
    long long pow2 = 1;
    n--;
    while (n > 0)
    {
        if ((x & 1) == 0)
        {
            ans = ((n & 1) == 1) ? (ans | pow2) : ans;
            n = n >> 1;
        }
        x = x >> 1;
        pow2 = pow2 << 1;
    }

    return ans;
}

int main()
{
    cout<<minEnd(3, 4);
    return 0;
}