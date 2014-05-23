from random import randint
from roll import roll

NumOfRooms = sum(roll('3d6'))
grid = []
rooms = []

class Room:
    def __init__(self):
        self.horiz = sum(roll('4d4'))
        self.vert = sum(roll('4d4'))
        self.tlc = (0, 0)
    def position(self):
        global grid
        self.trynewloc = True
        while self.trynewloc:
            self.testgrid = []
            self.tlc = (randint(0, 100), randint(0, 100))
            self.h = self.horiz + 2
            self.v = self.vert + 2
            for x in range(-1, self.v - 1):
                for y in range(-1, self.h - 1):
                    self.testgrid.append((self.tlc[0] + y, self.tlc[1] + x))
            self.trynewloc = False
            for coord in self.testgrid:
                if coord in grid:
                    self.trynewloc = True
                    break
                else:
                    pass
        for x in range(0, self.vert):
            for y in range(0, self.horiz):
                grid.append((self.tlc[0] + y, self.tlc[1] + x))

while NumOfRooms != 0:
    x = Room()
    rooms.append(x)
    NumOfRooms -= 1

for r in rooms:
    r.position()

def test():
    h = 0
    v = 0
    displayLine = ''
    while v < 80:
        while h < 80:
            if (h, v) in grid:
                displayLine += '.'
            else:
                displayLine += '#'
            h += 1
        print(displayLine)
        displayLine = ''
        h = 0
        v += 1

test()
