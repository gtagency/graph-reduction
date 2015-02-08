from calcFinalScore import *
from utils.MatrixPrototypes import *

# So, good news is that this very basic attempt is finished.
# Bad news is that there are so many local maxima that this doesn't fare much
# better than getting a random permutation. Back of the envelope estimate, it
# returns solutions with score about 3-4 points higher on average than random
# permutation does on average. Although that may be because the current scoring
# system is very strict. Current high score: 15.0061484094

def basicHillClimb(matrix, solution):
    score = calcFinalScore(matrix, solution)
    tries = 0
    while(tries < 10000000):
        newSol = hillClimbHelper(matrix, solution, score)
        if(newSol == solution):
            tries = 1000000000
        solution = newSol
        score = calcFinalScore(matrix, solution)
        tries += 1
    return solution, score


def hillClimbHelper(matrix, solution, score):
    for key in solution.keys():
        solution[key] = (solution[key][0] + 1, solution[key][1])
        if(calcFinalScore(matrix, solution) > score):
            return solution
        else:
            solution[key] = (solution[key][0] - 2, solution[key][1])
            if(calcFinalScore(matrix, solution) > score):
                return solution
            else:
                solution[key] = (solution[key][0] + 1, solution[key][1])
        solution[key] = (solution[key][0], solution[key][1] + 1)
        if(calcFinalScore(matrix, solution) > score):
            return solution
        else:
            solution[key] = (solution[key][0], solution[key][1] - 2)
            if(calcFinalScore(matrix, solution) > score):
                return solution
            else:
                solution[key] = (solution[key][0], solution[key][1] + 1)
    return solution

if __name__=='__main__':
    import sampleGraph
    import randomPermutation
    print(basicHillClimb(sampleGraph.matrix, randomPermutation.points)[1])
