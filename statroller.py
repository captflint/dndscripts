from roll import roll

results = []
for x in range(0, 6):
    statroll = roll('4d6')
    print(statroll)
    statroll.sort()
    del statroll[0]
    results.append(sum(statroll))
print(results)
