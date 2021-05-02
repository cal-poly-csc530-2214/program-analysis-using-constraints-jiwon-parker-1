

# Assignment 4 - Program Analysis Using Constraints

Jiwon Lee <br>
Parker Mitchell


## Approach
For this assignment, we spent a lot of time to understand the paper better before we started playing around with the Z3. 

We had little trouble installing z3 python version at first because some libraries got overwritten when we installed both 'z3' and 'z3-solver'. When both packages were installed, python didn't recognized the imported z3 library. We solved this issue by uninstalling 'z3' and only keeping 'z3-solver' package. 

After the installation, we ran simple example from the z3-solver documentation to see how it works (simple_sat.py). This gave us some ideas what calls we should be making to get the results we want to see (i.e. satisfiability, model). Then we created our own simple_smt.py file to test simpler yet similar expression that we want to run later. 

Second, we created a `VersionSpaceAlgebra.py` class to represent the concept of a version space algebra. This class has two attributes representing two different version spaces.

In the `VersionSpaceAlgebra.py` class we provide three methods:

1. `union()`: a method to union two version spaces
2. `join()`: a method to join to version spaces
3. `C(h1, h2, D)`: a function that performs a "consistency check that can be used to select which pairs in the cross product can actually be combined together"[1].

The lecture notes and [this MIT webpage](https://people.csail.mit.edu/asolar/SynthesisCourse/Lecture6.htm) proved very useful to our work and understanding, especially when determining how to implement the `union()` and `join()` methods, especially the figures below:

1. Version Space terminology and definitions <br> ![Terminology and definitions](images/vsf.png) [1]
2. Join definition <br> ![Join definition](images/join.png) [1]

__Note:__ More detailed explanations for all methods and datatypes can be found in the source files.


## References
1. “Lecture 6.” https://people.csail.mit.edu/asolar/SynthesisCourse/Lecture6.htm (accessed Apr. 19, 2021).

