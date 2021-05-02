# one of the examples from the z3 github

from z3 import *

x, y = Ints('x y')
s = Solver()
s.add((x % 4) + 3 * (y / 2) > x - y)
print(s.sexpr())
print("Checking...")
print(s.check())
print(s.model())
