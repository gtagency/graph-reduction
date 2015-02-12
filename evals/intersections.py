from __future__ import division

def score(graph, coords):
    lines = [(coords[u], coords[v]) for u, v in graph.getEdgeIterator()]
    return 1 - intersections(lines) / max_intersections(len(lines))

def intersections(lines):
    checked_lines = []
    i = 0
    for l in lines:
        checked_lines.append(l)
        for l2 in lines:
            if l2 in checked_lines: continue
            if intersect(l, l2): i += 1
    return i

def onSegment(a, b, c):
    if (b[0] <= max(a[0], c[0]) and b[0] >= min(a[0], c[0]) and
        b[1] <= max(a[1], c[1]) and b[1] >= min(a[1], c[1])):
        return True

    return False

def orientation(a, b, c):
    val = (b[1] - a[1]) * (c[0] - b[0]) - (b[0] - a[0]) * (c[1] - b[1])

    if (val == 0): return 0  # colinear
    return 1 if (val >= 0) else 2 # clock or counterclock wise

def intersect(l, k):
    # if one of the points is repeated, it can't intersect.
    if l[0] == k[0] or l[0] == k[1] or l[1] == k[0] or l[1] == k[1]:
        return False

    o1 = orientation(l[0], l[1], k[0])
    o2 = orientation(l[0], l[1], k[1])
    o3 = orientation(k[0], k[1], l[0])
    o4 = orientation(k[0], k[1], l[1])

    # General Case
    if (o1 != o2 and o3 != o4): return True

    # Special Cases
    # l[0], k[0] and l[1] are colinear and l[1] lies on segment p1q1
    if (o1 == 0 and onSegment(l[0], k[0], l[1])): return True

    # l[0], k[0] and l[1] are colinear and k[1] lies on segment p1q1
    if (o2 == 0 and onSegment(l[0], k[1], l[1])): return True

    # l[1], k[1] and l[0] are colinear and l[0] lies on segment p2q2
    if (o3 == 0 and onSegment(k[0], l[0], k[1])): return True

     # l[1], k[1] and k[0] are colinear and k[0] lies on segment p2q2
    if (o4 == 0 and onSegment(k[0], l[1], k[1])): return True

    return False # Doesn't fall in any of the above cases

def max_intersections(k):
    if k <= 0: return 0
    elif k is 1: return 0
    else: return k - 1 + max_intersections(k - 1)
