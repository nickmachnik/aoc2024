#!/usr/bin/env python

import sys
import numpy as np
import time

# Got a tree at NITER=111888

# EXAMPLE
# NCOLS = 11
# NROWS = 7

# ACTUAL SIZE
NCOLS = 101
NROWS = 103

class Robot():
    def __init__(self, pos, vel):
        self.pos = pos
        self.vel = vel

    def print(self):
        print(self.pos, self.vel)

    def move(self, niter):
        new_x = (self.pos[0] + niter * self.vel[0]) % NCOLS
        new_y = (self.pos[1] + niter * self.vel[1]) % NROWS
        self.pos = (new_x, new_y)


def main():
    infile = sys.argv[1]
    MINITER = int(sys.argv[2])
    MAXITER = int(sys.argv[3])
    robots = parse(infile)
    xmas_pos = get_xmas_tree_pos()
    for r in robots:
        r.move(MINITER)
    for i in range(MINITER, MAXITER):
        for r in robots:
            r.move(1)
        if xmas_pos <= make_rpos_set(robots):
            print(i + 1)
            print_map(robots)
            break


def print_map(robots):
    m = []
    for _ in range(NROWS):
        m.append([' '] * NCOLS)
    for r in robots:
        m[r.pos[1]][r.pos[0]] = 'X'
    time.sleep(0.2)
    print('\n'.join([''.join(row) for row in m]))
    print()


def make_rpos_set(robots):
    res = set()
    for r in robots:
        res.add(r.pos)
    return res


def parse(infile):
    robots = []
    with open(infile, 'r') as fin:
        for line in fin:
            line = line.strip()
            ppart, vpart = line.split()
            pa, pb = [int(e) for e in ppart.split('=')[1].split(',')]
            va, vb = [int(e) for e in vpart.split('=')[1].split(',')]
            robots.append(Robot((pa, pb), (va, vb)))
    return robots


def get_xmas_tree_pos():
    pos = set()
    with open("./christmas_tree.txt", 'r') as fin:
        rix = 0
        for line in fin:
            if rix > 43:
                for cix in range(36, 65):
                    if line[cix] == 'X':
                        pos.add((cix, rix))
            if rix > 75:
                break
            rix += 1
    return pos


if __name__ == "__main__":
    main()