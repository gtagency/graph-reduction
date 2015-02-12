import random
import sampleGraph

def getRandom(vertices=sampleGraph.matrix.vertices):
    return {vertex : (random.randrange(10*len(vertices)), 
    random.randrange(10*len(vertices))) for vertex in vertices}
