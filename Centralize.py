import json
from pprint import pprint

def most_populated_vertex():
    graph = json.load(open("sample.json").read())
    aCheck = get_number_of_vertices(graph["A"])
    bCheck = get_number_of_vertices(graph["B"])
    cCheck = get_number_of_vertices(graph["C"])
    dCheck = get_number_of_vertices(graph["D"])
    maxVal = get_max({aCheck, bCheck, cCheck, dCheck})
    if (maxVal == aCheck):
        return "A"
    if (maxVal == bCheck):
        return "B"
    if (maxVal == cCheck):
        return "C"
    if (maxVal == dCheck):
        return "D"

def get_number_of_vertices(vertex):
    num = 0
    i = 0
    for i in range(len(vertex)):
        if (vertex[i] == 0):
            num = nume + 1;
    return num


def get_max(numArray):
    i = 0;
    maxValue = 0;
    for i in range(len(numArray)):
        if (numArray[i] > maxValue):
            maxValue = numArray[i]
    return maxValue
