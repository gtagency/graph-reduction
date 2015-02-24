import networkx as nx

class AdjacencyMatrix:

    # This is the class constructor
    # Arguments:
    #   vertexCount:integer represents the number of vertices in the graph
    def __init__(self, vertexCount):
        self.order = vertexCount
        self.matrix = [[None for i in range(vertexCount)] for i in range(vertexCount)]
        self.vertices = []
        self.numEdges = 0

    def graph(self):
        G = nx.Graph()
        G.add_nodes_from(self.vertices)
        for u,v in self.getEdgeIterator():
            G.add_edge(u, v)
        return G

    def getNumEdges(self):
        return self.numEdges

    # Get vertices
    # Returns:
    #   list of vertices
    def vertices(self):
        return self.vertices

    # Adds vertices to the vertex list
    # newVertices:list of objects
    def addVertices(self, newVertices):
        for newVertex in newVertices:
            if not newVertex in self.vertices and len(self.vertices) < self.order:
                self.vertices.append(newVertex)

    # Adds an edge to the Adjacency Matrix
    # Arguments:
    #   fromVertex:string the name of the vertex this edge connects from
    #   toVertex:string the name of the vertex this edge connects to
    #   weight:integer an optional weight for the edge
    def addEdge(self, fromVertex, toVertex, weight=1):
        i = self.vertices.index(fromVertex)
        j = self.vertices.index(toVertex)
        self.matrix[i][j] = weight
        self.matrix[j][i] = weight
        self.numEdges += 1

    # Gets any edges between the two vertices
    # Arguments:
    #   fromVertex:string the name of the vertex this edge connects from
    #   toVertex:string the name of the vertex this edge connects to
    # Returns:
    #   None if this edge does not exist
    #   Otherwise, an integer weight
    def getEdge(self, fromVertex, toVertex):
        i = self.vertices.index(fromVertex)
        j = self.vertices.index(toVertex)

        return self.matrix[i][j]

    # Returns an item.
    # Necessary to access the matrix with the form matrix[i]
    # when outside the class, such as inside one of the iterators
    # Arguments:
    #   i:the element index desired
    # Returns:
    #   Array of the edges connected (or not) to vertex of index i
    def __getitem__(self, i):
        return self.matrix[i]

    # Returns:
    #   Iterator for the matrix
    def getIterator(self):
        return MatrixIterator(self)

    # Returns:
    #   Iterator for the edges of the graph
    def getEdgeIterator(self):
        return EdgeIterator(self)


class MatrixIterator:

    def __init__(self, matrix):
        self.matrix = matrix
        self.i = self.j = 0

    def __iter__(self):
        return self

    def next(self):
        if self.j < self.matrix.order:
            return self.matrix[self.i][self.j]
        else:
            self.i += 1
            self.j = 0
            return self.matrix[self.i][self.j]

# This iterator provides the existent edges of a graph in the form of a tuple
class EdgeIterator:

    def __init__(self, matrix):
        self.vertices = matrix.vertices
        self.matrix = matrix
        self.i = 0
        self.j = 1

    def __iter__(self):
        return self

    def next(self):
        if self.j < self.matrix.order:
            self.j += 1
            if self.matrix[self.i][self.j - 1] != None:
                return (self.vertices[self.i], self.vertices[self.j - 1])
            else:
                return next(self)
        elif self.i < self.matrix.order - 1:
            self.i += 1
            self.j = self.i + 1
            if self.j < self.matrix.order:
                self.j += 1
                if self.matrix[self.i][self.j - 1] != None:
                    return (self.vertices[self.i], self.vertices[self.j - 1])
                else:
                    return next(self)
            else:
                raise StopIteration
        else:
            raise StopIteration
