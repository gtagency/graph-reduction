from score import *
from utils.MatrixPrototypes import *
from random import random, shuffle
from utils import viz
import math

def climbhill(matrix, solution, maxAttempts=2000):
    for tries in range(maxAttempts):
        neighbors = getSuccessors(solution, 1)
        shuffle(neighbors)
        initialScore = currentScore = score(matrix, solution)

        if tries % 100 == 0: print "partial score: ", currentScore, tries # DEBUG

        for step in neighbors:
            nextScore = score(matrix, step)
            if nextScore > currentScore:
                solution = step
                currentScore = nextScore

        if initialScore == currentScore: break
    return solution, currentScore, tries

def getSuccessors(solution, dist=1):
    successors = []

    for key in solution.keys():
        successorOne = dict(solution)
        successorTwo = dict(solution)
        successorThree = dict(solution)
        successorFour = dict(solution)

        successorOne[key] = ((solution[key][0] + dist), (solution[key][1]))
        successorTwo[key] = ((solution[key][0] - dist), (solution[key][1]))
        successorThree[key] = ((solution[key][0]), (solution[key][1] + dist))
        successorFour[key] = ((solution[key][0]), (solution[key][1] - dist))

        successors.extend([successorOne, successorTwo, successorThree, successorFour])

    return successors
