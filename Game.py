import os
from GameEngine import GameEngine


def clearScreen():
    os.system('cls')

class Game():
    def __init__(self):
        self.__gameEngine = None

    def playersQtyInputScreen(self):
        qty = -1
        while qty == -1:
            try:
                qty = int(input("Informe a quantidade de jogadores: "))

                if (qty < 2) or (qty > 4):
                    print("Número de jogadores:")
                    print("Máximo: 4")
                    print("Mínimo: 2")
                    qty = -1
                else:
                    self.__gameEngine = GameEngine(qty)
            except:
                print("Digite apenas números!")
                qty = -1

    def inGameScreen(self):
        self.__gameEngine.showPlayersTurn()
        print("Peças na mesa:")
        self.__gameEngine.showGameTable()
        print("Peças do jogador:")
        numberOfPieces = self.__gameEngine.showPlayerDeck()
        numberOfPieces -= 1

        option = -1
        while option == -1:
            print("1. Jogar")
            print("2. Pegar do banco de paças")
            try:
                option = int(input("Opção: "))

                if (option < 1) or (option > 2):
                    print("Opção inválida!")
                    option = -1
            except:
                print("Digite apenas números!")
                option = -1

        if option == 1:
            selectedPiece = -1

            while selectedPiece == -1:
                try:
                    selectedPiece = int(input("Informe o número da peça que você deseja jogar: "))
                    selectedPiece -= 1

                    if (selectedPiece < 0) or (selectedPiece > numberOfPieces):
                        print("Peça inválida")
                        selectedPiece = -1
                    else:
                        selectedPiece = self.__gameEngine.playerMakeAMove(selectedPiece)
                        haveAWinner = self.__gameEngine.verifyWinner()
                        if haveAWinner:
                            return True
                        self.__gameEngine.changeTurn()
                        self.__gameEngine.updateDeadLock(False)
                except:
                    print("Digite apenas números!")
                    selectedPiece = -1

        else:
            self.__gameEngine.playerPassTurn()
            self.__gameEngine.updateDeadLock(True)
            self.__gameEngine.changeTurn()
            isDeadLock = self.__gameEngine.verifyDeadLock()
            if isDeadLock:
                return self.__gameEngine.verifyDeadlockWinnter()

    def gameLoop(self):
        gameOver = False

        self.playersQtyInputScreen()

        while not gameOver:
            gameOver = self.inGameScreen()
            clearScreen()
