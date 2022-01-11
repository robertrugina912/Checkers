class CheckersGame () :
    def __init__ (self) :
        self.board = [ [ 0, 2, 0, 2, 0, 2, 0, 2 ]
                     , [ 2, 0, 2, 0, 2, 0, 2, 0 ]
                     , [ 0, 2, 0, 2, 0, 2, 0, 2 ]
                     , [ 0, 0, 0, 0, 0, 0, 0, 0 ]
                     , [ 0, 0, 0, 0, 0, 0, 0, 0 ]
                     , [ 1, 0, 1, 0, 1, 0, 1, 0 ]
                     , [ 0, 1, 0, 1, 0, 1, 0, 1 ]
                     , [ 1, 0, 1, 0, 1, 0, 1, 0 ]
                     ]
                     
        self.whoseMove = "white"
        self.isWon = False
    
    def checkWinner(self) :
        foundWhite = False
        foundRed = False
        for rows in self.board:
            if (2 in rows) or (4 in rows):
                foundRed = True
            if (1 in rows) or (3 in rows):
                foundWhite = True
            if foundWhite == True and foundRed == True:
                break
        if foundWhite == False and foundRed == True:
            self.isWon = "red"
        elif foundWhite == True and foundRed == False:
            self.isWon = "white"
            
    def changeTurn(self) :
        if self.whoseMove == "white":
            self.whoseMove = "red"
        elif self.whoseMove == "red":
            self.whoseMove = "white"
    
    def parseMove(self, move):
        try:
            split = move.split(' ')
            # print(move)
            final = []
            # print(split)
            for elem in split:
                Y = int(elem)//10
                X = int(elem)%10
                if X not in range(8) or Y not in range(8):
                    raise ValueError
                final.append((Y,X))
            # print(len(final))
            if len(final) < 2:
                raise ValueError
            return tuple(final)
        except:
            raise ValueError
    
    def move(self, move) :
        moveTup = self.parseMove(move)
        for i in range(len(moveTup) - 1):
            deltaY = moveTup[i+1][0] - moveTup[i][0]
            initial =  self.board[moveTup[i][0]][moveTup[i][1]]
            self.board[moveTup[i][0]][moveTup[i][1]] = 0
            if abs(deltaY) == 1:
                self.board[moveTup[i][0]][moveTup[i][0]] = 0
                if self.whoseMove == "white":
                    if initial == 1 and moveTup[i+1][0] == 0:
                        self.board[moveTup[i+1][0]][moveTup[i+1][1]] = 3
                    else:
                        self.board[moveTup[i+1][0]][moveTup[i+1][1]] = initial
                elif self.whoseMove == "red":
                    if initial == 2 and moveTup[i+1][0] == 7:
                        self.board[moveTup[i+1][0]][moveTup[i+1][1]] = 4
                    else:
                        self.board[moveTup[i+1][0]][moveTup[i+1][1]] = initial
                    
            elif abs(deltaY) == 2:
                aveY = (moveTup[i+1][0] + moveTup[i][0])//2
                aveX = (moveTup[i+1][1] + moveTup[i][1])//2
                self.board[aveY][aveX] = 0
                #self.board[moveTup[i][0]][moveTup[i][1]] = 0
                if self.whoseMove == "white":
                    if initial == 1 and moveTup[i+1][0] == 0:
                        self.board[moveTup[i+1][0]][moveTup[i+1][1]] = 3
                    else:
                        self.board[moveTup[i+1][0]][moveTup[i+1][1]] = initial
                elif self.whoseMove == "red":
                    if initial == 2 and moveTup[i+1][0] == 7:
                        self.board[moveTup[i+1][0]][moveTup[i+1][1]] = 4
                    else:
                        self.board[moveTup[i+1][0]][moveTup[i+1][1]] = initial
                    
                    
                
        self.checkWinner() 
        self.changeTurn()
            
    def isValidMove(self, move) :
        if self.isWon == "white" or self.isWon == "red":
            return False
        parsedMoves = self.parseMove(move)
        for i in range(len(parsedMoves) - 1):
            delta = parsedMoves[i+1][0] - parsedMoves[i][0]
            avey = (parsedMoves[i+1][0] + parsedMoves[i][0])//2
            avex = (parsedMoves[i+1][1] + parsedMoves[i][1])//2
            if self.whoseMove == "white":
                if self.board[parsedMoves[i][0]][parsedMoves[i][1]] == 1:
                    if abs(delta) == 1:
                        if (parsedMoves[i][0] - parsedMoves[i+1][0] == 1) and (abs(parsedMoves[i][1] - parsedMoves[i+1][1]) == 1):
                            if self.board[parsedMoves[i+1][0]][parsedMoves[i+1][1]] == 0:
                                return True
                    elif abs(delta) == 2:
                        if (parsedMoves[i][0] - parsedMoves[i+1][0] == 2) and (abs(parsedMoves[i][1] - parsedMoves[i+1][1]) == 2):
                            if (self.board[parsedMoves[i+1][0]][parsedMoves[i+1][1]]) == 0 and ((self.board[avey][avex] == 2) or (self.board[avey][avex] == 4)):
                                return True
                    
                elif self.board[parsedMoves[i][0]][parsedMoves[i][1]] == 3:
                    if abs(delta) == 1:
                        if (abs(parsedMoves[i][0] - parsedMoves[i+1][0]) == 1) and (abs(parsedMoves[i][1] - parsedMoves[i+1][1]) == 1):
                            if self.board[parsedMoves[i+1][0]][parsedMoves[i+1][1]] == 0:
                                return True
                    elif abs(delta) == 2:
                        if (abs(parsedMoves[i][0] - parsedMoves[i+1][0]) == 2) and (abs(parsedMoves[i][1] - parsedMoves[i+1][1]) == 2):
                            if (self.board[parsedMoves[i+1][0]][parsedMoves[i+1][1]]) == 0 and ((self.board[avey][avex] == 2) or (self.board[avey][avex] == 4)):
                                return True
            elif self.whoseMove == "red":
                if self.board[parsedMoves[i][0]][parsedMoves[i][1]] == 2:
                    if abs(delta) == 1:
                        if (parsedMoves[i+1][0] - parsedMoves[i][0] == 1) and (abs(parsedMoves[i][1] - parsedMoves[i+1][1]) == 1):
                            if self.board[parsedMoves[i+1][0]][parsedMoves[i+1][1]] == 0:
                                return True
                    elif abs(delta) == 2:
                        if (parsedMoves[i+1][0] - parsedMoves[i][0] == 2) and (abs(parsedMoves[i][1] - parsedMoves[i+1][1]) == 2):
                            if (self.board[parsedMoves[i+1][0]][parsedMoves[i+1][1]]) == 0 and ((self.board[avey][avex] == 1) or (self.board[avey][avex] == 3)):
                                return True
                elif self.board[parsedMoves[i][0]][parsedMoves[i][1]] == 4:
                    if abs(delta) == 1:
                        if (abs(parsedMoves[i+1][0] - parsedMoves[i][0]) == 1) and (abs(parsedMoves[i+1][1] - parsedMoves[i][1]) == 1):
                            if self.board[parsedMoves[i+1][0]][parsedMoves[i+1][1]] == 0:
                                return True
                    elif abs(delta) == 2:
                        if (abs(parsedMoves[i][0] - parsedMoves[i+1][0]) == 2) and (abs(parsedMoves[i][1] - parsedMoves[i+1][1]) == 2):
                            if (self.board[parsedMoves[i+1][0]][parsedMoves[i+1][1]]) == 0 and ((self.board[avey][avex] == 1) or (self.board[avey][avex] == 3)):
                                return True
        return False

