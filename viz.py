import matplotlib.pyplot as plt
import networkx as nx

def show(matrix, points):
   nx.draw(matrix.graph(), points)
   plt.show()
