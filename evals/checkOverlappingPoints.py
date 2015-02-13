import math
from utils.MatrixPrototypes import *

def checkOverlappingPoints(matrix, solution, GAP=12):
    numFailures = 0.0
    vertexList = matrix.vertices
    for i in range(len(vertexList)):
        v1 = vertexList[i]
        for v2 in vertexList[i:]:
            if(v1 != v2):
                x = solution[v1][0] - solution[v2][0]
                y = solution[v1][1] - solution[v2][1]
                if(math.sqrt(x**2 + y**2) < GAP):
                    numFailures += ((GAP / (math.sqrt(x**2 + y**2) + 0.001)) - 0.999)
    return numFailures;
