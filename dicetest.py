from roll import roll

while 1 == 1:
    command = input('What do you want to roll? ')
    results = roll(command)
    for r in results:
        print(r)
    print('Total:', sum(results))
