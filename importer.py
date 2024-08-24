import json
import time

accounts_farm = open("accounts.json")
accounts = open("top_drop_accounts.json")
accounts_data = json.load(accounts)
accounts_farm_data = json.load(accounts_farm)
accounts.close()
accounts_farm.close()


accounts_for_farm = open("accounts.json", "w")
farm_data = accounts_farm_data


for i in accounts_data.keys():
    if (i in farm_data):
        continue
    farm_data[i] = [time.time() - 3600, time.time() - 86400, 0]


json.dump(farm_data, accounts_for_farm, indent=4)
accounts_for_farm.close()
