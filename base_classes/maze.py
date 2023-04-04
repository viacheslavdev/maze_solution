class Maze:

    def __init__(self, coordinate, has_key=False, has_heal=False, is_finish=False, is_yellow=False, left=None, right=None, up=None, down=None):
        self.coordinate = coordinate
        self.has_fire = False
        self.has_key = has_key
        self.has_heal = has_heal
        self.is_finish = is_finish
        self.is_yellow = is_yellow
        
        # Able to move to that positions. Other direction is wall.
        self.left = left
        self.right = right
        self.up = up
        self.down = down

