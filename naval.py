toLetters = {1: "A", 2: "B", 3: "C", 4: "D", 5: "E", 6:"F", 7:"G", 8: "H", 9: "I", 10:"J", 11:"K", 12: "L", 13: "M", 14 :"N", 15: "O"}
toNumbers = dict()
for number in toLetters:
    toNumbers[toLetters[number]] = number
EASY = {'size': 10, 'ships': 5}
HARD = {'size': 15, 'ships': 8}

class Game:
    
    def __init__(self, difficulty):
        if difficulty == "EASY":
            self.board1 = Board(EASY['size'], EASY['ships'])
            self.board2 = Board(EASY['size'], EASY['ships'])
        else:
            self.board1 = Board(HARD['size'], HARD['ships'])
            self.board2 = Board(HARD['size'], HARD['ships'])

class Block:

    def __init__(self, position):
        self.position = position
        self.shot = False
        self.isShip = False

class Board:

    def __init__(self, size, shipsNumber):
        self.cells = [[Block(self.setPostion([rows,columns])) for rows in range(size)] for columns in range(size)]
        self.size = size
        self.shipsNumber = shipsNumber
        self.ships = dict()
        for i in range(shipsNumber):
            self.ships[i] = []

    def setPostion(self, position):
        if str(position[0]).isnumeric(): 
            return [toLetters[position[0] + 1], position[1]]
        return [toNumbers[position[0]], position[1]]

    def insertShip(self, position, orientation, shipSize):
        if self.verifyInsertion(position, orientation, shipSize):
            if orientation == "horizontal":
                for block in range(shipSize):
                    self.cells[toNumbers[position[0]]][int(position[1]) + block].isShip = True
                    self.ships[len(self.ships) - 1].append([position]) 

    def verifyInsertion(self, position, orientation, shipSize):
        if orientation == "horizontal" and len(self.cells) < int(position[1]) + shipSize:
            for b in range(shipSize):
                if self.cells[position[0]][position[1] + b].isShip:
                    return False
            return True
        else:
            if len(self.cells) < toNumbers[position[0]] + shipSize:
                return False
            for b in range(shipSize):
                if self.cells[toNumbers[position[0]] + b][int(position[1])].isShip:
                    return False
            return True
            

    def __str__(self):
        alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O']
        string = '   '
        count = 0
        for i in range(self.size):
            string += f'{i}   '
        string  += '\n'
        for i in range(self.size):
            string += f'_ _ '
        string  += '\n'
        for row in self.cells:
            string += alpha[count]+ '| '
            count += 1
            for block in row:
                #string += f'{block.position[0] + str(block.position[1])}  '
                if block.shot and not block.isShip:
                    string += 'X   '
                elif not block.shot:
                    string += 'O   '
                else:
                    string += '!   '
            string  += '\n\n'
        return string


game = Game('EASY')
print(game.board1)
#Insert a 4 sized boat in position a0, in horizontal orientation (left to right)
game.board1.insertShip('A0', 'horizontal', 4)