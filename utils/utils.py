from __future__ import division
# returns aritmetic mean of a list of numbers
def avgMean(data):
    return sum(data) / len(data)

# returns standard deviation of a list of numbers
def stdev(data):
    return variance(data)**0.5

# returns variance of a list of numbers
def variance(data):
    mean = avgMean(data)
    sqdiff = [(elem - mean)**2 for elem in data]
    return avgMean(sqdiff)
