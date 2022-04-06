import time
from classes.game import Game

game = Game()

# Shorthand references
sRed = game.playerRed.soldier
sBlue = game.playerBlue.soldier

# A delay so we can watch the demo
sleepTime = .35
game.print_board()

# Move the red soldier arround
sRed.moveUp(game.grid)
time.sleep(sleepTime)
game.print_board()
sRed.moveLeft(game.grid)
time.sleep(sleepTime)
game.print_board()
sRed.moveLeft(game.grid)
time.sleep(sleepTime)
game.print_board()
sRed.moveLeft(game.grid)
time.sleep(sleepTime)
game.print_board()

# Have red attack blue
sRed.attack(sBlue)
sRed.attack(sBlue)


