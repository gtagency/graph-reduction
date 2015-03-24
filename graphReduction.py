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
    from score import diagnose
    if (len(sys.argv) < 2):
        print("Example: ")
        matrix = AdjacencyMatrix(12)
        matrix.addVertices(["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L"])
        matrix.addEdge("A", "B")
        matrix.addEdge("B", "C")
        matrix.addEdge("C", "D")
        matrix.addEdge("D", "A")
        matrix.addEdge("E", "F")
        matrix.addEdge("F", "G")
        matrix.addEdge("G", "H")
        matrix.addEdge("H", "E")
        matrix.addEdge("I", "J")
        matrix.addEdge("J", "K")
        matrix.addEdge("K", "L")
        matrix.addEdge("L", "I")
        matrix.addEdge("A", "E")
        matrix.addEdge("B", "F")
        matrix.addEdge("C", "G")
        matrix.addEdge("D", "H")
        matrix.addEdge("E", "I")
        matrix.addEdge("F", "J")
        matrix.addEdge("G", "K")
        matrix.addEdge("H", "L")
        randSolution = getRandom(matrix.vertices)
        solution, fScore = simulatedannealing.simulateanneal(matrix, randSolution)

        print "Random Solution"
        diagnose(matrix, randSolution)

        print "Final Solution"
        diagnose(matrix, solution)

        try:
            import networkx
            import matplotlib
            viz.display(matrix, solution)
        except ImportError:
            print("Need networkx and matplotlib to display graph.")
    else:
        matrix = sys.argv[1]
        newMatrix = resolveMatrix(matrix)
        simAnneal = True
        startSolution = True
        printFlag = False
        solution = graphReduction(newMatrix)
        try:
            import networkx
            import matplotlib
            viz.display(matrix, solution)
        except ImportError:
            print("Need networkx and matplotlib to display graph.")
    #for arg in sys.argv:
