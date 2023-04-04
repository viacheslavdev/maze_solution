class Player: 

    def __init__(self, name):
        self.name = name
        self.has_key = False
        self.lives = 5
        self.heal_spirits = 3
        self.position = 'A1'
        self.is_winner = False
        self.escaped = False
        self.last_position = None
