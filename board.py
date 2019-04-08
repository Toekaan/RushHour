from car import Car

class Board():
    """
    The board where the game takes place.
    The game is represented by a grid with different chars in it, which represent the cars.
    """
    def __init__(self, width_height, positions, exit_position):       
        # width and height are always the same (starts counting from 0!)
        self.width_height = width_height
        
        # represents the positions of all cars: [[],[]]
        self.positions = positions
        
        # if red car hits the exit position, the game is over: 2.5
        self.exit_position = exit_position   

        # list of all the cars in the grid
        self.cars = []
        

    def bounds(self, pos):
        """ Checks if in bounds
        """

    def passable(self, pos):
        """ Checks if passable
        """
        return pos not in self.cars

    def __str__(self):
        """ Print out board in readable strings
        """
        allowed = ['!', '@', '#', '$', '%', '^', '&', '*', '/', '.', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        returnstring = ""
        for row in self.positions:
            for char in row:
                if char.isupper() or char == 'r' or char in allowed:
                    returnstring += "| " + char + " "
                else:
                    returnstring += "| " + "_" + " "
            returnstring += "\n"
        return returnstring
