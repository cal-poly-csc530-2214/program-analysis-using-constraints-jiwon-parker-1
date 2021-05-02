# first constraint from the paper,
# not expanded out using farkas' lemma

# intention is to see how close to true --> I[-50/x]
# we can get using Z3 to reduce expansion work with
# De Morgan's laws/negations/etc

from z3 import *

t = Bools('t')
a1, a2, a3, a4, a5, a6, y = Ints('a1 a2 a3 a4 a5 a6 y')

s = Solver()

first = ((-50 * a1) + (a2 * y) + (a3) >= 0)
second = ((-50 * a4) + (a5 * y) + (a6) >= 0)

left_side = t
right_side = Or(first, second)
full = ForAll([y], Implies(True, right_side))

print("Solve constraint:")
solve(full)

print("- - - - - - - - - - - - - - - - - - - - - - - - - - - -")

s.add(ForAll([y], full))

print(s.sexpr())
print("Checking...")
print(s.check())
print(s.model())
