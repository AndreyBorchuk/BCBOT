import random

import api

accs = open("accs", "r").read().split()
n = 0

for i in range(10, 100):
    for j in range(1, 10):
        if (api.story_respond(accs[n], f"{i}_{j}:complete") != 0):
            print(i, j)
        n += 1