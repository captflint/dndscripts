import random
trials = 0
survived = 0
died = 0
duration = []
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
        duration.append(turn)
    trials += 1
print('Survival ratio:', survived / trials)
print('Death ratio:', died / trials)
total = 0
longest = 0
for n in duration:
    total += n
    if n > longest:
        longest = n
print('Average time til death:', total / len(duration))
print('Longest time until death:', longest)
