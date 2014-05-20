import random
results = [[1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0], [8, 0], [9, 0], [10, 0], [11, 0], [12, 0], [13, 0], [14, 0], [15, 0], [16, 0], [17, 0], [18, 0], [19, 0], [20, 0]]
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
    roll = random.randint(1, 20)
    for x in range(0, 20):
        if roll == results[x][0]:
            results[x][1] += 1
            break
    if roll == 20:
        streak(trials)
    trials -= 1
    progress()
for item in results:
    print(item[0], '\t', item[1] / totaltrials)
print('Longest streak:', longest_streak)
