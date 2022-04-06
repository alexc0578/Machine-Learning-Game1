from abc import ABC
from cmath import sqrt
from random import randint, randrange
from classes.grid_object import GridObject
from constants import ENDC, GRID_HEIGHT, MIN_HIT_SCORE
from constants import GRID_WIDTH

class GridUnit(GridObject):
    def __init__(self, player):
        self.player = player
        self.unitName = None
        self.cellText = "U"
        self.maxMp = 0
        self.cur_mp = self.maxMp
        self.maxHp = 0
        self.curHp = self.maxHp
        self.weaponRange = 0
        self.weaponAp = 0 # The armor penetration value of the unit's weapon
        self.weaponDamage = 0 # How much damage a successful hit inflicts
        self.aimModifier = 0 # Modifier to be added to hit rolls
        self.armorValue = 0 # The value to be exceeded to break through this units armor 0 = no armor, 100 = not possible without bonuses

    def distanceTo(self, target: GridObject) -> float:
        xDiff = abs(self.gridCell.x - target.gridCell.x)
        yDiff = abs(self.gridCell.y - target.gridCell.y)

        return float(sqrt((xDiff * xDiff) + (yDiff * yDiff)).real)
    
    def hasLosTo(self, target) -> bool:
        return True

    def attack(self, target):
        # Sanity check to ensure target exists and is valid
        if target is None or target.gridCell is None or target.curHp <= 0:
            print("Invalid target")
            return
            
        print(f"{self.player.textColor}{self.unitName}{ENDC}", end='')

        print(f' attacks ', end='')

        print(f"{target.player.textColor}{target.unitName}{ENDC}")

        if not self.hasLosTo(target):
            # todo how do errors work in python?
            print("No LOS")
            return
        if self.distanceTo(target) > self.weaponRange:
            # todo how do errors work in python?
            print("No range")
            return
        
        # We're in range and have los
        # Roll to hit
        hitScore = randint(1, 100) + self.aimModifier
        if hitScore < MIN_HIT_SCORE:
            print("Missed")
            return

        print("Hit")

        # Roll to breach
        penetrationScore = randint(1, 100) + self.weaponAp
        if penetrationScore <= target.armorValue:
            print("Bounced")
            return

        print("Breached armor")

        # Apply damage
        target.curHp = target.curHp - self.weaponDamage

        print(f'Did {self.weaponDamage} damage')

        # Is the unit dead?
        if target.curHp <= 0:
            # Remove it from the grid and the player list
            target.gridCell.cellObject = None
            target.gridCell = None
            print(f'Killed')

    def moveUp(self, grid):
        # Exec the move
        self.__execMove(grid, self.gridCell.x - 1, self.gridCell.y)

    def moveDown(self, grid):
        # Exec the move
        self.__execMove(grid, self.gridCell.x + 1, self.gridCell.y)

    def moveLeft(self, grid):
        # Exec the move
        self.__execMove(grid, self.gridCell.x, self.gridCell.y - 1)

    def moveRight(self, grid):
        # Exec the move
        self.__execMove(grid, self.gridCell.x, self.gridCell.y + 1)

    def __execMove(self, grid, proposedX, proposedY):
        # Is the move valid (within the board / remaining move points), user turn
        if self.cur_mp <= 0 or proposedY >= GRID_WIDTH or proposedX >= GRID_HEIGHT or self.player != self.player.game.currentPlayer :
            return

        proposedCell = grid[proposedX][proposedY]

        # Is anything in the grid spot already?
        if proposedCell.cellObject is not None:
            return

        #All clear exec the move
        self.cur_mp = self.cur_mp - 1
        self.gridCell.setCellObject(None)
        proposedCell.setCellObject(self)

#First class of player = the soldier
class SoldierUnit(GridUnit):
    pass 
    def __init__(self, player):
        GridUnit.__init__(self, player)

        self.unitName = "Soldier"
        self.cellText = "S"
        self.maxMp = 3
        self.cur_mp = self.maxMp
        self.maxHp = 10
        self.curHp = self.maxHp
        self.weaponRange = 9
        self.aimModifier = 10
        self.armorValue = 30
        self.weaponAp = 15
        self.weaponDamage = 5 

