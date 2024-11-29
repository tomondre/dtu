from z3 import *

# Create Z3 Solver
solver = Solver()

# Define Boolean variables for states at each time step
s0_0 = Bool('s0_0')
s1_1 = Bool('s1_1')
s5_1 = Bool('s5_1')
s2_2 = Bool('s2_2')
s0_2 = Bool('s0_2')
s6_2 = Bool('s6_2')

# Propositions (heat and closed) at each time step
heat_0 = Bool('heat_0')
closed_0 = Bool('closed_0')
heat_1 = Bool('heat_1')
closed_1 = Bool('closed_1')
heat_2 = Bool('heat_2')
closed_2 = Bool('closed_2')

# Initial state constraints
solver.add(s0_0 == True)  # Initial state is s0^0
solver.add(heat_0 == False, closed_0 == False)  # Initially, no heat and door is open

# Transition constraints
solver.add(Implies(s0_0, Or(s1_1, s5_1)))  # Transition from s0^0 to s1^1 or s5^1
solver.add(Implies(s1_1, s2_2))  # Transition from s1^1 to s2^2
solver.add(Implies(s5_1, Or(s0_2, s6_2)))  # Transition from s5^1x to s0^2 or s6^2

# Property constraints: Microwave should not heat until door is closed
solver.add(Or(closed_0, 
             And(Not(heat_0), closed_1), 
             And(Not(heat_0), Not(heat_1), closed_2)))  # Unfolded property constraint

# Check satisfiability to find a counterexample
if solver.check() == sat:
    print("SAT: A counterexample exists.")
    model = solver.model()
    # Output the truth assignment for each state and proposition
    for var in [s0_0, s1_1, s5_1, s2_2, s0_2, s6_2, heat_0, closed_0, heat_1, closed_1, heat_2, closed_2]:
        print(f"{var}: {model[var]}")
else:
    print("UNSAT: No counterexample exists within the bound.")
