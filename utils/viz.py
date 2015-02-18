from matplotlib.pyplot import show, ion, axis
import networkx as nx

def display(matrix, points):
    axis((0, 10*len(points.keys()), 0, 10*len(points.keys())))
    nx.draw(matrix.graph(), points)
    show()
