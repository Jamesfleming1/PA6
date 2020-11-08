from time import sleep
import random
# Maze.py
#  original version by db, Fall 2017
# Modified by James Fleming Fall 2020

# Maze has floor spaces covered with a letter representing a color


class Maze:

    # internal structure:
    #   self.walls: set of tuples with wall locations
    #   self.width: number of columns
    #   self.rows

    def __init__(self, mazefilename, observableColors):
        self.observableColors = observableColors
        #random.seed(1)
        
        self.robotloc = []
        # read the maze file into a list of strings
        f = open(mazefilename)
        lines = []
        for line in f:
            line = line.strip()
            # ignore blank limes
            if len(line) == 0:
                pass
            elif line[0] == "\\":
                #print("command")
                # there's only one command, \robot, so assume it is that
                parms = line.split()
                x = int(parms[1])
                y = int(parms[2])
                self.robotloc.append(x)
                self.robotloc.append(y)
            else:
                lines.append(line)
        f.close()

        self.width = len(lines[0])
        self.height = len(lines)

        self.map = list("".join(lines))
        # here is where we will colorize the map if not already colored 
        for i in range(len(self.map)):
            if (self.map[i]=='.'):
                # Randomly assign from the observable colors. 
                self.map[i] = random.choice(self.observableColors)
                

    def updateRobotMap(self, newRoboloc):
        self.robotloc = newRoboloc

    def index(self, x, y):
        return (self.height - y - 1) * self.width + x


    # returns True if the location is a floor
    def is_floor(self, x, y):
        if x < 0 or x >= self.width:
            return False
        if y < 0 or y >= self.height:
            return False

        return self.map[self.index(x, y)] != "#"


    # returns color of square if it is a floor, returns None if this was not a proper entry or wall
    def get_color(self, x, y):
        if (self.is_floor(x,y)):
            return self.map[self.index(x,y)]
        else:
            return None



    


    # function called only by __str__ that takes the map and the
    #  robot state, and generates a list of characters in order
    #  that they will need to be printed out in.
    def create_render_list(self):
        #print(self.robotloc)
        renderlist = list(self.map)

        robot_number = 0
        for index in range(0, len(self.robotloc), 2):

            x = self.robotloc[index]
            y = self.robotloc[index + 1]

            renderlist[self.index(x, y)] = renderlist[self.index(x,y)].capitalize()

            robot_number += 1

        return renderlist



    def __str__(self):

        # render robot locations into the map
        renderlist = self.create_render_list()

        # use the renderlist to construct a string, by
        #  adding newlines appropriately

        s = ""
        for y in range(self.height - 1, -1, -1):
            for x in range(self.width):
                s+= renderlist[self.index(x, y)]

            s += "\n"

        return s


def robotchar(robot_number):
    return chr(ord("A") + robot_number)


# Some test code

if __name__ == "__main__":
  pass