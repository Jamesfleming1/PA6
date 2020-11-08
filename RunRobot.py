# Here we will actually run the robot. This means putting it somewhere in the maze
# having it decide its moves
# and then creating a model and running filtering algorithm
from random import randrange
from random import choice
from random import random
from time import sleep
from RobotModel import RobotModel
from filtering import filter
class RunRobot:
    # Must pass in a filename to run everything and then either a moveLimit if you want moves to be randomly generate
    # or just straight pass in the moves list. 
    # Sensor readings will be generated from these moves depending on where they actually move the robot
    def __init__(self, mazeFileName, moveLimit = 0, moves = [], initialPos = ()):
        self.model = RobotModel(mazeFileName)

        self.initialPos = initialPos
        self.moveLimit = moveLimit
        self.moves = moves
        if (not initialPos):
            self.initialPos = self.randomlyPlaceRobot()
        if (not moves):
            self.moves = self.generateMoves(moveLimit)

        # generateColorSequence will find our actual path and the corresponding colorSequence 
        # This will tell us based on randomized moves, where did the robot actually go and what colors did its sensor read
        self.colorSequence, self.path  = self.generateColorSequence(self.initialPos, self.moves)
        
            
    # Pick a random location in the maze and return it
    def randomlyPlaceRobot(self):
        x = -1
        y = -1
        # keep going until we find a random position in maze that is not a wall
        # should not take long at all
        while( not self.model.maze.is_floor(x,y)):
            x = randrange(self.model.maze.width)
            y = randrange(self.model.maze.height)

        return (x,y)


    # generate a random list of moves
    def generateMoves(self, moveLimit):
        # The four directions a robot can make
        choices = ["N", "W", "S", "E"]
        # a list to hold the moves we make
        moves = []
        for x in range(moveLimit):
            # with uniform distribution choose to move in one of the four directions
            moves.append(choice(choices))
        return moves
            
    

    # generate a color sequence based on the moves the robot has made
    # References the maze of the model to see what color a square actually is in order to what color the sensor would get 
    def generateColorSequence(self, initial, moves):

        colorSequence = []
        path = []
        # Create a dictionary to relate a letter symbol to how it would actually affect a robots move
        moveToCoordinate = {"N": (0,1), "W": (-1, 0), "S": (0, -1), "E": (1,0)}
        currentPos = initial
        for move in moves:
            posChange = moveToCoordinate[move]
            # create an attempted move 
            # elementwise tuple addition
            attemptedMove = currentPos[0] + posChange[0], currentPos[1] + posChange[1]
            # If our attempted move brings us to a floor
            if (self.model.maze.is_floor(attemptedMove[0], attemptedMove[1])):
                # updated the currentPos
                currentPos = attemptedMove
            # add currentPos to path
            path.append(currentPos)
             # add the sensor reading to colorSequence
            colorSequence.append(self.sensorReading(currentPos))



        return colorSequence, path

    # takes in a position and returns a sensor reading based on color robot is actually on
    # probabilities of sensor reading are given by the problem
    def sensorReading(self, position):
        xCoord = position[0]
        yCoord = position[1]
        colorAtPos = self.model.maze.get_color(xCoord, yCoord)
        # create a copy of observable colors
        colors = self.model.observableColors.copy()
        # remove the color we are at
        colors.remove(colorAtPos)
        
        f = random()
        # if it is larger than the 0.88 threshold pick the color we are actually on
        if (f <= 0.88):
            return colorAtPos
        else:
            # else with uniform randomness pick the wrong color
            # 0.12 percent chance this happens. 3 options so each has 0.04 chance of being picked. (0.333333 * 0.12 = 0.04) 
            return choice(colors)
        
    # given a distribution, display it 
    def displayDistribution(self, distribution):
        # iterate through the maze by row
        s=''
        for y in range(self.model.maze.height-1, -1 ,-1):
            for x in range(self.model.maze.width):
                
                # grab index using basic algebra. Remember the distribution is a column vector ordered  low to high(x,y) in terms of  x and then y value as a tie breakerr
                index = x*self.model.maze.height + y
                percent = distribution[index]*100
                if (percent < 10):
                    s+="0" + ("%.2f" % percent)
                else:
                    s+= ("%.2f" % percent)

                s+= " "
            s+='\n'
        print(s)


        

    # Run filtering on the model. Display the filtering results alongside the robots actual moves 
    def displayResults(self):
        # call filtering
        distributions = filter(self.colorSequence, self.model)

        print(" \n The Robot Started at " + str(self.initialPos))
        print("The location of the Robot is designated by a capital letter. The color of the tile is designated by the letter")
        print("This is what the maze looks like before any moves or sensor readings")
        self.model.maze.robotloc = self.initialPos
        print(self.model.maze)
        print("The distribution of where the robot currently thinks it is as follows ")
        self.displayDistribution(self.model.prior)

        #sleep(1)
        for i in range(len(self.path)):
            print("The robot moves " + self.moves[i])
            currentLoc = self.path[i]

            print("At the location of " + str(currentLoc) + "the robot gets a sensor reading of " + self.colorSequence[i])
            self.model.maze.robotloc = currentLoc

            print("The maze currently looks like:")
            print(self.model.maze)
            print("The distribution of where the robot currently thinks it is as follows ")
            self.displayDistribution(distributions[i])
            #sleep(3)
   
   
if __name__ == "__main__":
    r1 = RunRobot("maze1.maz", moveLimit = 4)
    
    #print(r1.initialPos)

    #print(r1.moves)
    print(r1.model.maze)
    print(r1.model.maze.map)

    #print(r1.path)
    #print(r1.colorSequence)
    