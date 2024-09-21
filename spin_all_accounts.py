import api
import json


accounts_file = open("top_drop_accounts.json")
accounts_udid = json.load(accounts_file)
accounts_file.close()

print(accounts_udid)

epic_ids = ["480ctdmgepic", "370cwdmgfireepic", "460tbattdmgepic", "470ffadominionfireepic", "efiredragon", "370cwdmgleafepic", "470ffadominionleafepic", "480wbdmgepic", "eleafdragon", "370cwdmgwaterepic", "470ffadominionwaterepic", "ewaterdragon", "370cwdmgrockepic", "370wbdmgepic", "470ffadominionrockepic", "erockdragon", "370cwdmgwindepic", "410wbdmgepic", "480cttokenepic", "attackdragon", "ewinddragon", "470ffadominionwindepic"]
number = 1

for udid in accounts_udid:
    print(number)
    info = None
    while (info is None):
        info = api.gacha_info(udid)
    gold = info["wallet"]["gold"]
    count_pulls = info["gacha_info"][3]["free_spin"]
    for i in range(count_pulls):
        id = api.gacha_pulling(udid)
        if (id in epic_ids):
            print(udid)
            print(id)
    if (gold >= 50):
        id = api.gacha_pulling(udid, "event")
        if (id in epic_ids):
            print(id)
            print(udid)
    number += 1