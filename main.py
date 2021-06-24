from Puissance_4.init import *

winner = False
plateau = []

init_game = Game(plateau, 6, 7)                 # création d'un objet de la class InitGame
init_game.players()                             # appel de la méthode "players" afin de rentrer les noms utilisateurs et de choisir aléatoirement qui commencera
init_game.affichage()                           # appel de la méthode "affichage"

while not winner:
    init_game.placement_j1()
    init_game.affichage()
    init_game.placement_j2()
    init_game.affichage()