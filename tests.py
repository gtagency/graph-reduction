from utils.MatrixPrototypes import *
from score import score, diagnose
from utils import viz
from randomPermutation import getRandom

matrix7 = AdjacencyMatrix(7);
matrix7.addVertices(["A", "B", "C", "D", "E", "F", "G"])
matrix7.addEdge("D", "A")
matrix7.addEdge("D", "F")
matrix7.addEdge("D", "B")
matrix7.addEdge("B", "C")
matrix7.addEdge("B", "E")
matrix7.addEdge("F", "G")

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

matrix26 = AdjacencyMatrix(26)
matrix26.addVertices(["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O"])
matrix26.addEdge("A", "J")
matrix26.addEdge("A", "K")
matrix26.addEdge("J", "I")
matrix26.addEdge("I", "H")
matrix26.addEdge("I", "C")
matrix26.addEdge("I", "E")
matrix26.addEdge("K", "L")
matrix26.addEdge("B", "D")
matrix26.addEdge("C", "D")
matrix26.addEdge("C", "O")
matrix26.addEdge("L", "O")
matrix26.addEdge("L", "F")
matrix26.addEdge("O", "G")
matrix26.addEdge("E", "N")
matrix26.addEdge("G", "H")
matrix26.addEdge("D", "M")
matrix26.addEdge("M", "F")

matrix8 = AdjacencyMatrix(8)
matrix8.addVertices(["A", "B", "C", "D", "E", "F", "G", "H"])
matrix8.addEdge("A", "B")
matrix8.addEdge("A", "C")
matrix8.addEdge("A", "E")
matrix8.addEdge("B", "F")
matrix8.addEdge("B", "D")
matrix8.addEdge("C", "D")
matrix8.addEdge("C", "G")
matrix8.addEdge("E", "F")
matrix8.addEdge("E", "G")
matrix8.addEdge("H", "F")
matrix8.addEdge("H", "G")
matrix8.addEdge("H", "D")

matrix21 = AdjacencyMatrix(21)
matrix21.addVertices(["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U"])
matrix21.addEdge("A", "B")
matrix21.addEdge("A", "C")
matrix21.addEdge("A", "D")
matrix21.addEdge("A", "E")
matrix21.addEdge("B", "F")
matrix21.addEdge("B", "G")
matrix21.addEdge("B", "H")
matrix21.addEdge("B", "I")
matrix21.addEdge("C", "J")
matrix21.addEdge("C", "K")
matrix21.addEdge("C", "L")
matrix21.addEdge("C", "M")
matrix21.addEdge("D", "N")
matrix21.addEdge("D", "O")
matrix21.addEdge("D", "P")
matrix21.addEdge("D", "Q")
matrix21.addEdge("E", "R")
matrix21.addEdge("E", "S")
matrix21.addEdge("E", "T")
matrix21.addEdge("E", "U")

import hillclimb
import simulatedannealing
import sampleGraph

# PICK YOUR STARTING MATRIX
# matrix = matrix7
matrix = matrix26
# matrix = matrix8
# matrix = matrix21

randSolution = getRandom(matrix.vertices)

# FOR HILL CLIMBING, UNCOMMENT FIRST LINE.
# FOR SIMU ANNEALIN, UNCOMMENT SECOND LINE.
# solution, score, tries = hillclimb.climbhill(matrix, randSolution)
solution, fScore = simulatedannealing.simulateanneal(matrix, randSolution)

print "Random Solution"
diagnose(matrix, randSolution)
print "Final Solution"
diagnose(matrix, solution)

viz.display(matrix, randSolution)
viz.display(matrix, solution)
