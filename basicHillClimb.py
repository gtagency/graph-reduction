from calcFinalScore import *
from utils.MatrixPrototypes import *
import random
import math

# So, good news is that this very basic attempt is finished.
# I'd like to run it with more iterations, but there are too many local maxima.
# it usually hits a local max after about 250 iterations.
# Current highscore: 38.585079763757406 (after 362 iterations)
# (the highest i ever got randomly was 19).

def basicHillClimb(matrix, solution, maxAttempts=2000):
    score = calcFinalScore(matrix, solution)
    tries = 0
    peak = False
    while((tries < maxAttempts) and (peak == False)):
#        if(tries % 100 == 0):
#            print(score)
        newScore = hillClimbHelper(matrix, solution, score)
        if(newScore == score):
            peak = True
        score = newScore
        tries += 1
    return solution, score, tries

def getSuccessors(solution):
    successors = []

    for key in solution.keys():
        successorOne = solution
        successorTwo = solution
        successorThree = solution
        successorFour = solution

        successorOne[key] = (successorOne[key][0] + 1, successorOne[key][1])
        successorTwo[key] = (successorTwo[key][0] - 1, successorTwo[key][1])
        successorThree[key] = (successorThree[key][0], successorThree[key][1] + 1)
        successorFour[key] = (successorFour[key][0], successorFour[key][1] - 1)

        successors.extend([successorOne, successorTwo, successorThree, successorFour])

    return successors

def hillClimbHelper(matrix, solution, score):
    for key in solution.keys():
        solution[key] = (solution[key][0] + 1, solution[key][1])
        newScore = calcFinalScore(matrix, solution)
        if(newScore > score):
            return newScore
        else:
            solution[key] = (solution[key][0] - 2, solution[key][1])
            newScore = calcFinalScore(matrix, solution)
            if(newScore > score):
                return newScore
            else:
                solution[key] = (solution[key][0] + 1, solution[key][1])
        solution[key] = (solution[key][0], solution[key][1] + 1)
        newScore = calcFinalScore(matrix, solution)
        if(newScore > score):
            return newScore
        else:
            solution[key] = (solution[key][0], solution[key][1] - 2)
            newScore = calcFinalScore(matrix, solution)
            if(newScore > score):
                return newScore
            else:
                solution[key] = (solution[key][0], solution[key][1] + 1)
    return calcFinalScore(matrix, solution)

def simulatedAnnealing(matrix, solution, schedule=expSchedule, maxTries=10000):
    current = solution
    for t in range(maxTries):
        T = schedule(t)
        if (t % 10 == 0):
            print("Time: " + str(t) + ", Temp: " + str(T))
        if T == 0:
            return current
        nextState = random.choice(getSuccessors(solution))
        deltaE = calcFinalScore(matrix, nextState) - calcFinalScore(matrix, current)
        if deltaE > 0:
            current = nextState
        else:
            if random.random() < math.exp(deltaE / T):
                current = nextState
    return current


def expSchedule(t):
    T0 = 1.0
    alpha = 0.9
    return T0 * (alpha ** t)

if __name__=='__main__':
    import sampleGraph
    import randomPermutation
    print(simulatedAnnealing(sampleGraph.matrix, randomPermutation.points))
