from utils.MatrixPrototypes import *
from evals import *

# Calculates and returns the score of the solution, given a matrix.
def score(matrix, solution, percentComplete=1.0):
    areaM = 0.2
    edgeVarM = 0.7
    edgeDistM = 1
    intersM = 1.7
    edgeLenM = 0.1
    overlapM = 0.5 * percentComplete

    areaScore, diagonal = area.area(solution)
    areaScore = areaM * areaScore
    edgeVarScore = edgeVarM * edgeLengthVariance.getEdgeVariance(solution, matrix, diagonal)
    edgeDistScore = edgeDistM * checkDistributedEdges.checkDistributedEdges(matrix, solution)
    intersectScore = intersM * intersections.score(matrix, solution)
    edgeLenScore = edgeLenM * shrinkEdgesToTen.getEdgeLengthScore(solution, matrix, diagonal, 12)
    overlapScore = overlapM * (0.8 ** checkOverlappingPoints.checkOverlappingPoints(matrix, solution))

    return (areaScore + edgeVarScore + edgeDistScore + intersectScore + edgeLenScore + overlapScore) / (areaM + edgeVarM + edgeDistM + intersM + edgeLenM + overlapM)

def diagnose(matrix, solution):
    areaM = 0.2
    edgeVarM = 0.5
    edgeDistM = 1
    intersM = 1.7
    edgeLenM = 0.1
    overlapM = 0.5

    areaScore, diagonal = area.area(solution)
    areaScore = areaM * areaScore
    edgeVarScore = edgeVarM * edgeLengthVariance.getEdgeVariance(solution, matrix, diagonal)
    edgeDistScore = edgeDistM * checkDistributedEdges.checkDistributedEdges(matrix, solution)
    intersectScore = intersM * intersections.score(matrix, solution)
    edgeLenScore = edgeLenM * shrinkEdgesToTen.getEdgeLengthScore(solution, matrix, diagonal, 12)
    overlapScore = overlapM * (0.8 ** checkOverlappingPoints.checkOverlappingPoints(matrix, solution))

    print "== DIAGNOSIS =="
    print "areaScore: ", areaScore, " / ", areaM
    print "edgeVarScore: ", edgeVarScore, " / ", edgeVarM
    print "edgeDistScore: ", edgeDistScore, " / ", edgeDistM
    print "intersectScore: ", intersectScore, " / ", intersM
    print "edgeLenScore: ", edgeLenScore, " / ", edgeLenM
    print "overlapScore: ", overlapScore, " / ", overlapM

    print "FINAL SCORE: ", (areaScore + edgeVarScore + edgeDistScore + intersectScore + edgeLenScore + overlapScore) / (areaM + edgeVarM + edgeDistM + intersM + edgeLenM + overlapM)
    print "\n"
