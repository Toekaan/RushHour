
class Car():

    def __init__ (self, name, position, direction, size, red_car):
        # capital letters
        self.name = name

        # example: [1.1, 1.2]
        self.position = position
    
        # horizontal or vertical
        self.direction = direction

        # cars are always 2 or 3 tiles big
        self.size = size

        # is this car the red car?
        self.red_car = red_car 

    def get_rows(self):
        """ Returns row of car or list of rows (based on direction) in int.
        """
        rowlist = []
        if self.direction == "horizontal":
            rowlist.append(int(self.position[0][0]))
            return rowlist
        else:
            rowlist.append(int(self.position[0][0]))
            rowlist.append(int(self.position[1][0]))
            if self.size == 3:
                rowlist.append(int(self.position[2][0]))
            return rowlist

    def get_cols(self):
        """ Returns column of car or list of columns (based on direction) in int.
        """
        collist = []
        if self.direction == "vertical":
            if len(self.position[0]) == 4:
                print('TODO')
            elif len(self.position[0]) == 5:
                print('TODO')
            else:
                collist.append(int(self.position[0][2]))
            return collist
        else:
            # check for 3 or 4 length string
            if len(self.position[0]) == 4: # 11.1 or 1.11 ?
                if self.position[0][1] == '.': #1.11
                    newstr = self.position[0][2] + self.position[0][3]
                    collist.append(int(newstr))
                else:                        
                    collist.append(int(self.position[0][3]))
                print(self.position)
                print(self.position[0])
            elif len(self.position[0]) == 5:
                newstr1 = self.position[0][3] + self.position[0][4]
                collist.append(int(newstr1))
                newstr2 = self.position[1][3] + self.position[1][4]
                collist.append(int(newstr2))
            else:
                collist.append(int(self.position[0][2]))
                collist.append(int(self.position[1][2]))
            if self.size == 3:
                if len(self.position[0]) == 4:
                    if self.position[0][1] == '.': #1.11
                        print("hia")
                    collist.append(int(self.position[2][3]))
                elif len(self.position[0]) == 5:
                    newstr = self.position[2][3] + self.position[2][4]
                    collist.append(int(newstr))
                else:
                    collist.append(int(self.position[2][2]))
            return collist

    
    def moveable(self, board):
        """ Checks if car is moveable.
            Returns string of: (leftright, updown, right, left, down, up or none) based on movability
        """
        # horizontal
        if self.direction == "horizontal":
            # the position to which the car wants to move is either 1 more or 1 less column wise
            right = self.get_cols()[1] + self.size - 1
            left = self.get_cols()[0] - 1
            # check if right or left is out of the boards margins 
            if right > board.width_height:
                move_left = board.positions[self.get_rows()[0]][left]
                move_right = None
            elif left < 0:
                move_right = board.positions[self.get_rows()[0]][right]
                move_left = None
            else:            
                move_right = board.positions[self.get_rows()[0]][right]
                move_left = board.positions[self.get_rows()[0]][left]

            # try to move left and right
            if move_right == "x" and move_left == "x":
                return "leftright"
            elif move_right == "x":
                return "right"
            elif move_left == "x":
                return "left"
            else: 
                return "none"
            
        # vertical
        else:
            up = self.get_rows()[0] - 1
            #print(up)
            down = self.get_rows()[1] + self.size - 1
            # check if up or down is out of the boards margins 
            if up < 0:
                # no room on the board for upward movement
                move_down = board.positions[down][self.get_cols()[0]]
                move_up = None
            elif down > board.width_height:
                # no room on the board for downward movement
                move_up = board.positions[up][self.get_cols()[0]]
                move_down = None
            else:
                # both up and down are possible positions on the board
                move_up = board.positions[up][self.get_cols()[0]]
                move_down = board.positions[down][self.get_cols()[0]]

            # try to move up and down
            if move_down == "x" and move_up == "x":
                return "updown"
            elif move_up == "x":
                return "up"
            elif move_down == "x":
                return "down"
            else: 
                return "none"

    def move(self, board, move_dir):
        """ Tries to move car on the board.
            Returns board with moved car and changes .position of car object
            Nothing changes if car was not moveable in the first place.
        """
        if move_dir == "right":
            # failsafe: do not move through other cars on board
            if board.positions[self.get_rows()[0]][self.get_cols()[1] + (self.size - 1)].isupper() or board.positions[self.get_rows()[0]][self.get_cols()[1] + (self.size - 1)] == 'r':
                print("No movement!")
                return board
            
            # give board correct new positions (characters)
            else:
                board.positions[self.get_rows()[0]][self.get_cols()[1] + (self.size - 1)] = self.name[0]
                board.positions[self.get_rows()[0]][self.get_cols()[0]] = "x"

                # change car objects positions
                for i, col in enumerate(self.position):
                    self.position[i] = str(self.get_rows()[0]) + "." + str(int(col[2]) + 1)
                return board
        elif move_dir == "left":     
            if board.positions[self.get_rows()[0]][self.get_cols()[0] - 1].isupper() or board.positions[self.get_rows()[0]][self.get_cols()[0] - 1] == 'r':
                print("No movement!")
                return board
            else: 
                board.positions[self.get_rows()[0]][self.get_cols()[0] - 1] = self.name[0]
                board.positions[self.get_rows()[0]][self.get_cols()[1] + (self.size - 2)] = "x"

                for i, col in enumerate(self.position):
                    self.position[i] = str(self.get_rows()[0]) + "." + str(int(col[2]) - 1)
                return board
        elif move_dir == "up":
            #print(board.positions[self.get_rows()[0] - 1][self.get_cols()[0]])
            if board.positions[self.get_rows()[0] - 1][self.get_cols()[0]].isupper() or board.positions[self.get_rows()[0] - 1][self.get_cols()[0]] == 'r':
                print("No movement!")
                return board
            else:
                board.positions[self.get_rows()[0] - 1][self.get_cols()[0]] = self.name[0]
                board.positions[self.get_rows()[1] + (self.size - 2)][self.get_cols()[0]] = "x"

                for i, row in enumerate(self.position):
                    self.position[i] = str(int(row[0]) - 1) + "." + str(self.get_cols()[0])

                #print(board)
                return board
        elif move_dir == "down":            
            try:    
                if board.positions[self.get_rows()[1] + (self.size - 1)][self.get_cols()[0]].isupper() or board.positions[self.get_rows()[1] + (self.size - 1)][self.get_cols()[0]] == 'r':
                    print("No movement!")
                    return board
            except IndexError:
                return board
            else: 
                board.positions[self.get_rows()[0]][self.get_cols()[0]] = "x"            
                board.positions[self.get_rows()[1] + (self.size - 1)][self.get_cols()[0]] = self.name[0]

                for i, row in enumerate(self.position):
                    self.position[i] = str(int(row[0]) + 1) + "." + str(self.get_cols()[0])                   
                
                #print(self.position)
                #print(board)
                
                return board
        else:
            #print("NO MOVEMENT!")
            return board

    
    def __str__(self):
        return self.name