### EVERYTHING PAST THIS POINT IS A GIFT: Don't touch until December 25th        
    def __str__ (self) :
        out = "  0 1 2 3 4 5 6 7 \n  ╔═╤═╤═╤═╤═╤═╤═╤═╗\n"
        i = 0
        for row in self.board :
            out += f"{str(i)}║"
            j = 0
            for item in row :
                if item == 0:
                    out += "░" if (i + j) % 2 == 0 else " "
                elif item >= 1 and item <= 4:
                    out += ["○", "●", "♔", "♚"][item-1]
                out += "│"
                j += 1
            out = out[:-1]
            out += f"║{str(i)}\n ╟─┼─┼─┼─┼─┼─┼─┼─╢\n"
            i += 1
        out = out[:-18]
        out += "╚═╧═╧═╧═╧═╧═╧═╧═╝\n  0 1 2 3 4 5 6 7 \n"
        return out
    
def runGame (init = False, moveList = False) :
    game = CheckersGame()

    if (init != False) :
        game.board = init
    
    print("Checkers Initialized...")
    print(game)
    if (moveList != False) :
        print("Move List Detected, executing moves")
        for move in moveList :
            print(f"{game.whoseMove} makes move {move}\n")
            if (move == "q") :
                return
            if (game.isValidMove(move)) :
                game.move(move)
                print(game)
                if (game.isWon != 0) :
                    break
            else :
                print("Invalid Move")    
                
    print("Moves must be typed as coordinates (with no commas or brackets) separated by spaces. Row, then column.")
    print("Example: 54 43")
    print("When performing multiple jumps, enter each co-ordinate your piece will land on in sequence.")
    while (game.isWon == False) :
        print(f"{game.whoseMove} to move")
        move = input(">> ")
        if (move == "q") :
            return
        if (game.isValidMove(move)) :
            game.move(move)
            print(game)
            if (game.isWon != 0) :
                break
        else :
            print("Invalid Move")
    print("The Game is Finished!")
    print(f"Congratulations, {game.isWon}!")


moves = [ '50 41'
, '23 32'
, '41 23'
, '12 34'
, '52 41'
, '21 32'
, '41 30'
, '41 52'
, '34 43'
, '56 47'
, '43 52'
, '61 43 21' # double jump
, '10 32'
, '30 21'
, '25 36'
, '21 10'
, '01 13'
, '01 12'
, '10 01'
, '14 25'
, '01 23 41' # w.king double jumps backward
, '41 32'
, '25 34'
, '41 32'
, '34 43'
, '32 21'
, '43 52'
, '72 61'
, '05 14'
, '61 50'
, '52 43'
, '52 61'
, '54 43'
, '61 72' # red gets kinged 
, '70 61'
, '36 47'
, '36 45'
, '50 41'
, '72 50 32 54 72' # round the world! Red king jumps 4, lands back in the place he started.  
, '65 54'
, '16 25'
, '21 12'
, '14 23'
, '54 36 14 32' # This is an invalid move, the final jump is backwards and therefore disallowed.  
, '54 36 14' # This is fine though.
, '72 63'
, '74 52'
, '07 16'
, '14 05'
, '27 36'
, '05 27 45'
, '03 14'
, '76 65'
, '14 25'
, '12 34 61'
, '12 34 16'
]
runGame(moveList = moves)
