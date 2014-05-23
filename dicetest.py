from roll import roll

lastcommand = 'd20'
while 1 == 1:
    command = input('What do you want to roll? (' + lastcommand + ') ')
    if command == '':
        command = lastcommand
    else:
        lastcommand = command
    results = roll(command)
    for r in results:
        print(r)
    print('Total:', sum(results))
