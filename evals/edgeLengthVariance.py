from utils import utils
from utils.MatrixPrototypes import *
import sampleGraph
import randomPermutation

def getEdgeLength(solution, edge):
    # edge is a tuple, taken from input.
    firstX = solution[edge[0]][0]
    firstY = solution[edge[0]][1]
    secondX = solution[edge[1]][0]
    secondY = solution[edge[1]][1]

    return ((firstY - secondY)**2 + (firstX - secondX)**2)**(0.5)


def getEdgeVariance(solution, matrix, diagonal):
    lengths = [getEdgeLength(solution, edge) for edge in matrix.getEdgeIterator()]
    return -1 * utils.variance(lengths) / utils.variance([0, diagonal])
