import random
strikes = 0
turn = 0
while strikes < 3:
    input('enter to roll: ')
    roll = random.randint(1, 20)
    print('\n' + str(roll))
    turn += 1
    print('Turn:', turn)
    if roll == 20:
        strikes = 10
        print("You survive")
    elif roll < 10:
        print('You get worse')
        strikes += 1
        print('Strike:', strikes)
    else:
        print("You condition stays the same")
        print('Strike:', strikes)
if strikes == 10:
    print("You live")
else:
    print("You die")
