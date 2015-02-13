from __future__ import division
from utils.MatrixPrototypes import *
import math

def getEdgeLength(solution, edge):
    # edge is a tuple, taken from input.
    firstX = solution[edge[0]][0]
    firstY = solution[edge[0]][1]
    secondX = solution[edge[1]][0]
    secondY = solution[edge[1]][1]

    return ((firstY - secondY)**2 + (firstX - secondX)**2)**(0.5)

def getEdgeLengthScore(solution, matrix, diagonal, desiredDist=10):
    lengthDiffs = []
    edgeNum = 0
    for edge in matrix.getEdgeIterator():
        edgeNum += 1
        lengthDiffs.append(math.fabs(desiredDist - getEdgeLength(solution, edge)))
    maxSumPossible = edgeNum * math.fabs(desiredDist - diagonal)

    return 1 - sum(lengthDiffs) / maxSumPossible
