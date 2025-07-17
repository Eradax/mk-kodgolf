#include <bits/stdc++.h>
#include "validator.h"
using namespace std;

#define sz(c) ((int)c.size())

void run() {
	int maxn = Arg("maxn", int(1e5));
    int maxd = Arg("maxd", int(1e9));

	int n = Int(1, maxn);
	Endl();

    auto ei = SpacedInts(n, 0, 2 * n - 1);
    auto ki = SpacedInts(n, 0, 2 * n - 1);

    for (int i = 0; i < n; i++)
        assert((ei[i] == 2 * i && ki[i] == 2 * i + 1) || (ei[i] == 2 * i + 1 && ki[i] == 2 * i));

    for (int i = 0; i < 2 * n; i++) {
        Int(1, maxd);
        Endl();
    }

    Eof();
}