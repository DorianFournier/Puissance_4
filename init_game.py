
# test 1
# colonne = input("Choix de col :")
# ligne = input("Choix de ligne :")
# plateau[int(ligne)][int(colonne)] = 1

def init_game():
    global plateau, row, col, j1, j2
    row, col = 6, 7
    plateau = [[0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0],
               [0, 0, 1, 0, 0, 0, 0]]

    j1 = input("Entrez le nom du joueur 1 :")
    j2 = input("Entrez le nom du joueur 2 :")


def placement():
    while True:
        user_col = int(input("Choix de colonne :"))
        if 0 <= user_col <= 6:
            break

    for i in range(6):
        if plateau[i][user_col] == 0 and i == 5:
            plateau[i][user_col] = 1
        elif plateau[i][user_col] == 1:
            plateau[i - 1][user_col] = 2
        elif plateau[i][user_col] == 2:
            plateau[i - 1][user_col] = 1


def placement_player(player):
    while True:
        user_col = int(input("Choix de colonne du joueur {0} :".format(player)))
        if 0 <= user_col <= 6:
            break

    for i in range(6):
        if plateau[i][user_col] == 0 and i == 5:
            plateau[i][user_col] = 1
        elif plateau[i][user_col] == 1:
            plateau[i - 1][user_col] = 1
        elif plateau[i][user_col] == 2:
            plateau[i - 1][user_col] = 1


"""
        if player == 2:
            if plateau[i][user_col] == 0 and i == 5:
                plateau[i][user_col] = 2
            elif plateau[i][user_col] == 1:
                plateau[i - 1][user_col] = 2
            elif plateau[i][user_col] == 2:
                plateau[i - 1][user_col] = 2
"""

counter = 0
win = False

init_game()
print(j1)
while not win:
    if counter % 2 == 0:
        placement_player(1)
    elif counter % 2 != 0:
        placement_player(2)
    counter += 1
    affichage()
"""
for i in range(10):
    placement()
    affichage()
"""
class InitGame:
    def __init__(self, plateau, row, col, j1, j2):
        self.plateau = plateau
        self.row = row
        self.col = col
        self.j1 = j1
        self.j2 = j2

    def affichage(self):
        print("Plateau vide :")
        for rw in range(row):
            for cl in range(col):
                print(plateau[rw][cl], end='')
            print('')

