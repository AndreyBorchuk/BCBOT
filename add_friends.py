import api


target = api.login_search("Ontour", "UWiWZDxK4ToqDS1uILqs1w")
if (target is None):
    print("Error target")
    exit()


udids_file = open("friends", "r")
udids = udids_file.read().split()
udids_file.close()

for udid in udids:
    api.request_friend(udid, target)