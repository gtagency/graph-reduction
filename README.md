# PrettyGraphs

Make your graphs pretty and user-friendly using simulated annealing and hill climbing. Just input the vertices and the edges which connect them, and PrettyGraphs will output the position of the vertices such that the graph is visually pleasant.

How It Works
============
//how simu and hill climbing works.

Quick Demo
----------
To see the algorithms in action, simply run:
```
$ python tests.py
```
The algorithm will output the various states the graph goes through and then display two graphs: a randomly generated one (used as the initial state) and the final generated one.

You can also modify which demo you are visualizing by going to the bottom of the `tests.py` file and uncommenting different matrices or the algorithm being used (hill climbing or simulated annealing).

Examples
--------
//pics of random and generated.

How To Use It
=============
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


//how to use the thing, like make your own matrix and how to run the hill climbing and simu annealing algo. How to display the final result and visualize it

How To Tweak It
===============

Different graphs will require different weights for the heuristics in the score function. If you want to modify these weihts, it can easily be done.

How To Contribute To It
=======================


