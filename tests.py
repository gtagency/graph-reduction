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

import hillclimb
import simulatedannealing
import sampleGraph

# PICK YOUR STARTING MATRIX
# matrix = matrix7
matrix = matrix26

randSolution = getRandom(matrix.vertices)
for x in range(9):
    newRand = getRandom(matrix.vertices)
    if score(matrix, newRand) > score(matrix, randSolution):
        randSolution = newRand

# FOR SIMU ANNEALIN, UNCOMMENT FIRST LINE.
# FOR HILL CLIMBING, UNCOMMENT SECOND LINE.
# FOR BOTH UNCOMMENT BOTH
solution, fScore = simulatedannealing.simulateanneal(matrix, randSolution)
# solution, score, tries = hillclimb.climbhill(matrix, randSolution)

# FOR BOTH COMMENT OUT BOTH ABOVE, UNCOMMENT THESE TWO BELOW
# solution, fScore = simulatedannealing.simulateanneal(matrix, randSolution)
# solution, score, tries = hillclimb.climbhill(matrix, solution)

diagnose(matrix, randSolution)
diagnose(matrix, solution)

viz.display(matrix, randSolution)
viz.display(matrix, solution)
