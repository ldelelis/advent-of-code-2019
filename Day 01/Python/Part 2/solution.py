#!/usr/bin/env python3

import sys

vals = [int(x) for x in sys.stdin.read().strip().split('\n')]

sums = []
for v in vals:
    while v is not None:
        v = v // 3 - 2
        if v <= 0:
            v = None
        else:
            sums.append(v)

print(sum(sums))
