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
    return (xMax-xMin)*(yMax-yMin), math.sqrt((xMax-xMin)**2 + (yMax-yMin)**2)

if __name__=='__main__':
    print(area(randomPermutation.points))
