import api
import json
import time

import info_bot

daily_ids_file = open("daily_ids", "r")
daily_ids = daily_ids_file.read().split("\n")
daily_ids_file.close()

start_time = 0
while True:
    if (time.time() - start_time < 86400):
        time.sleep(10)
        continue
    try:
        except_accounts = []
        account_ids_file = open("daily", "r")
        account_ids = account_ids_file.read().split("\n")
        account_ids_file.close()
        for udid in account_ids:
            if (udid == ""):
                continue
            for id in daily_ids:
                level = 0
                while (level == 0):
                    try:
                        level = api.story_respond(udid, id)
                    except:
                        pass
            if (level >= 50):
                except_accounts.append(udid)
            # info_bot.send_notify_level_up(udid, level, "???")
        account_ids_file = open("daily", "r")
        account_ids = account_ids_file.read().split("\n")
        account_ids_file.close()
        new_account_ids = []
        for udid in account_ids:
            if (udid in except_accounts):
                continue
            new_account_ids.append(udid)
        account_ids_file = open("daily", "w")
        account_ids_file.write("\n".join(new_account_ids))
        account_ids_file.close()

        ready_accounts_file = open("ready_accounts", "r")
        ready_accounts_data = ready_accounts_file.read().split("\n")
        ready_accounts_file.close()

        if (ready_accounts_data == [""]):
            ready_accounts_file = open("ready_accounts", "w")
            ready_accounts_file.write("\n".join(except_accounts))
            ready_accounts_file.close()
        else:
            ready_accounts_file = open("ready_accounts", "w")
            ready_accounts_file.write("\n".join(ready_accounts_data) + "\n" + "\n".join(except_accounts))
            ready_accounts_file.close()
    except Exception as exc:
        print(exc)
        print("ERROR???")
    start_time = time.time()