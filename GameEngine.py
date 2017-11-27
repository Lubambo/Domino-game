from random import shuffle
from random import randint
from PiecesGenerator import PiecesGenerator
from PiecesBag import PiecesBag
from Player import Player


class GameEngine():
    def __init__(self, qty):
        self.__playersList = []
        self.__playersQty = qty
        self.__piecesBag = []
        self.__gameTable = []
        self.__playerTurn = -1
        self.__deadLockTurns = 0

        piecesGen = PiecesGenerator()
        gamePieces = piecesGen.genPieces()
        shuffle(gamePieces)

        for index in range(self.__playersQty):
            playerPieces = []

            for piece in range(5):
                playerPieces.append(gamePieces.pop())

            player = Player(playerPieces)
            self.__playersList.append(player)

        self.__piecesBag = PiecesBag(gamePieces)
        self.__playerTurn = randint(0, (self.__playersQty - 1)) % self.__playersQty

    def showGameTable(self):
        for piece in self.__gameTable:
            piece.toString()

    def twoPlayersGame(self):
        if self.__playerTurn == 0:
            print("     (1) - 2")
        else:
            print("     1 - (2)")

    def threePlayersGame(self):
        if self.__playerTurn == 0:
            print("   (1) - 2 - 3")

        elif self.__playerTurn == 1:
            print("   1 - (2) - 3")

        else:
            print("   1 - 2 - (3)")

    def fourPlayersGame(self):
        if self.__playerTurn == 0:
            print(" (1) - 2 - 3 - 4")

        elif self.__playerTurn == 1:
            print(" 1 - (2) - 3 - 4")

        elif self.__playerTurn == 2:
            print(" 1 - 2 - (3) - 4")

        else:
            print(" 1 - 2 - 3 - (4)")

    def showPlayersTurn(self):
        print(" = Jogadores =")
        if self.__playersQty == 2:
            self.twoPlayersGame()

        elif self.__playersQty == 3:
            self.threePlayersGame()

        else:
            self.fourPlayersGame()

    def changeTurn(self):
        self.__playerTurn = (self.__playerTurn + 1) % self.__playersQty

    def showPlayerDeck(self):
        numberOfPieces = self.__playersList[self.__playerTurn].showPieces()
        return numberOfPieces

    def playerMakeAMove(self, pieceIndex):
        piece = self.__playersList[self.__playerTurn].makeAMove(pieceIndex)

        if len(self.__gameTable) > 0:
            tableLeft = self.__gameTable[0].getLeftSide()
            tableRight = self.__gameTable[-1].getRightSide()

            if not piece:
                print("Peça selecionada: NULL")
                print("Peça inválida!")
                return -1
            elif ((piece.getLeftSide() != tableLeft) and (piece.getLeftSide() != tableRight) and
                      (piece.getRightSide() != tableLeft) and (piece.getRightSide() != tableRight)):
                print("Peça selecionada:")
                piece.toString()
                return -1
            else:
                print("Peça selecionada:")
                piece.toString()
                if piece.getLeftSide() == tableLeft:
                    piece.reversePiece()
                    self.__gameTable.insert(0, piece)
                elif piece.getRightSide() == tableLeft:
                    self.__gameTable.insert(0, piece)
                elif piece.getLeftSide() == tableRight:
                    self.__gameTable.append(piece)
                elif piece.getRightSide() == tableRight:
                    piece.reversePiece()
                    self.__gameTable.append(piece)
                return 1
        else:
            self.__gameTable.append(piece)

    def verifyWinner(self):
        if self.__playersList[self.__playerTurn].getPiecesQty() == 0:
            print("O jogador [" + str(self.__playerTurn) + "] venceu!")
            return True
        else:
            return False

    def playerPassTurn(self):
        self.__playersList[self.__playerTurn].passTurn()

        piece = self.__piecesBag.getPiece()

        if piece:
            self.__playersList[self.__playerTurn].getFromBank(piece)
        else:
            print("O banco de peças esta vazio!")

    def updateDeadLock(self, playerPass):
        if playerPass:
            deadlock = True
            tableLeft = self.__gameTable[0].getLeftSide()
            tableRight = self.__gameTable[-1].getRightSide()
            for piece in self.__playersList[self.__playerTurn].getPieces():
                if ((piece.getLeftSide() == tableLeft) or (piece.getLeftSide() == tableRight) or
                      (piece.getRightSide() == tableLeft) or (piece.getRightSide() == tableRight)):
                    deadlock = False
            if deadlock:
                self.__deadLockTurns += 1
        else:
            self.__deadLockTurns = 0

    def verifyDeadLock(self):
        if self.__deadLockTurns >= self.__playersQty:
            return True
        else:
            return False

    def verifyDeadlockWinnter(self):
        lessPieces = 28
        morePoints = 0

        for index in range(self.__playersQty):
            playerPiecesQty = self.__playersList[index].getPiecesQty()
            playerPoints = self.__playersList[index].getPoints()

            if playerPiecesQty < lessPieces:
                lessPieces = playerPiecesQty

            if playerPoints > morePoints:
                morePoints = playerPoints

        for index in range(self.__playersQty):
            playerPiecesQty = self.__playersList[index].getPiecesQty()
            playerPoints = self.__playersList[index].getPoints()

            if (playerPoints == morePoints) and (playerPiecesQty == lessPieces):
                print("O jogador[" + str(index) + "] venceu!")
                return True

        return False
