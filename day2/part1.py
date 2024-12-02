#!/usr/bin/env python

import sys
import numpy as np


def main():
    infile = sys.argv[1]
    lines = parse(infile)
    print(sum(is_valid(l) for l in lines))


def is_valid(line):
    n = len(line)
    last_sign = None
    for p in range(1, n):
        delta = line[p - 1] - line[p]
        sign = np.sign(delta)
        if np.abs(delta) > 3 or delta == 0:
            return False
        if last_sign is not None and last_sign != sign:
            return False
        last_sign = sign
    return True


def parse(file: str):
    lines = []
    with open(file, 'r') as fin:
        for line in fin:
            lines.append([int(e) for e in line.strip().split()])
    return lines

if __name__ == "__main__":
    main()