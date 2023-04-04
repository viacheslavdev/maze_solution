from base_classes.player import Player
from base_classes.maze import Maze
from constants.mazeConstants import *

# create a players
def getPlayers():
    print('Let\'s start this game')
    while True:
        try:
            count_players = int(input('How many players? '))
            if count_players <= 0:
                print("Please enter a number greater than 0.")
            else:
                break
        except ValueError:
            print("Please enter a valid number.")
    players = [Player(str(input(f'Enter player\'s name {x}'))) for x in range(1, count_players+1)]
    return players

players = getPlayers()

losers = []

maze = [
    Maze(A1, right=A2),
    Maze(A2, up=B2, left=A1),
    Maze(B2, right=B3, down=A2),
    Maze(B3, left=B2, up=C3, right=B4),
    Maze(C3, down=B3, has_key=True, is_yellow=True),
    Maze(B4, left=B3, down=A4),
    Maze(A4, up=B4, right=A5),
    Maze(A5, left=A4, right=A6),
    Maze(A6, left=A5, up=B6),
    Maze(B6, down=A6, right=B7, up=C6),
    Maze(B7, left=B6, has_heal=True, is_yellow=True),
    Maze(C6, down=B6, up=D6),
    Maze(D5, right=D6, has_heal=True, is_yellow=True),
    Maze(D6, down=C6, left=D5, right=D7),
    Maze(D7, left=D6, right=D8),
    Maze(D8, left=D7, is_finish=True)
]


