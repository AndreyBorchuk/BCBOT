import time
import json
import api


accounts = open("accounts.json")

accounts = open("accounts.json")
data = json.load(accounts)
accounts.close()

data = {"VvcACntvP97sfUjWbc0X8Q": [0, 0]}

while True:
    for i in data.keys():
        count = 10
        if (data[i][0] + 3600 <= time.time()):
            while(count != 0):
                api.request_room(i, "playcamp", "playcamp")
                count = api.daily_claim(i)
                if (count is None):
                    print("Error while daily claim")
                    continue
                battle_id = api.decr_energy(i, count)
                print(count)
                if (battle_id is None):
                    print("Error while decr energy")
                    continue
                print(api.battle_won(i, battle_id))
                data[i] = [time.time(), data[i][1]]
                count = api.daily_claim(i)
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