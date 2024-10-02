from z3 import *

solver = Solver()
routers = ['r1', 'r2', 'r3', 'r4', 'r5', 'r6', 'r7']
destinations = ['d110', 'd120', 'd130', 'd140', 'dOther']
level = {
    'r1': 0,  # Highest level
    'r2': 1,  # Second level
    'r3': 1,
    'r4': 2,  # Lowest level
    'r5': 2,
    'r6': 2,
    'r7': 2
}

# Clusters
cluster = {
    'r1': 'C1',
    'r2': 'C2',
    'r3': 'C3',
    'r4': 'C2',
    'r5': 'C2',
    'r6': 'C3',
    'r7': 'C3'
}

# VLANs
serving = {
    'r4': 'd110',
    'r5': 'd120',
    'r6': 'd130',
    'r7': 'd140'
}

# Send variables
send = {}
for s in routers:
    for d in destinations:
        for r in routers:
            var_name = f'send_{s}_{d}_{r}'
            send[(s, d, r)] = Bool(var_name)

# Constraint (i): No router should send a packet to itself unless it serves the destination VLAN
for s in routers:
    for d in destinations:
        if serving.get(s) == d:
            solver.add(send[(s, d, s)] == True)
            for r in routers:
                if r != s:
                    solver.add(send[(s, d, r)] == False)

# Constraint (ii): Consistent routing in the same cluster and level for destinations neither router serves
for s1 in routers:
    for s2 in routers:
        if s1 != s2 and cluster[s1] == cluster[s2] and level[s1] == level[s2]:
            for d in destinations:
                if serving.get(s1) != d and serving.get(s2) != d:
                    for r in routers:
                        solver.add(send[(s1, d, r)] == send[(s2, d, r)])

# Constraint (iii): Traffic directed to an address in a different cluster is forwarded to a router that stays higher in the hierarchy
  # First Level
for s in routers:
    if level[s] == 2:
        C_a = cluster[s]
        for d in destinations:
            C_b = None
            for router, vlan in serving.items():
                if vlan == d:
                    C_b = cluster[router]
                    break
            if d == 'dOther':
                C_b = 'other'
            if C_a != C_b and C_b != 'other':
                allowed_receivers = [r for r in routers if level[r] == 1 and cluster[r] == C_a]
                if allowed_receivers:
                    solver.add(Or([send[(s, d, r)] for r in allowed_receivers]))
                else:
                    solver.add(False)

  # Second Level
for s in routers:
    if level[s] == 1:  # L2
        C_a = cluster[s]
        for d in destinations:
            C_b = None
            for router, vlan in serving.items():
                if vlan == d:
                    C_b = cluster[router]
                    break
            if d == 'dOther':
                C_b = 'other'
            if C_a != C_b and C_b != 'other':
                solver.add(send[(s, d, 'r1')] == True)
                for r in routers:
                    if r != 'r1':
                        solver.add(send[(s, d, r)] == False)

solver.add(send[('r2', 'd110', 'r4')])
solver.add(Or(send[('r2', 'd120', 'r4')] , send[('r2', 'd120', 'r5')]))
# solver.add(send[('r2', 'd130', 'r6')]) # Violation of constraint here. Could be removed, as the catch-all rule will handle the case correctly
for des in [d for d in destinations if d not in ["d110", "d120"]]:
    solver.add(send[('r2', des, 'r1')])

solver.add(send[('r4', 'd120', 'r2')], send[('r4', 'd120', 'r5')])
solver.add(send[('r4', 'd130', 'r3')])
solver.add(send[('r4', 'd110', 'r4')]) # Add this rule to satisfy the constraint
for des in [d for d in destinations if d not in ["d120", "d130", "d110"]]:  # Fixed for loop
# for des in [d for d in destinations if d not in ["d120", "d130"]]: # The catch all rule violates the constraint
    solver.add(send[('r4', des, 'r1')])

solver.add(send[('r6', 'd140', 'r3')], send[('r6', 'd140', 'r7')])
# solver.add(send[('r6', 'd130', 'r1')]) # Violates the constraint
solver.add(send[('r6', 'd130', 'r6')]) # Corrected
for des in [d for d in destinations if d not in ["d130", "d140"]]:
    solver.add(send[('r6', des, 'r3')])


result = solver.check()
if result == sat:
    print(solver.assertions())
    print("SAT")
    model = solver.model()
    number_of_correct_routes = 0
    for s in routers:
        for d in destinations:
            for r in routers:
                var = send[(s, d, r)]
                res = model.evaluate(var)
                if is_true(res):
                    print(f"result: {res}  {s} sends packets to destination {d} to router {r}")
                    number_of_correct_routes += 1
    print(f"Number of correct routes: {number_of_correct_routes}")
else:
    print("UNSAT")