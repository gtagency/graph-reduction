import json
import utils.utils
from MatrixPrototypes import *

def getEdgeLength(solution, edge):
    # edge is a tuple, taken from input.
    firstX = sampleSolution[edge[0]][0]
    firstY = sampleSolution[edge[0]][1]
    secondX = sampleSolution[edge[1]][0]
    secondY = sampleSolution[edge[1]][1]

    return ((firstY - secondY)**2 + (firstX - secondX)**2)**(0.5)


def getEdgeVariance(solution, matrix):
    lengths = [getEdgeLength(solution, edge) for edge in matrix.getEdgeIterator() if edge != None]
    return utils.variance(lengths)



### TESTING PURPOSES ONLY ###
# in the future, will be the actual input graph.
sampleInput = json.loads(open("sampleInput.json").read())['sample']

# in the future, will be the current attempted solution.
sampleSolution = json.loads(open("format.json").read())

# testing everything here
myMatrix = AdjacencyMatrix(4)
myMatrix.addVertices(["A", "B", "C", "D"])
myMatrix.addEdge("A", "B")
myMatrix.addEdge("A", "D")
myMatrix.addEdge("B", "D")
myMatrix.addEdge("C", "D")

print getEdgeVariance(sampleSolution, myMatrix)
