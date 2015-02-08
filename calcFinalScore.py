from utils.MatrixPrototypes import *
from evals import *
#import area
#import edgeLengthVariance
#from checkDistributedEdges import *
#import intersections

def calcFinalScore(matrix, solution):
    # still need to implement the "check if nodes are too close" test

    # each score is weighted in order of importance
    # feel free to change weights, this is just a rough estimate of how
    # important different scores are
    areaScore, diagonal = area.area(solution)
    areaScore = 100 * (len(solution) / areaScore)
    edgeVarianceScore = 30 * edgeLengthVariance.getEdgeVariance(solution, matrix, diagonal)
    distEdgeScore = 15 * checkDistributedEdges.checkDistributedEdges(matrix, solution)
    intersectionsScore = 55 * intersections.score(matrix, solution)

    return areaScore + edgeVarianceScore + distEdgeScore + intersectionsScore

if __name__=='__main__':
    import sampleGraph
    import randomPermutation
    print(calcFinalScore(sampleGraph.matrix, randomPermutation.points))
