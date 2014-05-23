import random
from roll import roll

NumOfRooms = sum(roll('3d6'))
grid = []
rooms = []

while NumOfRooms != 0:
    rooms.append((sum(roll('4d4')), sum(roll('4d4'))))
    NumOfRooms -= 1

for r in rooms:
    TopLeftCorner = (random.randint(0, 100), random.randint(0, 100))
    horiz = r[0]
    vert = r[1]
    for x in range(0, vert):
        while horiz > 0:
            grid.append((TopLeftCorner[0] + horiz, TopLeftCorner[1] + x))
            horiz -= 1
        horiz = r[0]

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
