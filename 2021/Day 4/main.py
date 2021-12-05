class Board (object):
    def __init__(self, board, id):
        self.id = id
        self.board = self.createBoard(board)
        self.competed = False
        self.numColumn = [0,0,0,0,0]
        self.numRow = [0,0,0,0,0]
    
    def createBoard(self, board):
        for i in range(5):
            for j in range(5):
                board[i][j] = {
                    "value": int(board[i][j]),
                    "marked": False
                }
        return board
    
    def updateBoard(self, num):
        for i in range(5):
            for j in range(5):
                if self.board[i][j]["value"] == num:
                    self.board[i][j]["marked"] = True
                    self.numColumn[i] += 1
                    self.numRow[j]+= 1
                    if self.numRow[j] == 5 or self.numColumn[i] == 5:    
                        print("Board: ", self.id, " Victory royale")
                        self.competed = True
                    break
    def calculateCode(self, num):
        sum = 0
        for i in range(5):
            for j in range(5):
                if self.board[i][j]["marked"] == False:
                    sum += self.board[i][j]["value"]
        print(sum, num)
        return int(sum) * int(num)


lines = open("Day 4/dataFull.txt").read().splitlines()

boardAux = []
bingoList = []
boardList = []
i = 0
numBoard = 0

for line in lines:

    if i == 0:
        bingoList = line.split(",")

    elif line != '':
        spLine = line.split(" ")
        spLine[:] = (value for value in spLine if value != '')
        boardAux.append(spLine)

    elif line == '' and i != 1: 
        numBoard += 1
        boardList.append(Board(boardAux, numBoard))
        boardAux=[]    
    i += 1

boardList.append(Board(boardAux, numBoard + 1))

i = 0

def updateNumberBoard(num, board):
    for board in boardList:
        board.updateBoard(int(num))
        code = -1
        if(board.competed == True):
            code = board.calculateCode(num)
            return code
    return -1
    
    
for num in bingoList:

    code = updateNumberBoard(num, boardList)
    if(code != -1):
        print("RESULT!: ", code)
        break
        

