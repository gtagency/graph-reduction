import math

def getSuccessors(solution, temperature):
    maxDist = 10*len(solution.keys())
    dist = (temperature*maxDist)/(10)

    successors = []

    for key in solution.keys():
        for i in range(int(math.ceil(dist))):
            sOne = dict(solution)
            sTwo = dict(solution)
            sThree = dict(solution)
            sFour = dict(solution)
            sFive = dict(solution)
            sSix = dict(solution)
            sSeven = dict(solution)
            sEight = dict(solution)

            newSuccessors = []

            if (solution[key][0] + i) < maxDist:
                sOne[key] = ((solution[key][0] + i), (solution[key][1]))
                newSuccessors.append(sOne)
                if (solution[key][1] + i) < maxDist:
                    sFive[key] = ((solution[key][0] + i), (solution[key][1] + i))
                    newSuccessors.append(sFive)
                if (solution[key][1] - i) > 0:
                    sEight[key] = ((solution[key][0] + i), (solution[key][1] - i))
                    newSuccessors.append(sEight)

            if (solution[key][0] - i) > 0:
                sTwo[key] = ((solution[key][0] - i), (solution[key][1]))
                newSuccessors.append(sTwo)
                if (solution[key][1] + i) < maxDist:
                    sSix[key] = ((solution[key][0] - i), (solution[key][1] + i))
                    newSuccessors.append(sSix)
                if (solution[key][1] - i) > 0:
                    sSeven[key] = ((solution[key][0] - i), (solution[key][1] - i))
                    newSuccessors.append(sSeven)

            if (solution[key][1] + i) < maxDist:
                sThree[key] = ((solution[key][0]), (solution[key][1] + i))
                newSuccessors.append(sThree)
            if (solution[key][1] - i) > 0:
                sFour[key] = ((solution[key][0]), (solution[key][1] - i))
                newSuccessors.append(sFour)

            successors.extend(newSuccessors)

    return successors
