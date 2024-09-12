import api


accounts_file = open("accounts", "r")
accounts_data = accounts_file.read().split()
accounts_file.close()

for udid in accounts_data:
    result = api.gifts_send(udid, ["103966737015078"])
    while (result is None):
        result = api.gifts_send(udid, ["103966737015078"])