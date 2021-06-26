from Puissance_4.init import *

endGame = False
game_status = {}
plateau = []                # création d'un plateau vide

game = Game(plateau, 6, 7)  # création d'un objet de la class InitGame
game.players()              # appel de la méthode "players" afin de rentrer les noms utilisateurs et de choisir aléatoirement qui commencera
game.display()              # appel de la méthode "affichage"


def check_win():
    if (game_status["Egalité"] == 1) or (game_status["Victoire J1"] == 1) or (game_status["Victoire J2"] == 1):
        endGame = True
        print(game_status)
        return endGame


while not endGame:  # tant qu'il n'y a pas de gagnant
    if not endGame:
        game_status = game.placement_j1()
        game.display()
        endGame = check_win()
    if not endGame:
        game_status = game.placement_j2()
        game.display()
        endGame = check_win()

print("Fin de partie !")