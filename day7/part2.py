#!/usr/bin/env python

import sys
import numpy as np
import queue

class Equation():
    def __init__(self, line):
        self.line = line
        self._parse(line)
        self.num_ops_comps = 3 ** len(self.rhs)

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
            elif op == '||':
                v1 = int(str(v1) + str(v2))
        return v1

    def is_possible(self):
        num_ops = (len(self.rhs) - 1)
        start_ops = ['+'] * num_ops
        ops_cache = set()
        ops_cache.add(tuple(start_ops))
        q = queue.Queue()
        q.put(start_ops)
        while not q.empty():
            ops = q.get()
            eq_res = self.eval_eq(ops)
            if self.test_value == eq_res:
                return True
            needed_sign = np.sign(self.test_value - eq_res)
            for put_op in ['||', '*']:
                for ops_ix, op in enumerate(ops):
                    if op == put_op:
                        continue
                    loc_ops = ops.copy()
                    loc_ops[ops_ix] = put_op
                    if tuple(loc_ops) in ops_cache:
                        continue
                    diff = self.eval_eq(loc_ops) - eq_res
                    if np.sign(diff) == needed_sign:
                        ops_cache.add(tuple(loc_ops))
                        q.put(loc_ops)
        return False


def main():
    infile = sys.argv[1]
    result = 0
    with open(infile, 'r') as fin:
        for _, line in enumerate(fin):
            eq = Equation(line)
            if eq.is_possible():
                result += eq.test_value
    print(result)

    
if __name__ == "__main__":
    main()
