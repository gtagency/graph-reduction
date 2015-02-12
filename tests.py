from utils.MatrixPrototypes import *
from score import score, diagnose
from utils import viz
from randomPermutation import getRandom

matrix = AdjacencyMatrix(7);
matrix.addVertices(["A", "B", "C", "D", "E", "F", "G"])
matrix.addEdge("D", "A")
matrix.addEdge("D", "F")
matrix.addEdge("D", "B")
matrix.addEdge("B", "C")
matrix.addEdge("B", "E")
matrix.addEdge("F", "G")

goodSolution = {
    "A": (5, 10),
    "B": (15, 15),
    "C": (20, 20),
    "D": (10, 10),
    "E": (20, 15),
    "F": (15, 5),
    "G": (20, 10)
}

badSolution = {
    "A": (10, 5),
    "B": (5, 15),
    "C": (20, 20),
    "D": (10, 25),
    "E": (20, 10),
    "F": (15, 5),
    "G": (15, 15)
}

import hillclimb

import sampleGraph

matrix = sampleGraph.matrix

randSolution = getRandom(matrix.vertices)
solution, score, tries = hillclimb.climbhill(matrix, randSolution)

diagnose(matrix, randSolution)
diagnose(matrix, solution)

viz.display(matrix, randSolution)
viz.display(matrix, solution)
