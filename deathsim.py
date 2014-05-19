import random
trials = 0
survived = 0
died = 0
turnavg = 0
longest = 0
while trials != 1000000000:
    strikes = 0
    turn = 0
    while strikes < 3:
        roll = random.randint(1, 20)
        turn += 1
        if roll == 20:
            strikes = 10
        elif roll < 10:
            strikes += 1
        else:
            pass
    if strikes == 10:
        survived += 1
    else:
        died += 1
        turnavg = (turnavg * (died - 1) + turn) / died
        if turn > longest:
            longest = turn
    trials += 1
    if trials % 1000000 == 0:
        print(trials / 1000000000)
print('Survival ratio:', survived / trials)
print('Death ratio:', died / trials)
print('Average time til death:', turnavg)
print('Longest time until death:', longest)
