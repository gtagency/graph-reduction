import sampleGraph
import randomPermutation

def intersections(graph, coords):
    lines = []
    int_points = []
    lines = [(coords[edge[0]], coords[edge[1]]) for edge in
        graph.getEdgeIterator() if edge is not None]
    i = 0
    for l in lines:
        for l2 in lines:
            if l is l2: pass
            r, p = intersect(l, l2)
            if r and p not in int_points:
                i += 1
                int_points.append(p)
    return i

def intersect(l, k):
    a,c = slopeIntForm(l)
    b,d = slopeIntForm(k)
    if a is b or c is None or d is None: return (False, None)
    p = [(d-c)/(a-b), (a*d - b*c)/(a-b)]
    for q in (l+ k):
        if dist(p, q) < 2: return (False, None)
    
    return (True, p)

def slopeIntForm(line):
    p, o = line
    m = float("inf") if p[0] == o[0] else abs(p[1] - o[1])/abs(p[0] - o[0])
    return (m, None if p[0] == o[0] else m*(0 - p[0]) + p[1])

def dist(p1, p2):
    return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**0.5

print(intersections(sampleGraph.matrix, randomPermutation.points))
