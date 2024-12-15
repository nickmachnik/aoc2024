#!/usr/bin/env python

import sys
import numpy as np

class ClawMachine():
    def __init__(self, buf):
        self.button_a_data = self.get_button_data_from_line(buf[0])
        self.button_b_data = self.get_button_data_from_line(buf[1])
        self.target_vals = self.get_prize_data_from_line(buf[2])

    def get_prize_data_from_line(self, line):
        x, rest = line.split('X=')[1].split(',')
        _, y = rest.split('=')
        return [int(x), int(y)]

    def get_button_data_from_line(self, line):
        x, rest = line.split('X+')[1].split(',')
        _, y = rest.split('+')
        return [int(x), int(y)]

    def solve(self):
        X = np.array([self.button_a_data, self.button_b_data]).T
        y = np.array(self.target_vals) + 10000000000000
        beta = np.round(np.linalg.inv(X.T @ X) @ X.T @ y)
        # check that integer solution works
        if np.all(X @ beta == y):
            return beta[0] * 3 + beta[1]
        else:
            return 0


def main():
    infile = sys.argv[1]
    machines = parse(infile)
    coinsum = 0
    for machine in machines:
        coinsum += machine.solve()
    print(int(coinsum))


def parse(file):
    machines = []
    buf = []
    with open(file, 'r') as fin:
        for line in fin:
            line = line.strip()
            if line.startswith('Button'):
                buf.append(line)
            elif line.startswith('Prize'):
                buf.append(line)
            else:
                machines.append(ClawMachine(buf))
                buf = []
    machines.append(ClawMachine(buf))
    return machines


if __name__ == "__main__":
    main()