from init import Game   # importation de la class Game présente dans le fichier init.py

endGame = False                     # création d'une variable booléenne permettant l'arret de la partie en cas de victoire / nul
game_status = {}                    # création d'un dictionnaire pour stocker les états d'une partie
plateau = []                        # création d'un plateau vide

game = Game(plateau, 6, 7)          # création d'un objet de la class InitGame
game.players()                      # appel de la méthode "players" afin de rentrer les noms utilisateurs et de choisir aléatoirement qui commencera
game.display()                      # appel de la méthode "affichage"


def check_win():
    """
    Fonction permettant de regarder si une valeur de clé est passée à 1
    :return: la variable endGame (Booléenne)
    """
    if (game_status["Egalité"] == 1) or (game_status["Victoire J1"] == 1) or (game_status["Victoire J2"] == 1):         # si une valeur de clé est à 1
        endGame = True                               # passer la variable endGame à True
        print("\n", game_status)                     # afficher le dictionnaire
        return endGame                               # retrouner la variable endGame
    else:                                            # si non
        endGame = False                              # passer la variable endGame à False
        return endGame                               # retourner la variable endGame


while not endGame:                                   # tant qu'il n'y a pas de gagnant

    game_status = game.placement_j1()                # méthode permettant le placement de pion du J1
    game.display()                                   # méthode permettant l'affichage d'informations
    endGame = check_win()                            # appel de la fonction pour regarder si la partie est gagnée

    if not endGame:
        game_status = game.placement_j2()            # méthode permettant le placement de pion du J2
        game.display()                               # méthode permettant l'affichage d'informations
        endGame = check_win()                        # appel de la fonction pour regarder si la partie est gagnée

print("Fin de partie !")