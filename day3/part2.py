#!/usr/bin/env python

import sys
import re


def main():
    infile = sys.argv[1]
    instr = ''.join(parse(infile))
    re_str = r"don't|do|mul\([0-9]+,[0-9]+\)"
    print(eval_instrs(re.findall(re_str, instr)))


def eval_instrs(instrs):
    mul_active = True
    s = 0
    for expr in instrs:
        if expr == "don't":
            mul_active = False
        elif expr == "do":
            mul_active = True
        elif mul_active:
            sub = expr.strip(')')
            a, b = sub.split(',')
            _, a = a.split('(')
            s += int(a) * int(b)
    return s


def parse(file: str):
    lines = []
    with open(file, 'r') as fin:
        for line in fin:
            lines.append(line)
    return lines

if __name__ == "__main__":
    main()