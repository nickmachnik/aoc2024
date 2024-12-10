#!/usr/bin/env python

import sys
from queue import Queue
import numpy as np


class Map():
    def __init__(self, infile):
        self._parse(infile)
        self.nrows = self.map.shape[0]
        self.ncols = self.map.shape[1]

    def get_trailhead_score_sum(self):
        res = 0
        for row in range(self.nrows):
            for col in range(self.ncols):
                if self.at((row, col)) == 0:
                    res += self.count_paths((row, col))
        return res

    def count_paths(self, th: (int, int)):
        q = Queue()
        q.put(th)
        counts = np.zeros_like(self.map)
        queued = set()
        queued.add(q)
        counts[th[0], th[1]] = 1
        reached_peaks = set()
        while not q.empty():
            pos = q.get()
            pos_val = self.at(pos)
            for nb in self.get_neighbors(pos):
                nb_val = self.at(nb)
                if (nb_val - pos_val) == 1:
                    counts[nb[0], nb[1]] += counts[pos[0], pos[1]]
                    if nb_val == 9:
                        reached_peaks.add(nb)
                    elif nb not in queued:
                        queued.add(nb)
                        q.put(nb)
        res = sum(counts[pos[0], pos[1]] for pos in reached_peaks)
        return res

    def get_neighbors(self, pos: (int, int)):
        cand = [
            (pos[0], pos[1] + 1),
            (pos[0] + 1, pos[1]),
            (pos[0], pos[1] - 1),
            (pos[0] - 1, pos[1]),
        ]
        return [p for p in  cand if self.is_in_bounds(p)]

    def is_in_bounds(self, p):
        return p[0] >= 0 and p[1] >= 0 and p[0] < self.nrows and p[1] < self.ncols

    def at(self, pos: (int, int)):
        return self.map[pos[0], pos[1]]

    def _parse(self, infile):
        self.map = []
        with open(infile, 'r') as fin:
            for line in fin:
                self.map.append([int(e) for e in line.strip()])
        self.map = np.array(self.map)


def main():
    infile = sys.argv[1]
    m = Map(infile)
    print(m.get_trailhead_score_sum())

if __name__ == "__main__":
    main()