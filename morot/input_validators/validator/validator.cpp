#include <bits/stdc++.h>
#include "validator.h"
using namespace std;

void run() {
	int maxn = Arg("maxn", int(1e5));

	int n = Int(1, maxn);
	Endl();

    int nc = n;
    while (nc > 0) {
     SpacedInts(min(5, nc), -1, 0);
     nc -= min(5, nc);
    }
    Eof();
}