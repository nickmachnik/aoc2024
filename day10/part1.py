#!/usr/bin/env python

import sys
from queue import Queue

class Map():
    def __init__(self, infile):
        self._parse(infile)
        self.nrows = len(self.map)
        self.ncols = len(self.map[0])
        # self._print_map()

    def _print_map(self):
        for row in self.map:
            print(''.join([str(e) for e in row]))

    def get_trailhead_score_sum(self):
        res = 0
        for row in range(self.nrows):
            for col in range(self.ncols):
                if self.at((row, col)) == 0:
                    print((row, col))
                    res += self.count_peaks((row, col))
        return res

    def count_peaks(self, th: (int, int)):
        count = 0
        q = Queue()
        q.put(th)
        queued = set()
        queued.add(q)
        while not q.empty():
            pos = q.get()
            pos_val = self.at(pos)
            for nb in self.get_neighbors(pos):
                nb_val = self.at(nb)
                if (nb_val - pos_val) == 1 and nb not in queued:
                    queued.add(nb)
                    if nb_val == 9:
                        count += 1
                    else:
                        q.put(nb)
        return count

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
        return self.map[pos[0]][pos[1]]

    def _parse(self, infile):
        self.map = []
        with open(infile, 'r') as fin:
            for line in fin:
                self.map.append([int(e) for e in line.strip()])

def main():
    infile = sys.argv[1]
    m = Map(infile)
    print(m.get_trailhead_score_sum())

if __name__ == "__main__":
    main()