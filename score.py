from utils.MatrixPrototypes import *
from evals import *

# Calculates and returns the score of the solution, given a matrix.
def score(matrix, solution):
    areaScore, diagonal = area.area(solution)
    areaScore = 1.5 * areaScore
    edgeVarScore = 2 * edgeLengthVariance.getEdgeVariance(solution, matrix, diagonal)
    edgeDistScore = checkDistributedEdges.checkDistributedEdges(matrix, solution)
    intersectScore = intersections.score(matrix, solution)
    edgeLenScore = shrinkEdgesToTen.getEdgeLengthScore(solution, matrix, diagonal, 5)

    return (areaScore + edgeVarScore + edgeDistScore + intersectScore + edgeLenScore) / 6.5

def diagnose(matrix, solution):
    areaScore, diagonal = area.area(solution)
    areaScore = 1.5 * areaScore
    edgeVarScore = 2 * edgeLengthVariance.getEdgeVariance(solution, matrix, diagonal)
    edgeDistScore = checkDistributedEdges.checkDistributedEdges(matrix, solution)
    intersectScore = intersections.score(matrix, solution)
    edgeLenScore = shrinkEdgesToTen.getEdgeLengthScore(solution, matrix, diagonal, 5)

    print "== DIAGNOSIS =="
    print "areaScore: ", areaScore
    print "edgeVarScore: ", edgeVarScore
    print "edgeDistScore: ", edgeDistScore
    print "intersectScore: ", intersectScore
    print "edgeLenScore: ", edgeLenScore
    print "FINAL SCORE: ", (areaScore + edgeVarScore + edgeDistScore + intersectScore + edgeLenScore) / 6.5
    print "\n"
