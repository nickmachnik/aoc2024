#!/usr/bin/env python

import sys
import numpy as np

class Equation():
    def __init__(self, line):
        self.line = line
        self._parse(line)

    def print(self):
        print(self.line)

    def print_w_ops(self, ops):
        s = f'{self.rhs[0]}'
        for op_ix, op in enumerate(ops):
            s += f' {op} {self.rhs[op_ix + 1]}'
        s += f' = {self.test_value}'
        print(s)

    def _parse(self, line):
        line = line.strip()
        a, b = line.split(': ')
        self.test_value = int(a)
        self.rhs = [int(e) for e in b.split()]

    def eval_eq(self, ops):
        v1 = self.rhs[0]
        for op_ix, op in enumerate(ops):
            v2 = self.rhs[op_ix + 1]
            if op == '+':
                v1 += v2
            elif op == '*':
                v1 *= v2
        return v1

    def search_ops(self, ops, ops_cache):
        if tuple(ops) in ops_cache:
            return False
        ops_cache.add(tuple(ops))
        
        eq_res = self.eval_eq(ops)
        if self.test_value == eq_res:
            return True
        else:
            needed_sign = np.sign(self.test_value - eq_res)
            for ops_ix, op in enumerate(ops):
                if op == '*':
                    continue
                loc_ops = ops.copy()
                loc_ops[ops_ix] = '*'
                diff = self.eval_eq(loc_ops) - eq_res
                if np.sign(diff) == needed_sign and self.search_ops(loc_ops, ops_cache):
                    return True
            return False

    def is_possible(self):
        num_ops = (len(self.rhs) - 1)
        ops = ['+'] * num_ops
        return self.search_ops(ops, set())

def main():
    infile = sys.argv[1]
    result = 0
    with open(infile, 'r') as fin:
        for line in fin:
            eq = Equation(line)
            if eq.is_possible():
                result += eq.test_value
    print(result)

    
if __name__ == "__main__":
    main()