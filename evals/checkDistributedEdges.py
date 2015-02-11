import math
from utils import utils
from utils.MatrixPrototypes import *

#the smaller the result, the more evenly distributed the angles
#of the edges on the nodes are.

#expects matrix to be a Adjacency Matrix object, and vertices to be a dict of
#coords (coords stored as tuples, keys have same name as vertices)
#
# returns a num between 0 and 1 -> 1 is most fit, 0 is least fit
def checkDistributedEdges(matrix, vertices):
    tupleList = []
    for edge in matrix.getEdgeIterator():
        tupleList.append(edge)
    totalVariance = 0.0
    for key, coords in vertices.items():
        edges = []
        angles = []
        angleDist = []
        #find connecting nodes
        for a, b in tupleList:
            if (a == key):
                edges.append(vertices[b])
            elif (b == key):
                edges.append(vertices[a])
        #find angles from current node to connecting nodes
        if (len(edges) > 1):

            for node in edges:
                x = node[0] - coords[0]
                y = node[1] - coords[1]
                angle = math.atan2(y, x)
                angles.append(angle)

            #find angles between edges
            angles = sorted(angles)
            i = len(angles) - 1
            totalAng = 0
            while i > 0:
                angleDist.append(angles[i] - angles[i - 1])
                i = i - 1
            angleDist.append((2 * math.pi) - (angles[len(angles) - 1] - angles[0]))

            #calc variance
            totalVariance += utils.variance(angleDist)

    return 1.0 - totalVariance

#Test statement, need to import randomPermutation, sampleGraph to run
#
#print (checkDistributedEdges(sampleGraph.matrix, randomPermutation.points))
