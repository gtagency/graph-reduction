class AdjacencyMatrix:
    
    # This is the class constructor
    # Arguments:
    #   vertexCount:integer represents the number of vertices in the graph
    def __init__(self, vertexCount):
        self.order = vertexCount
        self.matrix = [[None for i in range(vertexCount)] for i in range(vertexCount)]
        self.vertices = []
        
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
        
    def getIterator(self):
        return MatrixIterator(self)
        

class MatrixIterator:
    
    def __init__(self, matrix):
        self.matrix = matrix
        self.i = self.j = 0
        
    def getNext(self):
        if self.j < self.matrx.order:
            return self.matrix[self.i][self.j]
        else:
            self.i += 1
            self.j = 0
            return self.matrix[self.i][self.j]
        
        
