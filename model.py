# James Fleming PA6 Hidden Markov Models Dartmouth COSC76 Fall 2020

# Physics are same. If tries to move west but there is wall, robot does not move but does not know

# Robot's prior information is a uniform distribution over all the open positions in the maze 
# We know where the walls are so we need a method that creates a prior distribution based on number of free space


# The robot has an inital position. Makes 1 move per step
# chooses a direction uniformly at random North South East West


# there are four colors red green yellow blue
# sensor mostly works. If the robot is in a blue square the probability of receiving evidence b is .88
#but the sensor might also give the evidence r with .04, g with .04 y with .04 and the situation is the same for others

# ie if pb is random variable that is true when robot is on a blue square
# p(pb | b) = .88
import numpy.matlib
import numpy as np

class model:
    def __init__(self, mazefilename, possibleObservations):
        # 
        self.updateMatrices = createUpdateMatrixDictionary()
        


    # create a uniform distribution of where the robot can be based on knowledge of map
    def createPrior(self):
        # prior should be a 16x 1 matrix. (n^2 x 1 in the general case)
        # Where each row of the matrix is for a different position in the maze. and the number in column 0 is the probability of being in that position
        # because our rows will now match up with our transition model. O
        pass

    def createTransitionModel(self):
        # a 16 x16 matrix. Where the rows are previous position of robot 
        # columns are current position of robot. Value at  (1,1 ) would be probability robot was at position 1 and is now at position 1
        # position 1 would obviously refer to a tuple maybbe (1,0) for the x and y coordinate of the robtot
        # Tricky!! We are told that the robot will move with a .25 percent probability in any direction
        # Need to remember that there are walls. So if there is a wall the probability that it doesnt move
        # becomes nonzero. Probability it doesn't move becomes sum of all the walls around that position. 

        pass
        

    def createUpdateMatrixDictionary(self, possibleObservations, possibleStates):
        pass
        # is based of the sensor model. We are given a color. Then we ask what is the probability we got that color from a specific position. 
        # there are 16 or (n^2) positions that the robot could be. And we need a probability of reading color c for each of those positions
        # we want the rows of all our matrices to be the locations of the maze. For the matrix multiplication to work out we need to multiply a 16x1 matrix 
        # which is every row (location in matrix) to a single probability for a given color by the identity matrix of 16 so that we get a 16 x16 where the 
        # diagnols correspond to the probailities and every other entry is 0. We need the information of the maze to tell us this because the robot cannot actually get sensor readings.


    # does the maze need to be randomly colored? I think so right
    # might have to create our own ascii representations of the map
    # all positions are either lower case color (r, g, b, y) or w for wall
    # if robot is in position it becomes (R, G, B, Y)
    def colorMaze(self):
        pass



    def normalize(self, matrix):
        # Normalize a matrix of probabilities. An incoming maxtrix will have values in the form of P(x|b)/a if we take a marginal distribution over our matrix
        # because these are all conditional probabilities given b occured. The sum of all the probabilities will be 1. so sum(P(x|b)/a) for all values of x
        # will be 1/a.. Therefore we can multiply every term by a to get just P(x|b) which is our state estimate P(some location | give a sequence of readings)

        pass



    # create an initial position for the robot to be
    # random selection (maybe this can just be part of create prior )
    def initialPosition(self):
        pass

    # uniformly randomly pick from North South East West to move. 
    def chooseDirection(self):
        pass





# What is state transition model
# what is sensor model
# How do i implement the filtering algorithm given that there are several possible values for the state variable
# state is not boolean


# Show distribution after each time step. Also show actual maze and the actual state of robot
# as well as sequences of motions taken


