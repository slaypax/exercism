# Globals for the directions
# Change the values as you see fit
NORTH, EAST, SOUTH, WEST = range(4)


class Robot:
    def __init__(self, direction=NORTH, x=0, y=0):
        self.x = x
        self.y = y
        self.direction=direction
        pass

    def coordinates(self):
        return (self.x, self.y)

    def move(self, direction):
        if 'L':
            self.direction = (self.direction + 1)% 4
        elif 'R':
            self.direction = (self.direction - 1)% 4
        elif 'A':
            self.x += [0, 1, 0, -1][self.direction]
            self.y += [1, 0, -1, 0][self.direction]    

    def simulate(self, path):
        instructions = {"L": self.move("L"), "R": self.move("R"), "A": self.move("A")}
        for instruction in path:
            instructions[instruction]()