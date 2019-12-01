#!/usr/bin/env python3

import sys

print(sum(int(x) // 3 - 2 for x in sys.stdin.read().strip().split('\n')))
