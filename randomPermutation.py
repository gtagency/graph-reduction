import random
import sampleGraph

vertices = sampleGraph.matrix.vertices
points = {vertex : (random.randrange(10*len(vertices)), 
    random.randrange(10*len(vertices))) for vertex in vertices}
