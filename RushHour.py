from board import Board
from car import Car
from random import randint
import time
from colorama import init
init()
import sys

class RushHour():
    """
    This is the Rush Hour game.
    """
    
    def __init__(self, game):
        """
        Create the board within the game and create car objects
        """
        self.board = self.load_board(f"data/{game}.txt")
        self.cars = self.load_cars()

    def load_board(self, filename):
        """
        initialize a Board object from the filename
        """
        # loadboard = [[],[]]
        loadboard = []
        redCarPosition = []
        exitPosition = ""
        allowed = ['!', '@', '#', '$', '%', '^', '&', '*', '/', '.', 'x', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        with open(filename, "r") as f:
            # still have lines to load in
            for i, line in enumerate(f):
                row = []
                if not line == "\n":
                    line.strip('\n')
                    for j, char in enumerate(line):
                        # still have chars to add to array
                        
                        # add car positions 
                        if char.isupper() or char in allowed:
                            row.append(char)

                        # red car position (example: [2.4, 2.5])
                        elif char == "r":
                            redCarPosition.append(str(i) + "." + str(j))
                            row.append(char)

                        # finish position
                        elif char == "e":
                            exitPosition = str(i) + "." + str(j - 1)
                loadboard.append(row)
            # initialize board
            board = Board(i, loadboard, exitPosition)
            return board
    
    def load_cars(self):
        """
        Searches all cars on the grid, creates car objects, append to list
        """
        positions = self.board.positions
        # letters of cars which are already taken
        taken_cars = []
        # list of car objects
        cars = []
        # list of allowed car chars
        allowed = ['!', '@', '#', '$', '%', '^', '&', '*', '/', '.', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        
        # 
        for i, row in enumerate(positions):
            for j, char in enumerate(row):
                # check for red car (which is always horizontal and of size 2)
                if (char.isupper() or char in allowed) and char not in taken_cars:
                    # trying to find a horizontal car
                    try:
                        if positions[i][j + 1] == char:
                            taken_cars.append(char)
                            # check for third 'block'
                            try:
                                if positions[i][j + 2] == char:
                                    position = [str(i) + "." + str(j), str(i) + "." + str(j + 1), str(i) + "." + str(j + 2)]
                                    car = Car(char * 3, position, "horizontal", 3, False)
                                    cars.append(car)
                                    continue
                                # add 'x' at end of list just to be sure index error wont occur 
                                position = [str(i) + "." + str(j), str(i) + "." + str(j + 1)] # removed x
                                car = Car(char * 2, position, "horizontal", 2, False)
                                cars.append(car)
                            # car found, but not a 3 tile car
                            except IndexError:
                                position = [str(i) + "." + str(j), str(i) + "." + str(j + 1)] # removed x
                                car = Car(char * 2, position, "horizontal", 2, False)
                                cars.append(car)
                                continue
                    # no car found
                    except IndexError:
                        pass

                    # trying to find a vertical car
                    try:
                        if positions[i + 1][j] == char:
                            taken_cars.append(char)
                            try:
                                if positions[i + 2][j] == char:
                                    position = [str(i) + "." + str(j), str(i + 1) + "." + str(j), str(i + 2) + "." + str(j)]
                                    car = Car(char * 3, position, "vertical", 3, False)
                                    cars.append(car)
                                    continue
                                position = [str(i) + "." + str(j), str(i + 1) + "." + str(j)] # removed x 
                                car = Car(char * 2, position, "vertical", 2, False)
                                cars.append(car)
                            except IndexError:
                                position = [str(i) + "." + str(j), str(i + 1) + "." + str(j)] # removed x
                                car = Car(char * 2, position, "vertical", 2, False)
                                cars.append(car)
                                continue
                    except IndexError:
                        continue
                elif char == "r" and char not in taken_cars:
                    position = [str(i) + "." + str(j), str(i) + "." + str(j + 1)] # removed x
                    redcar = Car("redCar", position, "horizontal", 2, True)
                    taken_cars.append(char)
                    cars.append(redcar)        
        self.board.cars = cars
        return cars
                
    def find(self):
        # while redcar_position niet op self.board.exit_position:
        print("hio")
        
    def check(self):
        """
        checks if car(s) are in certain row or colomn
        """
        print("test")

    def move(self, car, direction):
        """
        Moves car on the board 1 position in specified direction
        Takes car object and 0 or 1 for direction
        horizontal + 0 = right (+ 1 = left)
        vertical + 0 = up (+ 1 = down)
        """
        allowed = ['!', '@', '#', '$', '%', '^', '&', '*', '/', '.', '1', '2', '3', '4', '5', '6', '7', '8', '9']

        position = car.position
        #if "x" in position:
        #   position.remove("x")
        print(car.name)
        print(position)

        if car.direction == "horizontal":
            # get the horizontal row of the car
            row = int(position[0][0])
            print (row)
            # move car right
            if direction == 0:
                # check if care is 2 tiles or 3 tiles big
                # move_position indicates the character in the grid to where the car wants to move
                if car.size == 2:
                    move_position = self.board.positions[row][int(position[1][2]) + 1]
                else:
                    move_position = self.board.positions[row][int(position[2][2]) + 1]
                    print(move_position)

                # check if movement is possible
                if (not(move_position.isupper() or move_position in allowed or move_position == 'r')):
                    # move the car: change cars position on the board
                    self.board.positions[row][int(position[0][2])] = 'x' # leftmost
                    # check (again) if care is 2 tiles or 3 tiles big
                    if car.size == 2: 
                        self.board.positions[row][int(position[1][2]) + 1] = car.name[0] # rightmost 
                    else:
                        self.board.positions[row][int(position[2][2]) + 1] = car.name[0] 
                    # print just for clarity
                    print(self.board)
                else:
                    print("Direction not possible")
                
            # move car left
            else:
                # check if car is 2 tiles or 3 tiles big
                # move_position indicates the character in the grid to where the car wants to move
                #if car.size == 2:
                move_position = self.board.positions[row][int(position[0][2]) - 1]
                print(move_position)
                #else:
                #    move_position = self.board.positions[row][int(position[0][2]) - 1]
                    
                # check if movement is possible
                if (not(move_position.isupper() or move_position in allowed or move_position == 'r')):
                    # move the car: change cars position on the board
                    self.board.positions[row][int(position[0][2]) - 1] = car.name[0] # leftmost
                    # check (again) if care is 2 tiles or 3 tiles big
                    if car.size == 2: 
                        self.board.positions[row][int(position[1][2])] = 'x' # rightmost 
                    else:
                        self.board.positions[row][int(position[2][2])] = 'x' 
                    print(self.board)
                else:
                    print("Direction not possible")
                

        elif car.direction == "vertical":
            # move car up
            if direction == 0:
                # check if movement is possible
                print("Direction error.0")
                
            # move car down
            else:
                print("Direction error.")
                

        elif direction == "down":
            print("Direction error.")

        elif direction == "left":
            print("Direction error.")
        elif direction == "right":
            print("Direction error.")

        else:
            print("Direction error.")
           
    def playtest(self):
        print(self.board.positions)
        for line in self.board.positions:
            print(line)
        for i, car in enumerate(self.cars):
            print("No.%s: CAR: %s" % (i, car))
            print(car.direction)
            print(car.position)
            print('\n')
        print(self.board.width_height)        
        print(self.board)
        # rushhour.move(self.cars[32], 0)
        # rushhour.move(self.cars[36], 1)        
        #car = self.cars[6]
        #move = car.moveable(self.board)
        #car.move(self.board, move)
        for car in self.cars:
            if car.name == "redCar":
                rredcar = car
                break
        print(rredcar.position[1])
        
        
        # brute force the game!
        
        moves = 0
        moveables = ["left", "right", "up", "down"]
        AAcar = self.cars[6]
        movedir = AAcar.moveable(self.board)
        #print(AAcar.position)
        #AAcar.move(self.board, movedir)
        #print(movedir)
        #print(AAcar.position)
        ##AAcar.move(self.board, movedir)
        #print(AAcar.position)
        #print(rredcar.position[1])
        #print(self.board.exit_position)
        while rredcar.position[1] != self.board.exit_position:
            rredcarpos = self.cars[3].position
            randy = randint(0, len(self.cars) - 1)
            randomcar = self.cars[randy]
            #print(randomcar)
            carmove = randomcar.moveable(self.board)
            #print(carmove)
            if carmove in moveables:
                randomcar.move(self.board, carmove)
            elif carmove == "leftright": 
                rand = randint(0, 1)
                if rand == 0:
                    randomcar.move(self.board, "left")
                else:
                    randomcar.move(self.board, "right")
            elif carmove == "updown":
                rand = randint(0, 1)
                if rand == 0:
                    randomcar.move(self.board, "up")
                else:
                    randomcar.move(self.board, "down")
            else:
                continue    
            moves += 1
            if moves % 100000 == 0:
                print(self.board)
                print(moves)
            if rredcar.position != rredcarpos:
                print(self.board)
                print(moves)
        print(moves)
        print(self.board)
        

if __name__ == "__main__":
    rushhour = RushHour("medium2")
    rushhour.playtest()
    
