import math
from utils.MatrixPrototypes import *

def checkOverlappingPoints(matrix, solution, GAP=10):
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


    edges = [vertTuple for vertTuple in matrix.getEdgeIterator()]
    for pt in vertexList:
        for edge in edges:
            if (pt != edge[0] and pt != edge[1]):
                dist = pnt2line(solution[pt], solution[edge[0]], solution[edge[1]])
                if (dist != None and dist < GAP):
                    numFailures += ((GAP / (dist + 0.001)) - 0.999)

    return numFailures;

def pnt2line(pnt, start, end):
    line_vec = vector(start, end)
    pnt_vec = vector(start, pnt)
    line_len = length(line_vec)
    if (line_len == 0.0):
        return None
    line_unitvec = unit(line_vec)
    pnt_vec_scaled = scale(pnt_vec, 1.0/line_len)
    t = dot(line_unitvec, pnt_vec_scaled)

    # in these cases the point is closer to another point and is already
    # accounted for above in the point to point comparison.
    if t < 0.0:
        return None
    elif t > 1.0:
        return None

    nearest = scale(line_vec, t)
    dist = distance(nearest, pnt_vec)
    return dist


# Vector fns needed for pointEdgeOverlap

def dot(v,w):
    x,y = v
    X,Y = w
    return x*X + y*Y

def length(v):
    x,y = v
    return math.sqrt(x*x + y*y)

def vector(b,e):
    x,y = b
    X,Y = e
    return (X-x, Y-y)

def unit(v):
    x,y = v
    mag = length(v)
    if (mag == 0):
        return (0, 0)
    return (x/mag, y/mag)

def distance(p0,p1):
    return length(vector(p0,p1))

def scale(v,sc):
    x,y = v
    return (x * sc, y * sc)

def add(v,w):
    x,y = v
    X,Y = w
    return (x+X, y+Y)
