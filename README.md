

# Assignment 4 - Program Analysis Using Constraints

Jiwon Lee <br>
Parker Mitchell


## Approach
For this assignment, we spent a lot of time to understand the paper better before we started playing around with the Z3. 

We had little trouble installing z3 python version at first because some libraries got overwritten when we installed both 'z3' and 'z3-solver'. With both packages installed, python didn't recognized imported library inside the code. We solved this issue by uninstalling 'z3' and only keeping 'z3-solver' package. 

After the installation, we ran simple example from the z3-solver documentation to see how it works (simple_sat.py). This gave us some ideas what calls we should be making to get the results we want to see (i.e. satisfiability, model). Then we created our own simple_smt.py file to test simpler yet similar expression that we want to run later.
