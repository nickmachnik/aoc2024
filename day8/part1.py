#!/usr/bin/env python

import sys
from itertools import permutations

def main():
    infile = sys.argv[1]
    anode_locs = set()
    antennae, nrows, ncols = parse_input(infile)
    for _atype, alocs in antennae.items():
        for a, b in permutations(alocs, r=2):
            anode = calc_antinode(a, b)
            if in_bounds(anode, nrows, ncols):
                anode_locs.add(anode)
    print(len(anode_locs))


def calc_antinode(a, b):
    delta = (b[0] - a[0], b[1] - a[1])
    return (b[0] + delta[0], b[1] + delta[1])


def in_bounds(loc, nrows, ncols):
    return loc[0] >= 0 and loc[0] < nrows and loc[1] >= 0 and loc[1] < ncols

def parse_input(file):
    ncols = 0
    nrows = 0
    antennae = dict()
    with open(file, 'r') as fin:
        for row, line in enumerate(fin):
            line = line.strip()
            nrows += 1
            ncols = len(line)
            for col, sym in enumerate(line):
                if sym != '.':
                    if sym not in antennae:
                        antennae[sym] = []
                    antennae[sym].append((row, col))
    return antennae, nrows, ncols
            
            




if __name__ == "__main__":
    main()