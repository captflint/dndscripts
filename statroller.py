from roll import roll

results = []
for x in range(0, 6):
    statroll = roll('4d6')
    print(statroll)
    statroll.sort()
    del statroll[0]
    results.append(sum(statroll))
modifiers = []
for stat in results:
    stat = stat - 10
    modifiers.append(stat // 2)
print(results)
print('total modifiers:', sum(modifiers))
