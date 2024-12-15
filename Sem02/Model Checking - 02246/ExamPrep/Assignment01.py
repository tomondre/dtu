from z3 import *

routers = range(1,8)
vlans = [110,120,130,140]

def X(i, d, j):
    return Bool(f"X_{i}_{d}_{j}")

s = Solver()

# Constraint (i) repeated: No router forwards packet to itself unless it serves that VLAN
serve_map = {4:110, 5:120, 6:130, 7:140}
for i in routers:
    for d in vlans:
        if i not in serve_map or serve_map[i] != d:
            # If router i does not serve VLAN d, no self-forward:
            s.add(Not(X(i, d, i)))

# Constraint (ii):
# (S(4,d,j) <-> S(5,d,j)) and (S(6,d,j) <-> S(7,d,j))
for d in vlans:
    for j in routers:
        s.add(X(4,d,j) == X(5,d,j))  # Biimplication: both must have the same value
        s.add(X(6,d,j) == X(7,d,j))  # Same for r6 and r7

# Constraint (iii):
for i in routers:
    s.add(Implies(X(4,130,i), X(4,130,3)))
    s.add(Implies(X(4,140,i), X(4,140,3)))
    s.add(Implies(X(5,130,i), X(5,130,3)))
    s.add(Implies(X(5,140,i), X(5,140,3)))
    s.add(Implies(X(6,110,i), X(6,110,2)))
    s.add(Implies(X(6,120,i), X(6,120,2)))
    s.add(Implies(X(7,110,i), X(7,110,2)))
    s.add(Implies(X(7,120,i), X(7,120,2)))
    s.add(Implies(X(3,110,i), X(3,110,1)))
    s.add(Implies(X(3,120,i), X(3,120,1)))
    s.add(Implies(X(2,130,i), X(3,130,1)))
    s.add(Implies(X(2,140,i), X(3,140,1)))

# Now the "Table" constraints:

s.add(X(2,110,4))
s.add(Or(X(2,120,4), X(2,120,5)))
s.add(X(2,130,6))
s.add(X(2,140,1))

s.add(Or(X(4,120,2), X(4,120,5)))
s.add(X(4,130,3))
s.add(X(4,140,1))
s.add(X(4,110,1))

s.add(Or(X(6,140,3), X(6,140,7)))
s.add(X(6,130,1))
s.add(X(6,120,3))
s.add(X(6,110,3))

# Trying out
# s.add(X(7, 140, 7))
# s.add(X(7, 110, 4))
# s.add(X(4, 110, 4))


# Check satisfiability
if s.check() == sat:
    print("SAT")
    model = s.model()
    # Print out the chosen assignments
    for var in model:
        if model[var] == True:
            print(var, "=", model[var])
else:
    print("UNSAT")
