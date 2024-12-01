#!/usr/bin/env python

import sys
import numpy as np


def main():
    infile = sys.argv[1]
    l1, l2 = parse(infile)
    counts = count_dict(l2)
    print(np.sum([e1 * counts[e1] if e1 in counts else 0 for e1 in l1]))

def count_dict(l):
    res = dict()
    for e in l:
        if e not in res:
            res[e] = 0
        res[e] += 1
    return res

def parse(file: str):
    l1 = []
    l2 = []
    with open(file, 'r') as fin:
        for line in fin:
            a, b = [int(e) for e in line.split()]
            l1.append(a)
            l2.append(b)
    return l1, l2

if __name__ == "__main__":
    main()