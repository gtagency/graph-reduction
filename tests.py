from utils.MatrixPrototypes import *
from score import score
from utils import viz

matrix = AdjacencyMatrix(7);
matrix.addVertices(["A", "B", "C", "D", "E", "F", "G"])
matrix.addEdge("D", "A")
matrix.addEdge("D", "F")
matrix.addEdge("D", "B")
matrix.addEdge("B", "C")
matrix.addEdge("B", "E")
matrix.addEdge("F", "G")

goodSolution = {
    "A": [5, 10],
    "B": [15, 15],
    "C": [20, 20],
    "D": [10, 10],
    "E": [20, 15],
    "F": [15, 5],
    "G": [20, 10]
}

badSolution = {
    "A": [10, 5],
    "B": [5, 15],
    "C": [20, 20],
    "D": [10, 25],
    "E": [20, 10],
    "F": [15, 5],
    "G": [15, 15]
}

print "Good"
fscore = score(matrix, goodSolution)
print "Final Score: ", fscore, "\n"
print "Bad"
fscore = score(matrix, badSolution)
print "Final Score: ", fscore, "\n"


# TODO : fix intersect. it's not working.
from evals import intersections

goodLineOne = (goodSolution["A"], goodSolution["D"])
goodLineTwo = (goodSolution["B"], goodSolution["E"])
badLineOne = (badSolution["A"], badSolution["D"])
badLineTwo = (badSolution["B"], badSolution["E"])

print "Should be False"
print intersections.intersect(goodLineOne, goodLineTwo)
print "Should be Truec"
print intersections.intersect(badLineOne, badLineTwo)
