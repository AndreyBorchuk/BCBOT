import time
import json
import api


accounts = open("accounts.json")

accounts = open("accounts.json")
data = json.load(accounts)
accounts.close()

while True:
    for i in data.keys():
        if (data[i][0] + 3600 <= time.time()):
            api.request_room(i, "playcamp", "playcamp")
            count = api.daily_claim(i)
            if (count is None):
                print("Error while daily claim")
                continue
            battle_id = api.decr_energy(i, count)
            if (battle_id is None):
                print("Error while decr energy")
                continue
            print(api.battle_won(i, battle_id))
            data[i] = [time.time(), data[i][1]]
            if (data[i][1] + 86400 <= time.time()):
                status = api.character_updating("trainer_male_6", i, "templegatecamp")
                if (status is None):
                    print("Error while character update")
                    continue
                data[i] = [time.time(), time.time()]
                battle_id = api.decr_energy(i, 10)
                if (battle_id is None):
                    print("Error while decr energy")
                    continue
                print(api.battle_won(i, battle_id))
                accounts = open("accounts.json", "w")
                json.dump(data, accounts, indent=4)
                accounts.close()
    time.sleep(100)