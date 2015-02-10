from calcFinalScore import *
from utils.MatrixPrototypes import *

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

        successorOne[key] = (successorOne[key] + 1, successorOne[key])
        successorTwo[key] = (successorTwo[key] - 1, successorTwo[key])
        successorThree[key] = (successorThree[key], successorThree[key] + 1)
        successorFour[key] = (successorFour[key], successorFour[key] - 1)

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

if __name__=='__main__':
    import sampleGraph
    import randomPermutation
    print(basicHillClimb(sampleGraph.matrix, randomPermutation.points)[1:3])
