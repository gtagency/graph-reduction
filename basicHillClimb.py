from calcFinalScore import *
from utils.MatrixPrototypes import *

# So, good news is that this very basic attempt is finished.
# I'd like to run it with more iterations, but there are too many local maxima.
# it usually hits a local max after about 250 iterations.
# Current highscore: 32.656044771142 (after 320 iterations)
# (the highest i ever got randomly was 19).

def basicHillClimb(matrix, solution, maxAttempts=1000):
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


def hillClimbHelper(matrix, solution, score):
    for key in solution.keys():
        solution[key] = (solution[key][0] + 1, solution[key][1])
        if(calcFinalScore(matrix, solution) > score):
            return calcFinalScore(matrix, solution)
        else:
            solution[key] = (solution[key][0] - 2, solution[key][1])
            if(calcFinalScore(matrix, solution) > score):
                return calcFinalScore(matrix, solution)
            else:
                solution[key] = (solution[key][0] + 1, solution[key][1])
        solution[key] = (solution[key][0], solution[key][1] + 1)
        if(calcFinalScore(matrix, solution) > score):
            return calcFinalScore(matrix, solution)
        else:
            solution[key] = (solution[key][0], solution[key][1] - 2)
            if(calcFinalScore(matrix, solution) > score):
                return calcFinalScore(matrix, solution)
            else:
                solution[key] = (solution[key][0], solution[key][1] + 1)
    return calcFinalScore(matrix, solution)

if __name__=='__main__':
    import sampleGraph
    import randomPermutation
    print(basicHillClimb(sampleGraph.matrix, randomPermutation.points)[1:3])
