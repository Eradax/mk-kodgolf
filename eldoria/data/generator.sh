#!/usr/bin/env bash
. ../../../testdata_tools/gen.sh

use_solution erik.py
compile gen_rand.py

samplegroup
sample 1

NMAX=5000

group group1 100
tc 1
for i in {1..30}; do
    tc "g1-$i" gen_rand nmax=$NMAX
done