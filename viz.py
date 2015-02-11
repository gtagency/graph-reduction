from matplotlib.pyplot import show, ion
import networkx as nx

def display(matrix, points):
   nx.draw(matrix.graph(), points)
   show()
