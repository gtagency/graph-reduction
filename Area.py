import json
from pprint import pprint
json_data=open('format.json')

data = json.load(json_data)
#pprint(data)

def Area(coordinates):
    yMax = coordinates['A'][1]
    yMin = coordinates['A'][1]
    xMax = coordinates['A'][0]
    xMin = coordinates['A'][0]
    for value in coordinates.values():
        x = value[0]
        y = value[1]
        if x > xMax:
            xMax = value[0]
        if x <xMin:
            xMin = value[0]
        if y > yMax:
            yMax = value[1]
        if y < yMin:
            yMin = value[1]
#    print ((xMax-xMin)*(yMax-yMin))
    return (xMax-xMin)*(yMax-yMin)
Area(data)
json_data.close()
