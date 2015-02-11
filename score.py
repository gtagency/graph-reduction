from utils.MatrixPrototypes import *
from evals import *

# Calculates and returns the score of the solution, given a matrix.
# Assumes that there are no overlapping points.
def score(matrix, solution):
    areaScore, diagonal = area.area(solution)
    edgeVarScore = edgeLengthVariance.getEdgeVariance(solution, matrix, diagonal)
    edgeDistScore = checkDistributedEdges.checkDistributedEdges(matrix, solution)
    intersectScore = intersections.score(matrix, solution)

    print "Area: ", areaScore # done
    print "EdgeVar: ", edgeVarScore # done
    print "EdgeDist: ", edgeDistScore # done
    print "Intersect: ", intersectScore # TODO: fix intersect. it's outputting true when it shouldn't

    return areaScore + edgeVarScore + edgeDistScore + intersectScore
