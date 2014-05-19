import random
heads = 0
tails = 0
trials = 1000000
totaltrials = trials
while trials != 0:
    flip = random.randint(0, 1)
    if flip == 1:
        heads += 1
    elif flip == 0:
        tails += 1
    else:
        print('dafuq?')
    trials -= 1
print('Heads:', heads / totaltrials)
print('Tails:', tails / totaltrials)
