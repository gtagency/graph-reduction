import sys
import json
from utils.MatrixPrototypes import *
from randomPermutation import getRandom

def graphReduction(matrix, simAnneal=True, startSolution=None, printFlag=False):
    if startSolution == None:
        startSolution = getRandom(matrix.vertices)
    if simAnneal:
        solution, fScore = simulatedannealing.simulateanneal(matrix, randSolution, printFlag)
    else:
        solution, fScore, tries = hillclimb.climbhill(matrix, solution)
    return solution




if __name__=='__main__':
    from utils import viz
    if (len(sys.argv) < 2):
        print "idiot"
    else:
        matrix = sys.argv[1]
        if (isinstance(matrix, list) and isinstance(matrix[0], list) and len(matrix[i]) == len(matrix) for i in range(len(matrix)) ):
            newMatrix = AdjacencyMatrix(len(matrix))
            newMatrix.vertices = [range(len(matrix))]
            newMatrix.matrix = matrix
        elif not isinstance(matrix, AdjacencyMatrix):
            try:
                matrix = open(matrix)
                doubleArray =json.load(matrix)
            except ValueError:
                try:
                    doubleArray = json.loads(matrix)
                except Exception:
                    raise Exception("Invalid input")
            if not (isinstance(doubleArray, list) and isinstance(doubleArray[0], list) and len(doubleArray[i]) == len(doubleArray) for i in range(len(doubleArray))):
                raise Exception("Invalid Matrix")
            newMatrix = AdjacencyMatrix(len(doubleArray))
            newMatrix.vertices = [range(len(doubleArray))]
            newMatrix.matrix = matrix
        else:
            newMatrix = matrix
        simAnneal = True
        startSolution = True
        printFlag = False
        solution = graphReduction(newMatrix)
        viz.display(matrix, solution)
    #for arg in sys.argv:
