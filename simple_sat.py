# one of the examples from the z3 github
# Conjuctive Normal Form Example
# (Tie | Shirt) & (Not Tie | Shirt) & (Not Tie | Not Shirt)

# gives satisfying boolean assignment for the above CNF example

from z3 import *

Tie, Shirt = Bools('Tie Shirt')
s = Solver()
s.add(Or(Tie, Shirt), 
    Or(Not(Tie), Shirt), 
    Or(Not(Tie), Not(Shirt)))
print(s.check())
print(s.model())
