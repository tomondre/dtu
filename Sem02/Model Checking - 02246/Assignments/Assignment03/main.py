from z3 import *

# Create a solver instance
solver = Solver()

# Number of steps (k = 2)
k = 2

# Declare Boolean variables for each time step
s = [Bool('s{}'.format(i)) for i in range(k + 1)]  # s[0], s[1], s[2]

# Initial state constraint: s[0] = True (a holds at initial state)
solver.add(s[0])

# Transition constraints
for i in range(k):
    # Transition constraint: s[i] or Not(s[i+1])
    # This ensures that if s[i] is False, then s[i+1] is also False
    # If s[i] is True, s[i+1] can be either True or False
    solver.add(Or(s[i], Not(s[i+1])))

# Property violation constraint: a does not hold at s[1] or s[2]
solver.add(Or(Not(s[1]), Not(s[2])))

# Check for satisfiability
if solver.check() == sat:
    model = solver.model()
    # Extract the counterexample
    for i in range(k + 1):
        state_value = model.evaluate(s[i])
        print(f's[{i}] = {state_value}')
else:
    print('The property AG a holds in the system up to the given k.')
