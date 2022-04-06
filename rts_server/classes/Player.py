
from classes.grid_cell import GridCell
from classes.grid_unit import SoldierUnit

#Defines the players
class Player:
    def __init__(self, playerName, textColor, game):
        self.playerName = playerName
        self.game = game #Reference back to the game 
        self.textColor = textColor
        self.soldier = SoldierUnit(self)
 