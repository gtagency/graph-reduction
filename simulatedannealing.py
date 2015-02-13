from getSuccessors import getSuccessors
from score import *
from random import random, choice, randrange
import math

def expSchedule(t):
    T0 = 5.0
    alpha = 0.9995
    return T0 * (alpha ** t)

def linearSchedule(t):
    T0 = 5.0
    alpha = 0.0005
    return T0 - (alpha * t)

def getNeighbor(solution, T):
    neighbor = dict(solution)

    # pick a vertex to move
    vertex = solution.keys()[randrange(len(solution.keys()))]
    # pick a direction to move to (0 is up, 1 is up-right, 2 is right, etc.)
    direction = randrange(8)
    # pick a distance to move it by (based on T)
    maxDist = 10*len(solution.keys())
    dist = int(math.ceil((T*maxDist)/(10)))
    if dist < 1: dist = 1

    # if distance is invalid, return a different neighbor
    # else, move the vertex and return neighbor

    if direction == 0:
        if (solution[vertex][1] + dist) > maxDist: return getNeighbor(solution, T)
        neighbor[vertex] = ((solution[vertex][0]), (solution[vertex][1] + dist))
    if direction == 1:
        if (solution[vertex][0] + dist) > maxDist or (solution[vertex][1] + dist) > maxDist: return getNeighbor(solution, T)
        neighbor[vertex] = ((solution[vertex][0] + dist), (solution[vertex][1] + dist))
    if direction == 2:
        if (solution[vertex][0] + dist) > maxDist: return getNeighbor(solution, T)
        neighbor[vertex] = ((solution[vertex][0] + dist), (solution[vertex][1]))
    if direction == 3:
        if (solution[vertex][0] + dist) > maxDist or (solution[vertex][1] - dist) < 0: return getNeighbor(solution, T)
        neighbor[vertex] = ((solution[vertex][0] + dist), (solution[vertex][1] - dist))
    if direction == 4:
        if (solution[vertex][1] - dist) < 0: return getNeighbor(solution, T)
        neighbor[vertex] = ((solution[vertex][0]), (solution[vertex][1] - dist))
    if direction == 5:
        if (solution[vertex][0] - dist) < 0 or (solution[vertex][1] - dist) < 0: return getNeighbor(solution, T)
        neighbor[vertex] = ((solution[vertex][0] - dist), (solution[vertex][1] - dist))
    if direction == 6:
        if (solution[vertex][0] - dist) < 0: return getNeighbor(solution, T)
        neighbor[vertex] = ((solution[vertex][0] - dist), (solution[vertex][1]))
    if direction == 7:
        if (solution[vertex][0] - dist) < 0 or (solution[vertex][1] + dist) > maxDist: return getNeighbor(solution, T)
        neighbor[vertex] = ((solution[vertex][0] - dist), (solution[vertex][1] + dist))

    return neighbor


def simulateanneal(matrix, solution, schedule=linearSchedule, maxTries=10000):
    current = dict(solution)
    best = dict(solution)
    cScore = score(matrix, solution)
    bScore = score(matrix, solution)
    jumps = 0

    # make maxTries, T's schedule, and everything else really dependent on the NUMBER OF VERTICES.
    for t in range(maxTries):
        T = schedule(t)
        neighbor = getNeighbor(current, T)
        # successors = getSuccessors(current, T)
        # neighbor = choice(successors)
        neighborScore = score(matrix, neighbor)

        if T == 0:
            if (t % 100 == 0): print "Time:", t, "\tTemp:", T, "\tbScore:", bScore, "\tcScore:", cScore, "\tjumps:", jumps, "\tdeltaE:", (neighborScore - cScore)
        else:
            if (t % 100 == 0): print "Time:", t, "\tTemp:", T, "\tbScore:", bScore, "\tcScore:", cScore, "\tjumps:", jumps, "\tdeltaE:", (neighborScore - cScore), "\tchance:", math.exp((neighborScore - cScore) / (0.005*T/5))

        if neighborScore > cScore:
            current = dict(neighbor)
            cScore = neighborScore
            if neighborScore > bScore:
                best = dict(neighbor)
                bScore = neighborScore
        elif T == 0:
            continue
        # elif random() < math.exp((neighborScore - cScore) / (0.0003 * T)):
        elif random() < math.exp((neighborScore - cScore) / (0.0007*T)):
            # elif random() < math.exp((neighborScore - cScore) / (0.0008*T)):
            jumps += 1
            current = dict(neighbor)
            cScore = neighborScore
    if bScore > cScore: return best, bScore
    else: return current, cScore
