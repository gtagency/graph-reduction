import randomPermutation

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
    return (xMax-xMin)*(yMax-yMin)

print(area(randomPermutation.points))
