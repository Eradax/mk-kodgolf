#!/usr/bin/env bash
. ../../testdata_tools/gen.sh

use_solution erik.py
compile gen_rand.py

samplegroup
sample 1

MAXN=100000
MAXD=1000000000

group group1 100
limits maxn=$MAXN maxd=$MAXD
tc 1
for i in {1..30}; do
    tc "g1-$i" gen_rand nmax=$MAXN dmax=$MAXD
done
