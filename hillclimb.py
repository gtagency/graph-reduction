from score import *
from utils.MatrixPrototypes import *
from random import random, shuffle
from utils import viz
from getSuccessors import getSuccessors, getSuccessorsHill
import math

def climbhill(matrix, solution, maxAttempts=2000):
    for tries in range(maxAttempts):
        neighbors = getSuccessorsHill(solution, 1)
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
