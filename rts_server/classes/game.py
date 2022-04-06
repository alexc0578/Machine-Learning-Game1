import array
from math import floor
from classes.grid_cell import GridCell
from classes.grid_object import GridObject
from classes.grid_unit import GridUnit, SoldierUnit
from classes.Player import Player
from classes.Terrain import Terrain
from constants import GRID_HEIGHT, GRID_WIDTH, ENDC
import time
from os import system, name


class Game:
    def __init__(self):
        # The current turn (1 based...I guess? It feels dirty)
        self.curTurn = 1

        # The grid array
        self.grid = [[]]
        self.playerRed = Player("Homer", '\033[91m', self)
        self.playerBlue = Player("Lisa", '\033[94m', self)

        # Red goes first
        self.currentPlayer = self.playerRed

        self.define_board()
        self.setup_players()

    # Start the turn for all the players
    def end_round(self):
        if self.currentPlayer == self.playerBlue:
            self.next_turn()

        # Toggle the active player
        self.currentPlayer = (self.playerBlue, self.playerRed)[self.currentPlayer == self.playerBlue]

        self.print_board()


    # Start the turn for all the players
    def next_turn(self):
        # Increment the turn
        self.curTurn = self.curTurn + 1

        # Reset the player's units
        self.reset_player_units(self.playerRed)
        self.reset_player_units(self.playerBlue)
        self.print_board()
    
        
    # For a given player, reset turn based settings (mp, etc)
    def reset_player_units(self, player):
        for i in range(len(player.units)):
            player.units[i].mp = player.units[i].maxMp
            player.units[i].curHp = player.units[i].maxHp

    # define our clear function
    def __clear(self):
    
        # for windows
        if name == 'nt':
            _ = system('cls')
    
        # for mac and linux(here, os.name is 'posix')
        else:
            _ = system('clear')

    def print_board(self):
        # Get some whitespace
        self.__clear()

        # Print the header
        print(f'Turn: {str(self.curTurn)} Active player: {self.currentPlayer.playerName}')

        # This will hold the table text
        print( " ", end='')

        # Define the upper boundary
        for x in range(GRID_WIDTH):
            print( "__", end='')
        print("\n", end='')

        for x in range(GRID_HEIGHT):
            print("|", end='')

            for y in range(GRID_WIDTH):
                print( " ", end='')
                if self.grid[x][y].cellObject is None:
                        print( " ", end='')
                else:
                    if isinstance(self.grid[x][y].cellObject, GridUnit) and self.grid[x][y].cellObject.player is not None:
                        print(f"{self.grid[x][y].cellObject.player.textColor}{self.grid[x][y].cellObject.cellText}{ENDC}", end='')
                    else:
                        print( self.grid[x][y].cellObject.cellText, end='')
            print( "|\n", end='')
        
        # Define the lower boundary   
        print( "|", end='')
        for x in range(GRID_WIDTH):
            print( "__", end='')
        print( "|\n", end='')


    def define_board(self):
        # Construct a column of elements to the width
        for x in range(GRID_HEIGHT):
            gridCol = []

            for y in range(GRID_WIDTH):
                cell = GridCell(x , y)
                gridCol.append (cell)
            self.grid.insert(x, gridCol)
        
        # Set a basic map
        self.grid[5][6].setCellObject(Terrain("Rock"))
        self.grid[5][7].setCellObject(Terrain("Rock"))
        self.grid[5][8].setCellObject(Terrain("Rock"))
        self.grid[5][9].setCellObject(Terrain("Rock"))
        self.grid[5][10].setCellObject(Terrain("Rock"))
        self.grid[5][11].setCellObject(Terrain("Rock"))
        self.grid[5][12].setCellObject(Terrain("Rock"))



    def setup_players(self):
        sRed = self.playerRed.soldier
        sBlue = self.playerBlue.soldier

        self.grid[8][12].setCellObject(sRed)
        self.grid[3][3].setCellObject(sBlue)

