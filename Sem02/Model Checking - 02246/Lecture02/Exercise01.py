from z3 import *

# Number of satellites
satellite = [[Bool(f'sat_{i}_{j}') for j in range(4)] for i in range(4)]

s = Solver()

# Rows
for i in range(4):
    s.add(Or([satellite[i][j] for j in range(4)]))
    for j in range(4):
        for k in range(j + 1, 4):
            s.add(Not(And(satellite[i][j], satellite[i][k])))

# Columns
for j in range(4):
    s.add(Or([satellite[i][j] for i in range(4)]))
    for i in range(4):
        for k in range(i + 1, 4):
            s.add(Not(And(satellite[i][j], satellite[k][j])))

# Diagonals
for d in range(7):
    diag1 = []
    diag2 = []
    for i in range(4):
        for j in range(4):
            if i + j == d:
                diag1.append(satellite[i][j])
            if i - j == d - 3:
                diag2.append(satellite[i][j])
    for i in range(len(diag1)):
        for j in range(i + 1, len(diag1)):
            s.add(Not(And(diag1[i], diag1[j])))
    for i in range(len(diag2)):
        for j in range(i + 1, len(diag2)):
            s.add(Not(And(diag2[i], diag2[j])))

if s.check() == sat:
    model = s.model()
    grid = [['.' for _ in range(4)] for _ in range(4)]
    for i in range(4):
        for j in range(4):
            if model.evaluate(satellite[i][j]):
                grid[i][j] = 'S'
    for row in grid:
        print(' '.join(row))
else:
    print("No solution found")
