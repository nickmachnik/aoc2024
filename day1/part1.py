#!/usr/bin/env python

import sys
import numpy as np


def main():
    infile = sys.argv[1]
    l1, l2 = parse(infile)
    print(np.sum(np.abs(np.array(sorted(l1)) - np.array(sorted(l2)))))

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