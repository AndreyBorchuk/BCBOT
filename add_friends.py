import api


target = "us6gKaLW71IOfd0eLQTdEw"
udids_file = open("friends", "r")
udids = udids_file.read().split()
udids_file.close()

for udid in udids:
    api.request_friend(udid, target)