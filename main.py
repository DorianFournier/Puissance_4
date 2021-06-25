from Puissance_4.init import *

winner = False
plateau = []                                    # création d'un plateau vide

game = Game(plateau, 6, 7)                      # création d'un objet de la class InitGame
game.players()                                  # appel de la méthode "players" afin de rentrer les noms utilisateurs et de choisir aléatoirement qui commencera
game.affichage()                                # appel de la méthode "affichage"

while not winner:                               # tant qu'il n'y a pas de gagnant
    winner = game.placement_j1()
    game.affichage()
    winner = game.placement_j2()
    game.affichage()

print("Fin de partie !")
