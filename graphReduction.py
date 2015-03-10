import sys
import json
from utils.MatrixPrototypes import *
from randomPermutation import getRandom
import simulatedannealing

def graphReduction(matrix, simAnneal=True, startSolution=None, printFlag=True):
    matrix = resolveMatrix(matrix)
    if startSolution == None:
        startSolution = getRandom(matrix.vertices)
    if simAnneal:
        solution, fScore = simulatedannealing.simulateanneal(matrix, startSolution, printFlag)
    else:
        solution, fScore, tries = hillclimb.climbhill(matrix, strartSolution)
    return solution, fScore


def resolveMatrix(matrix):
    if (isinstance(matrix, AdjacencyMatrix)):
        newMatrix = matrix
    elif (isinstance(matrix, list) and isinstance(matrix[0], list) and len(matrix[i]) == len(matrix) for i in range(len(matrix)) ):
        newMatrix = AdjacencyMatrix(len(matrix))
        newMatrix.vertices = [range(len(matrix))]
        newMatrix.matrix = matrix
    else:
        try:
            matrix = open(matrix)
            doubleArray =json.load(matrix)
        except ValueError:
            try:
                doubleArray = json.loads(matrix)
            except Exception:
                raise Exception("Invalid Matrix")
        if not (isinstance(doubleArray, list) and isinstance(doubleArray[0], list) and len(doubleArray[i]) == len(doubleArray) for i in range(len(doubleArray))):
            raise Exception("Invalid Matrix")
        newMatrix = AdjacencyMatrix(len(doubleArray))
        newMatrix.vertices = [range(len(doubleArray))]
        newMatrix.matrix = matrix
    return newMatrix

if __name__=='__main__':
    from utils import viz
    if (len(sys.argv) < 2):
        print "Need a matrix"
    else:
        matrix = sys.argv[1]
        newMatrix = resolveMatrix(matrix)
        simAnneal = True
        startSolution = True
        printFlag = False
        solution = graphReduction(newMatrix)
        viz.display(matrix, solution)
    #for arg in sys.argv:
