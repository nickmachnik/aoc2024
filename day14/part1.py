#!/usr/bin/env python

import sys
import numpy as np

# EXAMPLE
# NCOLS = 11
# NROWS = 7

# ACTUAL SIZE
NCOLS = 101
NROWS = 103

NITER = 100

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
    robots = parse(infile)
    for r in robots:
        r.move(NITER)
    print(quadrant_product(robots))


# def print_map(robots):
#     m = []
#     for _ in range(NROWS):
#         m.append(['.'] * NCOLS)
#     for r in robots:
#         m[r.pos[1]][r.pos[0]] = 'X'
#     for row in m:
#         print(''.join(row))
#     print()


def quadrant_product(robots):
    mid_row = NROWS // 2
    mid_col = NCOLS // 2
    quad_sums = [0, 0, 0, 0]
    for r in robots:
        # top left
        if r.pos[0] < mid_col and r.pos[1] < mid_row:
            quad_sums[0] += 1
        # top right
        elif r.pos[0] > mid_col and r.pos[1] < mid_row:
            quad_sums[1] += 1
        # bottom left
        elif r.pos[0] < mid_col and r.pos[1] > mid_row:
            quad_sums[2] += 1
        # bottom right
        elif r.pos[0] > mid_col and r.pos[1] > mid_row:
            quad_sums[3] += 1
    return np.prod(quad_sums)


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


if __name__ == "__main__":
    main()