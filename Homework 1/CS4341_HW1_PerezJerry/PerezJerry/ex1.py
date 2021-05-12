class ConnectFour:

    def __init__(self, board, w, h):
        """Class constructor"""
        # Board data
        self.board = board
        # Board width
        self.w = w
        # Board height
        self.h = h

    def isLineAt(self, x, y, dx, dy):
        """Return True if a line of identical tokens exists starting at (x,y)
           in direction (dx,dy)"""
        # Your code here
        nextX = x + (3 * dx)
        nextY = y + (3 * dy)
        if nextX >= self.w or nextY >= self.h:
            return False
        else:
            if self.board[y][x] == self.board[y + dy][x + dx] == self.board[y+(2*dy)][x+(2*dx)] == self.board[y+(3*dy)][x+(3*dx)]:
                return True
            else:
                return False


    def isAnyLineAt(self, x, y):
        """Return True if a line of identical symbols exists starting at (x,y)
           in any direction"""
        return (self.isLineAt(x, y, 1, 0) or # Horizontal
                self.isLineAt(x, y, 0, 1) or # Vertical
                self.isLineAt(x, y, 1, 1) or # Diagonal up
                self.isLineAt(x, y, 1, -1)) # Diagonal down

    def getOutcome(self):
        """Returns the winner of the game: 1 for Player 1, 2 for Player 2, and
           0 for no winner"""
        # Your code here, use isAnyLineAt()
        if self.h < 4 or self.w < 4: # if the board is less than 4x4 then there cannot be a winner
            return 0
        for x in range(self.w):
            for y in range(self.h):
                if self.isAnyLineAt(x, y) and (x+3 < self.w or y+3 < self.h):
                    setter = self.board[y][x]
                    if setter != 0:
                        return setter
        return 0


    def printOutcome(self):
        """Prints the winner of the game"""
        o = self.getOutcome()
        if o == 0:
            print("No winner")
        else:
            print("Player", o, " won")