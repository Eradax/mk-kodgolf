#include "validate.h"
#include <bits/stdc++.h>
using namespace std;

#define rep(i, a, b) for(int i = a; i < (b); ++i)
#define all(x) begin(x), end(x)
#define sz(x) (int)(x).size()
#define debug(...) //ignore
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef long double ld;

int main(int argc, char **argv) {
	init_io(argc, argv);
	
	int n;
	judge_in >> n;

    vvi rows;
    int nc = n;
    while (nc > 0) {
        vi row(min(5, nc));
        for (int i = 0; i < min(5, nc); i++)
            judge_in >> row[i];
        rows.push_back(row);
        nc -= sz(row);
    }

	auto cmp = [&](istream& ans, istream& sol) -> bool {
        istream::pos_type p1 = ans.tellg();
        istream::pos_type p2 = sol.tellg();

        if (p1 == -1 || p2 == -1)
            return 0;
        
        ans.seekg(0, ios::beg);
        sol.seekg(0, ios::beg);

        char c1, c2;
        while (1) {
            ans.get(c1);
            sol.get(c2);

            if (ans.eof() && sol.eof())
                break;

            if (ans.eof() != sol.eof() || c1 != c2) {
                ans.clear();
                sol.clear();
                ans.seekg(p1);
                sol.seekg(p2);

                return 1;
            }
        }
        

        ans.clear();
        sol.clear();
        ans.seekg(p1);
        sol.seekg(p2);

        return 0;
	};

    if (cmp(judge_ans, author_out))
        wrong_answer("Contestants output differed from judge");
    else
        accept();
}