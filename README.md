# PrettyGraphs

Make your graphs pretty and user-friendly using simulated annealing and hill climbing. Just input the vertices and the edges which connect them, and PrettyGraphs will output the position of the vertices such that the graph is visually pleasant.

How It Works
------------
//how simu and hill climbing works.

### Quick Demo
To see the algorithms in action, simply run:
```
$ python tests.py
```
The algorithm will output the various states the graph goes through and then display two graphs: a randomly generated one (used as the initial state) and the final generated one.

You can also modify which demo you are visualizing by going to the bottom of the `tests.py` file and uncommenting different matrices or the algorithm being used (hill climbing or simulated annealing). Just follow the commented instructions.

### Examples
//pics of random and generated.

How To Use It
-------------
Before running the algorithms, you will need a representation of the graph. Thankfully, we provide you with an easy to use one.
```
from utils.MatrixPrototypes import AdjacencyMatrix, MatrixIterator, EdgeIterator
```
Now you instantiate an AdjacencyMatrix and add vertices and edges to it.
```
matrix = AdjacencyMatrix(numberOfVertices)
matrix.addVertices(["Name", "Of", "Each", "Vertex"])
matrix.addEdges("Name", "Of") # now edges 'Name' and 'Of' are connected.
```

//TODO: how to use the thing, like make your own matrix and how to run the hill climbing and simu annealing algo. How to display the final result and visualize it. Depends a lot on rob's work right now.

How To Tweak It
---------------
Different graphs will require different weights for the heuristics in the score function. If you want to modify these weihts, it can easily be done. Just go into the `score.py` file and modify the weights there. Be sure to also modify the weights in the diagnose function, if you're using it.

How To Contribute To It
-----------------------
### How To Add Heuristics
You can add heuristics to the score function. Just create a python file that takes in an AdjacencyMatrix and/or a proposed solution and outputs a normalized value from 0 to 1. Add this file to `/evals` and add its name to `/evals/__init__.py`. Now you can modify the score function to take it into account. Remember to normalize the final score by adding the maxValue to the bottom of the division in the return statement. The maxValue of your heuristi should be its weight, if the score your file outputs is properly normalized.


