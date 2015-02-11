import randomPermutation
import math

def area(coords):
    xMin, yMin = coords['A']
    xMax, yMax = xMin, yMin

    for value in coords.values():
        x, y = value
        if x > xMax:
            xMax = x
        if x <xMin:
            xMin = x
        if y > yMax:
            yMax = y
        if y < yMin:
            yMin = y

    maxArea = 10*len(coords.values()) ** 2
    areaScore = 1 - float((xMax-xMin)*(yMax-yMin)) / maxArea
    diagonal = math.sqrt((xMax-xMin)**2 + (yMax-yMin)**2)

    return areaScore, diagonal
