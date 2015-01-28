import json

# in the future, will be the actual input graph.
sampleInput = json.loads(open("sampleInput.json").read())['sample']

# in the future, will be the current attempted solution.
sampleSolution = json.loads(open("format.json").read())

def getEdgeLength(edge):
    # edge is a tuple, taken from input.
    firstX = sampleSolution[edge[0]][0]
    firstY = sampleSolution[edge[0]][1]
    secondX = sampleSolution[edge[1]][0]
    secondY = sampleSolution[edge[1]][1]

    return ((firstY - secondY)**2 + (firstX - secondX))**(0.5)

def getEdgeVariance(solution):
    edgeLengths = []

    # go through upper triangular matrix, to visit all edges
    for i in xrange(0, (len(sampleInput) - 1)):
        currentRow = sampleInput[i]
        for j in xrange((i + 1), len(currentRow)):
            if currentRow[j] == 1:
                # edge found.
                edge = (chr(65 + i), chr(65 + j))
                edgeLengths.append(getEdgeLength(edge))

    return edgeLengths

print getEdgeVariance(sampleSolution)
