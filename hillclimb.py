from score import *
from utils.MatrixPrototypes import *
from random import random, shuffle
from utils import viz
from getSuccessors import getSuccessors, getSuccessorsHill
import math

def climbhill(matrix, solution, printFlag=True, maxAttempts=2000):
    for tries in range(maxAttempts):
        neighbors = getSuccessorsHill(solution, 1)
        shuffle(neighbors)
        initialScore = currentScore = score(matrix, solution)
        if printFlag:
            if tries % 1 == 0: print "partial score: ", currentScore, " tries: ", tries

        for step in neighbors:
            nextScore = score(matrix, step)
            if nextScore > currentScore:
                solution = step
                currentScore = nextScore

        if initialScore == currentScore: break
    return solution, currentScore, tries
