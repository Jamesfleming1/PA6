from model import model
import numpy.matlib
import numpy as np
from Maze import Maze

class RobotModel(model):
    def __init__(self, moves, mazeFileName, observableColors=["r", "g", "b", "y"]):
        # Other methods use the maze so make sure it is declared first.
        # 
        self.observableColors = observableColors 
        self.maze = Maze(mazeFileName, observableColors)
    
        self.transitionMatrix = self.createTransitionModel()
        self.prior = self.createPrior()
        self.updateMatrixDictionary = self.createUpdateMatrixDictionary(["r", "g","b", "y"])
        super().__init__(self.prior, self.transitionMatrix, self.updateMatrixDictionary)


    # create a uniform distribution of where the robot can be based on knowledge of maze
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


    # create a transition matrix relating one position in maze to another position.           
    def createTransitionModel(self):
        # a 16 x16 matrix. Where the rows are previous position of robot 
        # columns are current position of robot.

        # Create an empty matrix that is all the positions in the maze by all the positions in the maze
        # how many positions are in the maze?
        numPositions = self.maze.width * self.maze.height
        transitionMatrix = np.zeros(numPositions**2)
        # remember here that the height of a matrix refers to # of rows and width refers to # of columns
        # we will see numerous instances where indexing into a matrix vs (x,y) positions will be tricky
        transitionMatrix = transitionMatrix.reshape((numPositions, numPositions))

        #  Value at  (1,1 ) would be probability robot was at position 1 and is now at position 1

        # position 1 would obviously refer to a tuple maybbe (1,0) for the x and y coordinate of the robtot
        
        # Tricky!! We are told that the robot will move with a .25 percent probability in any direction
        # Need to remember that there are walls. So if there is a wall the probability that it doesnt move
        # becomes nonzero. 


        # Go through every location of the maze. This is our previous position. 
        # see which neighbors are walls vs floors.  Leave walls as assigned 0, neighbor floors get .25
        # the same position gets .25*numOfWallNeighbors
        for x in range(self.maze.width):
            for y in range(self.maze.height):
                
                # Now go through each neighbor of this position if it is not a wall
                if (self.maze.is_floor(x,y)):
                    # Simple algebra can convert a position in the maze to its index in the transition matrix 
                    # Because of how we order the positions of a maze in our matrix equivalent. Current Position (0,0) is row 0 in matrix. Next position of (0,0) would be column 0 in matrix
                    
                    rowIndex = x*self.maze.width + y
                    
                    #keep track of how many neighbors are walls. 
                    numWallNeighbors = 0

                    # go through neighbors of this position(up +-1 and right +-1)
                    for d in ([-1, 1]):
                        xIndex = (x+d)*self.maze.width + y 
                        yIndex = x*self.maze.width + (y+d)
                        if (self.maze.is_floor(x+d, y)):
                            # the probability that we were at a give (x,y) and transitioned to 
                            # (x+d, y) is 0.25 if (x+d, y) is a floor
                            transitionMatrix[rowIndex][xIndex] = 0.25
                        else:
                            numWallNeighbors+=1
                        
                        if (self.maze.is_floor(x,y+d)):
                            transitionMatrix[rowIndex][yIndex] = 0.25
                        else:
                            numWallNeighbors+=1
                    # Now we know how many neighbors are walls so we can assign the probability 
                    # That a robot doesn't actually move to be .25* the number of walls.
                    # For instance if has 3 walls on 3 sides then 75 percent of the time it tries to move
                    # it will just bump into a wall and not actually move
                    transitionMatrix[rowIndex][rowIndex] = .25* numWallNeighbors
        return transitionMatrix


    # create an update matrix that key is color observed a matrix that relates position robot is at to probability key color was observed
    # 
    def createUpdateMatrixDictionary(self, observableColors):
        updateMatrixDictionary ={}
        for color in observableColors:
            for x in range(self.maze.width):
                for y in range(self.maze.height):
                    pass
        return updateMatrixDictionary

        # is based of the sensor model. We are given a color. Then we ask what is the probability we got that color from a specific position. 
        # there are 16 or (n^2) positions that the robot could be. And we need a probability of reading color c for each of those positions
       
        
if __name__ == "__main__":
    # Make sure we get a column vector of 16 with all equal probabilities of 1/16 
    # This is the prior of an empty maze
    r1 = RobotModel([], "emptyMaze.maz")
    #print(r1.prior)
    #print(r1.prior.shape)
    # Now add a few walls and makes sure we get equal probabilities of 1/13 for the places with no walls and 0 for places with walls

    r1 = RobotModel([], "maze1.maz")
    #print(r1.prior)
    #print(r1.prior.shape)

    # Looks good, prior function is complete. 
    startArray = np.identity(4)
    #print(startArray[0][0])
    #print(startArray[3][3])
    # direct array manipulation (remember that x and y are flipped, it takes row , column)
    startArray[2][1] = 1
    #print(startArray[2][1])
    #print(startArray)

    startArray = np.zeros(4*4)
    startArray = startArray.reshape((4,4))
    #print(startArray)
    #print(startArray.shape)
    #print(r1.transitionMatrix)
    #print(r1.transitionMatrix.shape)
    #print(r1.transitionMatrix)
    # Test an play around with different values in the matrix. 
    # Pretty confident our transition matrix is correctly built!
    #print(r1.transitionMatrix[10][5])
    print(r1.maze)



