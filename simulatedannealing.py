from getSuccessors import getSuccessors
from score import *
from random import random, choice
import math

def expSchedule(t):
    T0 = 5.0
    alpha = 0.9995
    return T0 * (alpha ** t)

def linearSchedule(t):
    T0 = 5.0
    alpha = 0.0005
    return T0 - (alpha * t)

def simulateanneal(matrix, solution, schedule=linearSchedule, maxTries=10000):
    current = dict(solution)
    best = dict(solution)
    cScore = score(matrix, solution)
    bScore = score(matrix, solution)
    jumps = 0

    for t in range(maxTries):
        T = schedule(t)
        successors = getSuccessors(current, T)
        neighbor = choice(successors)
        neighborScore = score(matrix, neighbor)

        if (t % 100 == 0): print "Time: ", t, ", Temp: ", T, ", bScore: ", bScore, ", cScore: ", cScore, ", jumps: ", jumps, ", deltaE: ", (neighborScore - cScore), ", chance: ", math.exp((neighborScore - cScore) / (0.1 * T)), ", suc: ", len(successors)

        if neighborScore > cScore:
            current = dict(neighbor)
            cScore = neighborScore
            if neighborScore > bScore:
                best = dict(neighbor)
                bScore = neighborScore
        elif random() < math.exp((neighborScore - cScore) / (0.0006 * T)):
            jumps += 1
            current = dict(neighbor)
            cScore = neighborScore
    if bScore > cScore: return best, bScore
    else: return current, cScore
