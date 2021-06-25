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
        self.winner = False
        self.col_used = {"0": 0, "1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0}

        for lines in range(self.row):
            temp = []
            for cln in range(self.col):
                temp.append(0)
            self.plateau.append(temp)

    def affichage(self):
        print("\nPlateau :\n")
        for rw in range(self.row):
            for cl in range(self.col):
                print(self.plateau[rw][cl], end=' ')
            print('')

    def players(self):
        self.j1 = input("Entrez le nom du joueur 1 : ")
        self.j2 = input("Entrez le nom du joueur 2 : ")
        self.user_name = [self.j1, self.j2]
        self.j1 = choice(self.user_name)
        self.user_name.remove(self.j1)
        self.j2 = self.user_name[0]

    def placement_j1(self):
        self.counterJ1 = self.counterJ1 - 1
        if self.counterJ1 >= 0:
            while True:
                print(self.counterJ1)
                user_col = int(input("\n{0} doit choisir une colonne (0 à 6): ".format(self.j1)))
                if 0 <= user_col <= 6:
                    if 0 <= self.col_used[str(user_col)] < 6:
                        break
                    else:
                        print("La colonne est pleine, veuillez en choisir une autre !")

            self.col_used[str(user_col)] = self.col_used[str(user_col)] + 1
            print("{0} pions peuvent encore être mis dans la colonne {1}.".format(6 - self.col_used[str(user_col)], user_col))

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
            if (self.plateau[i][user_col] == 1) and (self.plateau[i][user_col - 1] == 1) and (self.plateau[i][user_col - 2] == 1) and (self.plateau[i][user_col - 3] == 1):
                print("{0} gagne !".format(self.j1))
        else:
            print("Plus de coup disponible")
            self.winner = True
            return self.winner

    def placement_j2(self):
        self.counterJ2 = self.counterJ2 - 1
        if self.counterJ2 >= 0:
            print(self.counterJ2)
            while True:
                user_col = int(input("\n{0} doit choisir une colonne (0 à 6): ".format(self.j2)))
                if 0 <= user_col <= 6:
                    if 0 <= self.col_used[str(user_col)] < 6:
                        break
                    else:
                        print("La colonne est pleine, veuillez en choisir une autre !")

            self.col_used[str(user_col)] = self.col_used[str(user_col)] + 1
            print("{0} pions peuvent encore être mis dans la colonne {1}.".format(6 - self.col_used[str(user_col)], user_col))

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
                if i == 5 and user_col == 0:
                    if (self.plateau[i][user_col] == 2) and (self.plateau[i][user_col + 1] == 2) and (
                            self.plateau[i][user_col + 2] == 2) and (self.plateau[i][user_col + 3] == 2):
                        print("{0} gagne !".format(self.j2))
                    elif (self.plateau[i][user_col] == 2) and (self.plateau[i-1][user_col] == 2) and (
                            self.plateau[i-2][user_col] == 2) and (self.plateau[i-3][user_col] == 2):
                        print("{0} gagne !".format(self.j2))
                    elif (self.plateau[i][user_col] == 2) and (self.plateau[i-1][user_col+1] == 2) and (
                            self.plateau[i-2][user_col+2] == 2) and (self.plateau[i-3][user_col+3] == 2):
                        print("{0} gagne !".format(self.j2))
        else:
            print("Plus de coup disponible")
            self.winner = True
            return self.winner
"""
    def cherche_haut(self, lig, col):
        if lig == 0:
            return 0
        elif self.plateau[lig - 1][col] == 'M':
            return 1
        else:
            return 0

    def cherche_haut_droite(self, lig, col):
        if lig == 0 or col == largeur - 1:
            return 0
        if plateau[lig - 1][col + 1] == 'M':
            return 1
        else:
            return 0

    def cherche_haut_gauche(self, lig, col):
        if lig == 0 or col == 0:
            return 0
        if plateau[lig - 1][col - 1] == 'M':
            return 1
        else:
            return 0

    def cherche_droite(self, lig, col):
        if col == largeur - 1:
            return 0
        if plateau[lig][col + 1] == 'M':
            return 1
        else:
            return 0

    def cherche_gauche(self, lig, col):
        if col == 0:
            return 0
        if plateau[lig][col - 1] == 'M':
            return 1
        else:
            return 0

    def cherche_bas_gauche(self, lig, col):
        if lig == hauteur - 1 or col == 0:
            return 0
        if plateau[lig + 1][col - 1] == 'M':
            return 1
        else:
            return 0

    def cherche_bas_droite(self, lig, col):
        if lig == hauteur - 1 or col == largeur - 1:
            return 0
        if plateau[lig + 1][col + 1] == 'M':
            return 1
        else:
            return 0

    def cherche_bas(self, lig, col):
        if lig == hauteur - 1:
            return 0
        if plateau[lig + 1][col] == 'M':
            return 1
        else:
            return 0
"""