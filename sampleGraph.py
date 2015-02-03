from utils.MatrixPrototypes import *

matrix = AdjacencyMatrix(26)
matrix.addVertices(["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"])
matrix.addEdge("A", "J")
matrix.addEdge("A", "K")
matrix.addEdge("J", "I")
matrix.addEdge("I", "H")
matrix.addEdge("I", "C")
matrix.addEdge("I", "E")
matrix.addEdge("K", "L")
matrix.addEdge("B", "D")
matrix.addEdge("C", "D")
matrix.addEdge("C", "O")
matrix.addEdge("L", "O")
matrix.addEdge("L", "F")
matrix.addEdge("O", "G")
matrix.addEdge("E", "N")
matrix.addEdge("G", "H")
matrix.addEdge("D", "M")
matrix.addEdge("M", "F")
