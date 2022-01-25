class SudokuSolver:
    def __init__(self):
        self.board = [
            [1,0,3],
            [2,0,0],
            [0,1,0]
        ]
        #self.newBoard = []
        self.column1 = [self.board[0][0], self.board[1][0], self.board[2][0]]    
        self.column2 = [self.board[0][1], self.board[1][1], self.board[2][1]]
        self.column3 = [self.board[0][2], self.board[1][2], self.board[2][2]]

    def solve(self):
        # runs through rows
        for line in self.board:
            counter = 0
            # runs through numbers in rows
            for number in line:
                possibleNumbers = [1,2,3]

                if number == 0:
                    
                    #if line.index(number) == 0:
                    if counter == 0:
                        # runs through column1
                        for number2 in self.column1:
                            if number2 != 0 and number2 in possibleNumbers:
                                possibleNumbers.remove(number2)
                        # runs through current row
                        for number2 in line:
                            if number2 != 0 and number2 in possibleNumbers:
                                possibleNumbers.remove(number2)
                        self.board[self.board.index(line)][line.index(number)] = possibleNumbers[0]
                        #self.newBoard.append(possibleNumbers[0])
                    
                    #if line.index(number) == 1:
                    if counter == 1:
                        for number2 in self.column2:
                            if number2 != 0 and number2 in possibleNumbers:
                                possibleNumbers.remove(number2)
                        for number2 in line:
                            if number2 != 0 and number2 in possibleNumbers:
                                possibleNumbers.remove(number2)
                        self.board[self.board.index(line)][line.index(number)] = possibleNumbers[0]
                        #self.newBoard.append(possibleNumbers[0])

                    #if line.index(number) == 2:
                    if counter == 2:
                        for number2 in self.column3:
                            if number2 != 0 and number2 in possibleNumbers:
                                possibleNumbers.remove(number2)
                        for number2 in line:
                            if number2 != 0 and number2 in possibleNumbers:
                                possibleNumbers.remove(number2)
                        self.board[self.board.index(line)][line.index(number)] = possibleNumbers[0]
                        #self.newBoard.append(possibleNumbers[0])
                counter = counter+1
                #else:
                #    pass
                    #self.newBoard.append(number)
                
    def show(self):
        print(self.board)

game = SudokuSolver()
game.solve()
game.show()
