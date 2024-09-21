for j in range(3, 100):
    print (f"{j}% ", end="")
    chance = 3
    data = [3]
    i = 0
    while chance < j:
        data.append(data[i] * 0.97)
        i += 1
        chance += data[-1]
    print(len(data))
