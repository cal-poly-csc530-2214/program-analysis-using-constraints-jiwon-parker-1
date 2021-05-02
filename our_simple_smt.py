# our own simple smt example
# to prove/see unsat

from z3 import *

x, y, z = Ints('x y z')
s = Solver()
# s.add((x % 4) + 3 * (y / 2) > x - y)
s.add(x + y + z < x + y + z)
print(s.sexpr())
print("Checking...")
print(s.check())
