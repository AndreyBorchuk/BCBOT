import json

import api
from threading import Thread
import string
import random

epic_ids = ["480ctdmgepic", "370cwdmgfireepic", "460tbattdmgepic", "470ffadominionfireepic", "efiredragon", "370cwdmgleafepic", "470ffadominionleafepic", "480wbdmgepic", "eleafdragon", "370cwdmgwaterepic", "470ffadominionwaterepic", "ewaterdragon", "370cwdmgrockepic", "370wbdmgepic", "470ffadominionrockepic", "erockdragon", "370cwdmgwindepic", "410wbdmgepic", "480cttokenepic", "attackdragon", "ewinddragon", "470ffadominionwindepic"]


def get_random_name():
    name = ""
    letters = string.ascii_letters
    name += "".join(random.choice(letters) for i in range(14))
    return name


n = 1


while (True):
    try:
        udid = api.create_bot(get_random_name())
        if (udid is None):
            print("Error while creating account")
            continue
        print(str(n) + "\t" + udid)
        n += 1
        status = api.settings_do(udid)
        if (status is None):
            print("Error while settings")
            continue
        status = api.request_room(udid, "playcamp", "playcamp")
        if (status is None):
            print("Error while request room")
            continue
        status = api.character_updating("penelope", udid, "playcamp")
        if (status is None):
            print("Error while character updating")
            continue
        status = battle_id = api.decr_energy(udid)
        if (status is None):
            print("Error while decr energy")
            continue
        status = api.battle_won(udid, battle_id)
        if (status is None):
            print("Error while battle won request")
            continue
        status = api.gacha_info(udid)
        if (status is None):
            print("Error while gacha info request")
            continue
        status = api.finished_tutorial_do(udid)
        if (status is None):
            print("Error while finished tutorial")
            continue
        status = monster_id = api.gacha_pulling(udid)
        if (status is None):
            print("Error while gacha pulling")
            continue
        print(monster_id)
        if (monster_id in epic_ids):
            accounts = open("top_drop_accounts.json")
            data = json.load(accounts)
            accounts.close()
            accounts = open("top_drop_accounts.json", "w")
            data[udid] = monster_id
            json.dump(data, accounts, indent=4)
            accounts.close()
            print("ЕБАТЬ ТЫ НАХУЙ ЧТО ВЫБИЛ ФЫВФОЫВФЫЛВАЛДФЦСЫДИ КОАЫЦУДДВАЫКУИРОАДЫУ")
    except:
        print("ERROR??")