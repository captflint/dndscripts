import random
heads = 0
tails = 0
trials = 1000000000
totaltrials = trials
longest_streak = 0
current_streak = 0
last_trial = -1
def progress():
    if trials % 1000000 == 0:
        print((totaltrials - trials) / totaltrials)
def streak(current_trial):
    global longest_streak
    global current_streak
    global last_trial
    if last_trial - 1 == current_trial:
        current_streak += 1
        last_trial = current_trial
        if current_streak > longest_streak:
            longest_streak = current_streak
            print('New streak:', longest_streak)
    else:
        current_streak = 1
        last_trial = current_trial
while trials != 0:
    flip = random.randint(0, 1)
    if flip == 1:
        heads += 1
        streak(trials)
    elif flip == 0:
        tails += 1
    else:
        print('dafuq?')
    trials -= 1
    progress()
print('Heads:', heads / totaltrials)
print('Tails:', tails / totaltrials)
print('Longest streak:', longest_streak)
