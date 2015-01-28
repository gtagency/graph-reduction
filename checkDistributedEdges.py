import json
import math
import statistics

#the smaller the result, the more evenly distributed the angles of the edges on the nodes are.
#expects graph edges to be a list of tuples, and vertices to be a JSON obj containing a dict of coords
def checkDistributedEdges(tupleList, vertices):
    vertices = json.loads(vertices)
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
            
            #num = len(angleDist)
            #mean = (2 * math.pi) / num
            #variance = 0
            #for angle in angleDist:
            #    variance += ((angle - mean) ** 2) / num
            totalVariance += statistics.variance(angleDist)
        
    return totalVariance

#test code

#testVertices = {
#    "A": [15, 15],
#    "B": [20, 10],
#    "C": [10, 10],
#    "D": [15, 25]
#}
#testVertices = json.dumps(testVertices)
#testTuples = [("A", "C"), ("B", "C"), ("D", "A"), ("B", "D")]
#print(checkDistributedEdges(testTuples, testVertices))
