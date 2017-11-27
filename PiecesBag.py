class PiecesBag():
    def __init__(self, leftOverPieces):
        self.__piecesList = leftOverPieces

    def getPiece(self):
        top = len(self.__piecesList) - 1
        if len(self.__piecesList) < 1:
            return False
        else:
            return self.__piecesList.pop(top)
