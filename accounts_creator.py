import api


quests_file = open("quests", "r")
quests_data = quests_file.read().split()
quests_file.close()
count_accounts = 100
base = []
for i in range(count_accounts):
    udid = api.create_bot(api.get_random_name())
    while (udid is None):
        udid = api.create_bot(api.get_random_name())
    status = api.request_room(udid, "playcamp", "playcamp")
    while (status is None):
        status = api.request_room(udid, "playcamp", "playcamp")
    for quest in quests_data:
        level = 0
        while (level == 0):
            try:
                level = api.story_respond(udid, quest)
            except:
                pass
    print(i)
    base.append(udid)


accounts_file = open("accounts", "w")
accounts_file.write("\n".join(base))
accounts_file.close()