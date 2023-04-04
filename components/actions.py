from components.objects import players, maze, losers
import random
from constants.mazeConstants import yellow

# make a fire in random 4 place 
def fire():
    cells = [x for x in maze if not x.is_yellow]
    random_number = random.sample(range(1, len(cells)-1), 4)
    for index in random_number:
        cells[index].has_fire = True
        print(f'Position {cells[index].coordinate} has fire')
        
# delete a fire from all places
def no_fire():
    for element in maze:
        element.has_fire = False        


# able to take the key or heal
def maze_items(player):
    for x in maze:
        if x.has_key and player.position == x.coordinate:
            player.has_key = True
            print(f'Player {player.name} got a key')
            x.has_key = False
        elif x.has_heal and player.position == x.coordinate:
            player.lives = (3 - player.heal_spirits) + 5
            print(f'Player {player.name} got a heal')


# player's ability to move
def move(action, player):
    print(f'Player {player.name} chose to move {action}')
    for index, value in enumerate(maze):
        if value.coordinate == player.position:
            if getattr(value, action):
                escaped_position = player.last_position
                last_position = player.position

                player.position = getattr(value, action)

                if player.position not in yellow:
                    player.last_position = last_position

                print(f'Last position {player.last_position}')
                print(f'Player {player.name} moved to {player.position}')
                
                neighbors = [x.name for x in players if x.position == player.position and x != player]

                if player.position == escaped_position:
                    print(f'Player {player.name} is ascaped from maze')
                    out_of_game(player)
                elif len(neighbors) > 0:
                    print(f'Player {player.name} has neigbors: {", ".join(neighbors)}')
                else:
                    print(f'Player {player.name} does not have a neighbors in cell {player.position}')

                maze_items(player)
                break
            else:
                player.lives -= 1
                print(f'Player {player.name} got damage because he hit a wall')
        pass


# player get damage from fire
def damage_from_fire(player):
    for x in maze:
        if x.has_fire and x.coordinate == player.position:
            player.lives -= 1
            print(f'Player {player.name} got damage from fire')


# player get damage from player
def damage_from_player(player):
    for damaged_player in players:
        if damaged_player.position == player.position and damaged_player != player:
            damaged_player.lives -= 1
            print(f'Player {damaged_player.name} got damage from {player.name} and has {damaged_player.lives} lives')
            if_dead(damaged_player)


# ability to heal himself
def heal(player):
    player.lives += 1
    player.heal_spirits -=1
    print(f'Player {player.name} has {player.lives} lives and {player.heal_spirits} heal spirits')


# get the command from player
def maze_actions(action, player):
    if action in ['up', 'down', 'left', 'right']:
        move(action, player)
        damage_from_fire(player)
    elif action == 'hit':
        damage_from_player(player) 
    elif action == 'heal':
        if player.heal_spirits > 0:
            heal(player)
        else:
            new_action = input(f'Player {player.name} has not heal spirits, choose another command')
            maze_actions(new_action, player)
    else:
        print('Wrong command, try again')
        action = input('Enter action: ')
        maze_actions(action, player)

# remove player from game
def out_of_game(player):
    losers.append(player)
    print(f'Player {player.name} get out of this game')
    if player in players:
        players.remove(player)

# able to take a key from dead player
def if_dead(player):
    if player.lives < 1 and player.has_key:
        has_players = []
        for x in players:
            if player.position == x.position and player != x:
                has_players.append(players.index(x))
        if len(has_players) == 0:
            for square in maze:
                if square.coordinate == player.position:
                    print(f'Position {square.coordinate} has a key after player {player.name}')
                    square.has_key = True
        elif len(has_players) > 0:
            random_player_index = random.randint(0, len(has_players) - 1)
            random_player = has_players[random_player_index]
            players[random_player].has_key = True
            print(f'Player {players[random_player].name} got a key from player {player.name}')
        out_of_game(player)
    elif player.lives < 1:
        out_of_game(player)