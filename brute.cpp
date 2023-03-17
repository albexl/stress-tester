#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<ll, int> pii;

int brute(vector<int> &a, int x)
{

    for (int i = 0; i < a.size(); i++)
        if (a[i] == x)
            return i;
    return -1;
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;
    vector<int> a(n);
    for (int i = 0; i < n; i++)
        cin >> a[i];
    int x;
    cin >> x;

    cout << brute(a, x) << endl;

    return 0;
}