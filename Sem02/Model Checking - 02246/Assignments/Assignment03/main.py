from z3 import *

solver = Solver()

s0_0 = Bool('s0_0')
s1_1 = Bool('s1_1')
s2_2 = Bool('s2_2')
s3_2 = Bool('s3_2')
s3_3 = Bool('s3_3')

solver.add(s0_0 == True)

solver.add(Implies(s0_0, s1_1))
solver.add(Implies(s1_1, Or(s2_2, s3_2)))
solver.add(Implies(s2_2, s0_0))
solver.add(Implies(s3_2, s3_3))

# Violation
solver.add(Or(Not(s0_0), Not(s1_1), Not(s2_2), Not(s3_3)))

if solver.check() == sat:
    print("SAT!")
    model = solver.model()

    if model[s0_0] == True:
        print("s0")
    if model[s1_1] == True:
        print("s1")
    if model[s2_2] == True:
        print("s2")
    if model[s3_2] == True:
        print("s3")
    if model[s3_3] == True:
        print("s3 (self-loop)")
else:
    print("UNSAT!")
