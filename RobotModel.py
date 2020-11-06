from model import model
import numpy.matlib
import numpy as np
from Maze import Maze

class RobotModel(model):
    def __init__(self, moves, mazeFileName):
        self.transitionMatrix = self.createTransitionModel()
        self.maze = Maze(mazeFileName)
        self.prior = self.createPrior()
        self.updateMatrixDictionary = self.createUpdateDictionary
        super().__init__(self.prior, self.transitionMatrix)


    # create a uniform distribution of where the robot can be based on knowledge of map
    def createPrior(self):
        # prior should be a 16x 1 matrix. (n^2 x 1 in the general case)
        # Where each row of the matrix is for a different position in the maze. and the number in column 0 is the probability of being in that position
        # because our rows will now match up with our transition model.
        probabilities = []
        # Go through each position of a maze.
        numFloor = 0 
        for x in range(self.maze.width):
            for y in range(self.maze.height):
                # If this is a floor score it 1
                if (self.maze.is_floor(x,y)):
                    probabilities.append(1)
                    numFloor+=1
                else:
                    #If this is a wall score it 0
                    probabilities.append(0)
        # create a uniform distribution by dividing all scores by the total number of floor spaces
        # a robot could be placed at any floor space with equal probability
        probabilities = np.array(probabilities)
        prior = probabilities * (1/numFloor)
        # make sure to grab the transpose of this row vector. We want it to be a column vector 
        prior = prior.T
        return prior


                
        # Go through each position of a maze. 



    def createTransitionModel(self):
        # a 16 x16 matrix. Where the rows are previous position of robot 
        # columns are current position of robot. Value at  (1,1 ) would be probability robot was at position 1 and is now at position 1
        # position 1 would obviously refer to a tuple maybbe (1,0) for the x and y coordinate of the robtot
        # Tricky!! We are told that the robot will move with a .25 percent probability in any direction
        # Need to remember that there are walls. So if there is a wall the probability that it doesnt move
        # becomes nonzero. Probability it doesn't move becomes sum of all the walls around that position. 

        return []

      def createUpdateMatrixDictionary(self):
        return {}
        # is based of the sensor model. We are given a color. Then we ask what is the probability we got that color from a specific position. 
        # there are 16 or (n^2) positions that the robot could be. And we need a probability of reading color c for each of those positions
        # we want the rows of all our matrices to be the locations of the maze. For the matrix multiplication to work out we need to multiply a 16x1 matrix 
        # which is every row (location in matrix) to a single probability for a given color by the identity matrix of 16 so that we get a 16 x16 where the 
        # diagnols correspond to the probailities and every other entry is 0. We need the information of the maze to tell us this because the robot cannot actually get sensor readings.
    
    
    
    



if __name__ == "__main__":
    # Make sure we get a column vector of 16 with all equal probabilities of 1/16 
    # This is the prior of an empty maze
    r1 = RobotModel([], "emptyMaze.maz")
    print(r1.prior)
    print(r1.prior.shape)
    # Now add a few walls and makes sure we get equal probabilities of 1/13 for the places with no walls and 0 for places with walls

    r1 = RobotModel([], "maze1.maz")
    print(r1.prior)
    print(r1.prior.shape)

    # Looks good, prior function is complete. 