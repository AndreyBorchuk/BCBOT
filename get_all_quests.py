import api

accs = open("accs", "r").read().split()

j = 0

for i in range(0, 1000):
    udid = accs[j]
    id = f"daily_{i + 1}:complete"
    status = api.story_respond(udid, id)
    if (status == 0):
        j += 1