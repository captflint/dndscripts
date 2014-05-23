from random import randint

def roll(dice):
    number = ''
    sides = ''
    befored = True
    for char in dice:
        if char in 'Dd':
            befored = False
            continue
        if befored:
            number += char
        else:
            sides += char

    if number == '':
        number = '1'
    number = int(number)
    sides = int(sides)
    rolls = []

    while number != 0:
        rolls.append(randint(1, sides))
        number -= 1

    return(rolls)
