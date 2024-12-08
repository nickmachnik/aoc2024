#!/usr/bin/env python

import sys
from itertools import permutations

def main():
    infile = sys.argv[1]
    anode_locs = set()
    antennae, nrows, ncols = parse_input(infile)
    for _atype, alocs in antennae.items():
        for a, b in permutations(alocs, r=2):
            anodes = calc_antinodes(a, b, nrows, ncols)
            anode_locs.update(anodes)
    print(len(anode_locs))


def calc_antinodes(a, b, nrows, ncols):
    res = []
    delta = (b[0] - a[0], b[1] - a[1])
    dfactor = 0
    while True:
        anode = (b[0] + dfactor * delta[0], b[1] + dfactor * delta[1])
        if not in_bounds(anode, nrows, ncols):
            return res
        else:
            dfactor += 1
            res.append(anode)


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