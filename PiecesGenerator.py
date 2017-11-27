from Piece import Piece


class PiecesGenerator():
    def __init__(self):
        self.__piecesList = []

    def genPieces(self):
        for leftNumber in range(7):
            for rightNumber in range(7):
                if rightNumber >= leftNumber:
                    pieceSides = [leftNumber, rightNumber]
                    piece = Piece(pieceSides)
                    self.__piecesList.append(piece)

        print("Quantidade de peças: " + str(len(self.__piecesList)))
        return self.__piecesList
