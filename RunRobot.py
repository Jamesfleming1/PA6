# Here we will actually run the robot. This means putting it somewhere in the maze
# having it decide its moves
# and then creating a model and running filtering algorithm
from Maze import Maze
from RobotModel import RobotModel
class RunRobot:
    def __init__(self, mazeFileName):
        self.maze = Maze(mazeFileName)
        self.posToColor = {}
        self.coloredMaze = colorMaze()



    # Create an ascii representation of the maze and build a dictionary that has key of location with value of its color

    def colorMaze(self):
        
        pass

 def animate_path(self, path):
        # reset the robot locations in the maze
        self.maze.robotloc = tuple(self.start_state)

        for state in path:
            print(str(self))
            self.maze.robotloc = tuple(state)
            sleep(1)

            print(str(self.maze))
