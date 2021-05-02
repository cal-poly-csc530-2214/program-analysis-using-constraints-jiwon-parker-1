

# Assignment 4 - Program Analysis Using Constraints

Jiwon Lee
Parker Mitchell


## Approach
For this assignment, we took a bit of a different approach. We decided to setup Python classes to serve as a framework for creating version classes and performing version space algebra.

We had trouble figuring out how exactly hypotheses spaces were formed from the inputs and outputs, and how functions could be learned from such states, so we focused on understanding the core of what a version space and version space algebra was, and how to perform some of the operations we discussed in class (namely union and join).

First, we created a `VersionSpace.py` Python class to represent a single version space. It has two class attributes, `h` and `d`, which represent the hypothesis space and set of examples respectively.

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

