# Let's implement the game Mastermind
# and play against the computer
# First play a bit online:
# https://www.archimedes-lab.org/mastermind.html
#
# Create a python program that helps me win this game
#
# Your program suggests a move
# I tell the program the results I got (whites and blacks)
# Your program suggests the next move
# and so on until we win

# ynon@ynonperek.com

game_solver = GameSolver()

for next_suggestion in game_solver:
    # now I got online and try the next suggestion
    game_solver.results(white=3, black=1)









