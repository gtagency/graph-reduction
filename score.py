from utils.MatrixPrototypes import *
from evals import *

# Calculates and returns the score of the solution, given a matrix.
def score(matrix, solution):
    areaM = 0.2
    edgeVarM = 0.7
    edgeDistM = 1
    intersM = 1.7
    edgeLenM = 0.1

    areaScore, diagonal = area.area(solution)
    areaScore = areaM * areaScore
    edgeVarScore = edgeVarM * edgeLengthVariance.getEdgeVariance(solution, matrix, diagonal)
    edgeDistScore = edgeDistM * checkDistributedEdges.checkDistributedEdges(matrix, solution)
    intersectScore = intersM * intersections.score(matrix, solution)
    edgeLenScore = edgeLenM * shrinkEdgesToTen.getEdgeLengthScore(solution, matrix, diagonal, 12)

    return (areaScore + edgeVarScore + edgeDistScore + intersectScore + edgeLenScore) / (areaM + edgeVarM + edgeDistM + intersM + edgeLenM)

def diagnose(matrix, solution):
    areaM = 0.2
    edgeVarM = 0.5
    edgeDistM = 1
    intersM = 1.7
    edgeLenM = 0.1

    areaScore, diagonal = area.area(solution)
    areaScore = areaM * areaScore
    edgeVarScore = edgeVarM * edgeLengthVariance.getEdgeVariance(solution, matrix, diagonal)
    edgeDistScore = edgeDistM * checkDistributedEdges.checkDistributedEdges(matrix, solution)
    intersectScore = intersM * intersections.score(matrix, solution)
    edgeLenScore = edgeLenM * shrinkEdgesToTen.getEdgeLengthScore(solution, matrix, diagonal, 12)

    print "== DIAGNOSIS =="
    print "areaScore: ", areaScore
    print "edgeVarScore: ", edgeVarScore
    print "edgeDistScore: ", edgeDistScore
    print "intersectScore: ", intersectScore
    print "edgeLenScore: ", edgeLenScore
    print "FINAL SCORE: ", (areaScore + edgeVarScore + edgeDistScore + intersectScore + edgeLenScore) / (areaM + edgeVarM + edgeDistM + intersM + edgeLenM)
    print "\n"
