import random
import sampleGraph

vertices = sampleGraph.matrix.vertices
points = {vertex : (random.randrange(len(vertices)), 
    random.randrange(len(vertices))) for vertex in vertices}
