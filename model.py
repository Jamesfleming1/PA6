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
    def __init__(self, prior, transitionMatrix, updateMatrixDictionary):

        self.prior = prior
        self.transitionMatrix = transitionMatrix
        self.updateMatrixDictionary = updateMatrixDictionary

        


    

  
        

  


    



  



    
    





# What is state transition model
# what is sensor model
# How do i implement the filtering algorithm given that there are several possible values for the state variable
# state is not boolean


# Show distribution after each time step. Also show actual maze and the actual state of robot
# as well as sequences of motions taken


