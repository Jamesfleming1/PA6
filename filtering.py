import numpy.matlib
import numpy as np
from model import model
from RobotModel import RobotModel
#
# filtering
# Takes a sequence of sensor readings, and a model
def filter(sequence, model):
    distributions = []
    # get the prior matrix from model 
    currentStateEstimate = model.prior
    # go through every value in the given sequence 
    for observation in sequence:
        #based on given observation we should have a particular matrix for that
        # which gives us our "update values"
        updateMatrix = model.updateMatrixDictionary[observation]
        # calculate a new current State estimate    
        # warning matrix multiplication is not associative!!! Order matters don't mess this up
        currentStateEstimate = normalize(np.dot(updateMatrix, np.dot(model.transitionMatrix, currentStateEstimate)))
        distributions.append(currentStateEstimate)
    return distributions


def normalize(matrix):
    # Normalize a matrix of probabilities. An incoming maxtrix will have values in the form of P(x|b)/a if we take a marginal distribution over our matrix
    # because these are all conditional probabilities given b occured. The sum of all the probabilities will be 1. so sum(P(x|b)/a) for all values of x
    # will be 1/a.. Therefore we can multiply every term by a to get just P(x|b) which is our state estimate P(some location | give a sequence of readings)

    normalizeMatrix = (1/(matrix.sum())) * matrix 
    return normalizeMatrix


if __name__ == "__main__":
    # Test normalize function
    # Compare these to example in lecture 22 filtering examples
    pre = np.array([0.45, 0.1])
    #print(pre)
    #print(normalize(pre))

    pre = np.array([[0.565], [0.075]])
    #print(pre)
    #print(normalize(pre))

    # Nice it works. 
    # Lets test our filter algorithm on the umbrella problem
    #updateMatrix 
    prior = np.array([[0.5] ,[0.5]])
    
    prior = np.array([0.5, 0.5])
    #print(prior)
    prior = prior.T
    #print(prior)
    #print(prior.shape)
    
    

    #print(prior)
    transitionMatrix = np.array([[0.7,0.3], [0.3,0.7]])
    # U represents we saw an umbrella, #NU represents we didnt 
    updateDict = {"U": np.array([[0.9, 0], [0, 0.2]])}

    
    #, "NU":np.dot(np.array([0.1,0.8]), np.identity(2)) }
    #print(updateDict["U"])
    UmbrellaModel = model(prior,transitionMatrix, updateDict)
    sequence = ["U", "U"]
    distributions = filter(sequence, UmbrellaModel)
    print(distributions)
    # In fact this does give us the correct distributions for day 1 and day 2 of the umbrella
    # after seeing the umbrella twice. Now the challenge is how do we build these same datastructures
    # for the matrix robot program. 

    #r1 = RobotModel("maze1.maz")
    #print(r1.maze)
    #sequences = ["y", "y", "g", "r"]
   # print(filter(sequences, r1)[3])
    # nice with random seed 1 set in maze we can run this ans see that
    # we will get a distribution that puts the robot in some sensible places. 




