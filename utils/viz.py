from matplotlib.pyplot import show, ion, axis
import networkx as nx

def display(matrix, points):
    axis((-5, 10*len(points.keys()) + 5, -5, 10*len(points.keys()) + 5))
    nx.draw(matrix.graph(), points)
    show()
