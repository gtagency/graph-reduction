from utils.MatrixPrototypes import *
from evals import *

# Calculates and returns the score of the solution, given a matrix.
# Assumes that there are no overlapping points.
def score(matrix, solution):
    areaScore, diagonal = area.area(solution)
    areaScore = 1.5 * areaScore
    edgeVarScore = 2 * edgeLengthVariance.getEdgeVariance(solution, matrix, diagonal)
    edgeDistScore = checkDistributedEdges.checkDistributedEdges(matrix, solution)
    intersectScore = intersections.score(matrix, solution)

    return areaScore + edgeVarScore + edgeDistScore + intersectScore
