class Player():
    def __init__(self, pieces):
        self.__pieces = pieces
        self.__points = 10

    def showPieces(self):
        index = 1
        for piece in self.__pieces:
            print("Peça [" + str(index) + "]:")
            index += 1
            piece.toString()

        return index

    def makeAMove(self, piece):
        self.__points += 4
        try:
            return self.__pieces.pop(piece)
        except:
            return False

    def passTurn(self):
        self.__points -= 2
        return True

    def getFromBank(self, piece):
        self.__points -= 2
        self.__pieces.append(piece)

    def getPiecesQty(self):
        return len(self.__pieces)

    def getPoints(self):
        return self.__points

    def getPieces(self):
        return self.__pieces
