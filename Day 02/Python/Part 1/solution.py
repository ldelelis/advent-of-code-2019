#!/usr/bin/env python3
# coding: utf-8

from operator import add, mul
import sys


def chunky_range(xs, step_size):
    return (xs[pos:pos+step_size] for pos in range(0, len(xs), step_size))


opcodes = {0: add, 1: mul, 99: None}


inputs = [int(x) for x in sys.stdin.read().strip().split(',')]
inputs[1]=12
inputs[2]=2

for chunk in chunky_range(inputs, 4):
    op = opcodes[chunk[0]]
    if op is None:
        break

    pos1 = inputs[chunk[1]]
    pos2 = inputs[chunk[2]]
    inputs[chunk[3]] = op(pos1, pos2)

print(inputs[0])
