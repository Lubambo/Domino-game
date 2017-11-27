class Piece():
    def __init__(self, sides):
        self.__sides = sides

    def getPice(self):
        return self.__sides

    def reversePiece(self):
        aux = self.__sides[0]
        self.__sides[0] = self.__sides[1]
        self.__sides[1] = aux

    def getLeftSide(self):
        return self.__sides[0]

    def getRightSide(self):
        return self.__sides[1]

    def toString(self):
        if self.__sides[0] == self.__sides[1]:
            print("|" + str(self.__sides[0]) + "|" + str(self.__sides[1]) + "|")
        else:
            print(" |" + str(self.__sides[0]) + "|")
            print(" |-|")
            print(" |" + str(self.__sides[1]) + "|")
