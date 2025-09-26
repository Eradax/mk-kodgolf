#include <bits/stdc++.h>
#include "validator.h"
using namespace std;

#define sz(c) ((int)c.size())

void run() {
  int maxn = Arg("maxn", int(1e5));

  int n = Int(1, maxn);
  Endl();

  for (int i = 1; i < n; i++) {
    auto ai = Int(1, i + 1);
    Endl();
  }

  Eof();
}