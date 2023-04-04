from components.objects import players
from components.actions import maze_actions, fire, no_fire, out_of_game, if_dead
from constants.mazeConstants import GAME

# game loop
def start_game():
    global GAME
    while GAME and players:
        fire()
        for player in players:
            print('------------------------------------------------------------------')
            print(f'Player {player.name} has position {player.position} and {player.lives} live points')
            print(f'Player {player.name} is going to choose')
            action = str(input('Enter your choise: move to left, right, up, down, hit or heal '))
            maze_actions(action, player)
            if_dead(player)
            if player.position == 'D8' and player.has_key:
                GAME = False
                print(f'Player {player.name} IS WINNER. CONGRAT!!!')
                break
            elif player.position == 'D8' and player.has_key == False:
                out_of_game(player)
                print(f'Golem killed the player {player.name}')
                if not players:
                    GAME = False
                    print(f'All players are loose. Game is over.')
                    break
            elif len(players) == 0:
                GAME = False
                print(f'All players are loose. Game is over.')
                break
        no_fire()

        
