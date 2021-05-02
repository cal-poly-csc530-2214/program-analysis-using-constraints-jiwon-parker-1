# our own simple smt example
# to prove/see unsat

from z3 import *

a1, a2, a3, a4, a5, a6, l, l1, l2 = Ints('a1 a2 a3 a4 a5 a6 l l1 l2')
s = Solver()
s.add((((50*a1*l1) - (a3*l1) - l1) + ((50*a4*l2) - (a6*l2) - l2) == -l) and ((a2*l1)+(a5*l2) == 0))
print(s.sexpr())
print("Checking...")
print(s.check())
