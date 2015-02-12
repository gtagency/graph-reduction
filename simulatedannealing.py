

def expSchedule(t):
    T0 = 5.0
    alpha = 0.5
    return T0 * (alpha ** t)

def linearSchedule(t):
    T0 = 1.0
    alpha = 0.01
    return T0 - (alpha * t)

def simulateanneal(matrix, solution, schedule=expSchedule, maxTries=10000):
    current = solution
    for t in range(maxTries):
        T = schedule(t)
        
