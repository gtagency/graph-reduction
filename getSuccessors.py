import math

def getSuccessors(solution, temperature):
    maxDist = 10*len(solution.keys())
    dist = int(math.ceil((temperature*maxDist)/(10)))
    if dist < 1: dist = 1

    successors = []

    for key in solution.keys():
        for i in range(dist):
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

def getSuccessorsHill(solution, dist=1):
    successors = []

    for key in solution.keys():
        sOne = dict(solution)
        sTwo = dict(solution)
        sThree = dict(solution)
        sFour = dict(solution)

        sOne[key] = ((solution[key][0] + dist), (solution[key][1]))
        sTwo[key] = ((solution[key][0] - dist), (solution[key][1]))
        sThree[key] = ((solution[key][0]), (solution[key][1] + dist))
        sFour[key] = ((solution[key][0]), (solution[key][1] - dist))

        successors.extend([sOne, sTwo, sThree, sFour])

    return successors
