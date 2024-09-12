import json


accounts_file = open("top_drop_accounts.json")
accounts_data = json.load(accounts_file)
accounts_file.close()


mobs_count = {}
ontour = []
oxiden = []


for udid in accounts_data:
    if (len(ontour) != 6 and accounts_data[udid] == "480ctdmgepic"):
        ontour.append(udid)
    elif (len(oxiden) != 10 and accounts_data[udid] == "480ctdmgepic"):
        oxiden.append(udid)
    if (accounts_data[udid] in mobs_count.keys()):
        mobs_count[accounts_data[udid]] += 1
        continue
    mobs_count[accounts_data[udid]] = 0
for i in ontour:
    print(i)
print(mobs_count)