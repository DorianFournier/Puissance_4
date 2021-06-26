from random import *


class Game:
    def __init__(self, plateau, row=0, col=0, j1='', j2=''):
        self.row = row
        self.col = col
        self.j1 = j1
        self.j2 = j2
        self.plateau = plateau
        self.user_name = None
        self.counterJ1 = 21
        self.counterJ2 = 21
        #self.J1winner = False
        #self.J2winner = False
        #self.equal = False
        self.game_status = {"Egalité": 0, "Victoire J1": 0, "Victoire J2": 0}
        self.col_used = {"0": 0, "1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0}

        for rw in range(self.row):
            temp = []
            for cl in range(self.col):
                temp.append(0)
            self.plateau.append(temp)

    def display(self):
        print("\nPlateau :\n")
        for rw in range(self.row):
            for cl in range(self.col):
                print(self.plateau[rw][cl], end=' ')
            print('')

    def players(self):
        self.j1 = input("Entrez le nom du premier joueur : ")
        self.j2 = input("Entrez le nom du second joueur : ")
        print("\nChoix aléatoire du joueur commençant la partie ...")
        self.user_name = [self.j1, self.j2]
        self.j1 = choice(self.user_name)
        self.user_name.remove(self.j1)
        self.j2 = self.user_name[0]
        print("\n{0} commencera la partie et sera donc le Joueur 1 !".format(self.j1))
        print("{0} sera donc le Joueur 2 !".format(self.j2))

    def placement_j1(self):
        if self.counterJ1 > 0:
            while True:
                print(self.counterJ1)
                user_col = int(input("\n{0} doit choisir une colonne (0 à 6): ".format(self.j1)))
                if 0 <= user_col <= self.row:
                    if 0 <= self.col_used[str(user_col)] < self.row:
                        break
                    else:
                        print("La colonne est pleine, veuillez en choisir une autre !")

            self.col_used[str(user_col)] = self.col_used[str(user_col)] + 1
            print("{0} pions peuvent encore être mis dans la colonne {1}.".format(self.row - self.col_used[str(user_col)], user_col))

            for i in range(6):
                if self.plateau[i][user_col] == 0 and i == 5:
                    self.plateau[i][user_col] = 1
                    break
                elif self.plateau[i][user_col] == 1:
                    self.plateau[i - 1][user_col] = 1
                    break
                elif self.plateau[i][user_col] == 2:
                    self.plateau[i - 1][user_col] = 1
                    break

            # Check horizontal locations for win
            for cl in range(self.col - 3):
                for rw in range(self.row):
                    if self.plateau[rw][cl] == 1 and self.plateau[rw][cl + 1] == 1 and self.plateau[rw][cl + 2] == 1 and \
                            self.plateau[rw][cl + 3] == 1:
                        print("{0} gagne en {1} coups !".format(self.j1, 22 - self.counterJ1))
                        self.game_status["Victoire J1"] = 1

            # Check vertical locations for win
            for c in range(self.col):
                for r in range(self.row - 3):
                    if self.plateau[r][c] == 1 and self.plateau[r + 1][c] == 1 and self.plateau[r + 2][c] == 1 and \
                            self.plateau[r + 3][c] == 1:
                        print("{0} gagne en {1} coups !".format(self.j1, 22 - self.counterJ1))
                        self.game_status["Victoire J1"] = 1

            # Check positively sloped diaganols
            for c in range(self.col - 3):
                for r in range(self.row - 3):
                    if self.plateau[r][c] == 1 and self.plateau[r + 1][c + 1] == 1 and self.plateau[r + 2][c + 2] == 1 \
                            and self.plateau[r + 3][c + 3] == 1:
                        print("{0} gagne en {1} coups !".format(self.j1, 22 - self.counterJ1))
                        self.game_status["Victoire J1"] = 1

            # Check negatively sloped diaganols
            for c in range(self.col - 3):
                for r in range(3, self.row):
                    if self.plateau[r][c] == 1 and self.plateau[r - 1][c + 1] == 1 and self.plateau[r - 2][c + 2] == 1 \
                            and self.plateau[r - 3][c + 3] == 1:
                        print("{0} gagne en {1} coups !".format(self.j1, 22 - self.counterJ1))
                        self.game_status["Victoire J1"] = 1

        else:
            print("Plus de coup disponible")
            self.game_status["Egalité"] = 1

        self.counterJ1 = self.counterJ1 - 1
        return self.game_status

    def placement_j2(self):
        if self.counterJ2 > 0:
            print(self.counterJ2)
            while True:
                user_col = int(input("\n{0} doit choisir une colonne (0 à 6): ".format(self.j2)))
                if 0 <= user_col <= self.row:
                    if 0 <= self.col_used[str(user_col)] < self.row:
                        break
                    else:
                        print("La colonne est pleine, veuillez en choisir une autre !")

            self.col_used[str(user_col)] = self.col_used[str(user_col)] + 1
            print("{0} pions peuvent encore être mis dans la colonne {1}.".format(self.row - self.col_used[str(user_col)], user_col))

            for i in range(6):
                if self.plateau[i][user_col] == 0 and i == 5:
                    self.plateau[i][user_col] = 2
                    break
                elif self.plateau[i][user_col] == 1:
                    self.plateau[i - 1][user_col] = 2
                    break
                elif self.plateau[i][user_col] == 2:
                    self.plateau[i - 1][user_col] = 2
                    break

            # Check horizontal locations for win
            for c in range(self.col - 3):
                for r in range(self.row):
                    if self.plateau[r][c] == 2 and self.plateau[r][c + 1] == 2 and self.plateau[r][c + 2] == 2 and \
                            self.plateau[r][c + 3] == 2:
                        print("{0} gagne en {1} coups !".format(self.j2, 22 - self.counterJ2))
                        self.game_status["Victoire J2"] = 1

            # Check vertical locations for win
            for c in range(self.col):
                for r in range(self.row - 3):
                    if self.plateau[r][c] == 2 and self.plateau[r + 1][c] == 2 and self.plateau[r + 2][c] == 2 and \
                            self.plateau[r + 3][c] == 2:
                        print("{0} gagne en {1} coups !".format(self.j2, 22 - self.counterJ2))
                        self.game_status["Victoire J2"] = 1

            # Check positively sloped diaganols
            for c in range(self.col - 3):
                for r in range(self.row - 3):
                    if self.plateau[r][c] == 2 and self.plateau[r + 1][c + 1] == 2 and self.plateau[r + 2][c + 2] == 2 and \
                            self.plateau[r + 3][c + 3] == 2:
                        print("{0} gagne en {1} coups !".format(self.j2, 22 - self.counterJ2))
                        self.game_status["Victoire J2"] = 1

            # Check negatively sloped diaganols
            for c in range(self.col - 3):
                for r in range(3, self.row):
                    if self.plateau[r][c] == 2 and self.plateau[r - 1][c + 1] == 2 and self.plateau[r - 2][c + 2] == 2 and \
                            self.plateau[r - 3][c + 3] == 2:
                        print("{0} gagne en {1} coups !".format(self.j2, 22 - self.counterJ2))
                        self.game_status["Victoire J2"] = 1

        else:
            print("Plus de coup disponible")
            self.game_status["Egalité"] = 1

        self.counterJ2 = self.counterJ2 - 1
        return self.game_status


"""
        def winning_move(board, piece):
            # Check horizontal locations for win
            for c in range(COLUMN_COUNT - 3):
                for r in range(ROW_COUNT):
                    if board[r][c] == piece and board[r][c + 1] == piece and board[r][c + 2] == piece and board[r][
                        c + 3] == piece:
                        return True

            # Check vertical locations for win
            for c in range(COLUMN_COUNT):
                for r in range(ROW_COUNT - 3):
                    if board[r][c] == piece and board[r + 1][c] == piece and board[r + 2][c] == piece and board[r + 3][
                        c] == piece:
                        return True

            # Check positively sloped diaganols
            for c in range(COLUMN_COUNT - 3):
                for r in range(ROW_COUNT - 3):
                    if board[r][c] == piece and board[r + 1][c + 1] == piece and board[r + 2][c + 2] == piece and \
                            board[r + 3][c + 3] == piece:
                        return True

            # Check negatively sloped diaganols
            for c in range(COLUMN_COUNT - 3):
                for r in range(3, ROW_COUNT):
                    if board[r][c] == piece and board[r - 1][c + 1] == piece and board[r - 2][c + 2] == piece and \
                            board[r - 3][c + 3] == piece:
                        return True
"""