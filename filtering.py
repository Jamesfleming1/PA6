import numpy.matlib
import numpy as np



#
# filtering
# Takes a sequence of sensor readings, a prior assumption, and a model
def filter(sequence, prior, model):
    # go through every value in the given sequence 
    estimates = []
    currentStateEstimate = prior
    for observation in sequence:
        #based on given observation we should have a particular matrix for that
        # which gives us our "update values" or our sensor model
        updateMatrix = model.updateMatrices[observation]
        

    
        # warning matrix multiplication is not associative!!! Order matters don't mess this up
        currentStateEstimate = normalize(createUpdateMatrix(color)*(transitionMatrix*currentStateEstimate))
        estimates.append(currentStateEstimate)
    return estimates


 def animate_path(self, path):
        # reset the robot locations in the maze
        self.maze.robotloc = tuple(self.start_state)

        for state in path:
            print(str(self))
            self.maze.robotloc = tuple(state)
            sleep(1)

            print(str(self.maze))