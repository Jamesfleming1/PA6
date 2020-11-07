# Here we will actually run the robot. This means putting it somewhere in the maze
# having it decide its moves
# and then creating a model and running filtering algorithm
from random import randrange
from RobotModel import RobotModel
class RunRobot:
    # Must pass in a filename to run everything and then either a moveLimit if you want moves to be randomly generate
    # or just straight pass in the moves list. 
    # Sensor readings will be generated from these moves depending on where they actually move the robot
    def __init__(self, mazeFileName, moveLimit = 0, moves = None, initialPos = None):
        self.model = RobotModel(mazeFileName)

        self.initialPos = initialPos
        self.moveLimit = moveLimit
        self.moves = moves
        if (not initialPos):
            self.initialPos = self.randomlyPlaceRobot()
        if (not moves):
            self.moves = self.generateMoves(moveLimit)
        
            
    



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
        choices = ["N", "W", "S", "E"]
        moves = []
        for x in range(moveLimit):
            random.choice(choices)
            
    

    # generate a color sequence based on the moves the robot has made 
    def generateColorSequence(self, initial, moves):
        pass

    def displayDistribution(self, distribution):
        pass

    def Results(self):
        pass

   
    """
    def animate_path(self, path):
        # reset the robot locations in the maze
        self.maze.robotloc = tuple(self.start_state)

        for state in path:
            print(str(self))
            self.maze.robotloc = tuple(state)
            sleep(1)

            print(str(self.maze))
    """

if __name__ == "__main__":
    r1 = RunRobot("maze1.maz", moveLimit = 3)
    print(r1.initialPos)
    