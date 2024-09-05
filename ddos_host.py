import api

accounts_file = open("accs", "r")
accounts_udids = accounts_file.read().split()
accounts_file.close()

ign = "KsenyaLego"
user_id = api.login_search(ign, "3SpqOXtqgHCSOA46Psj7rA")

if (user_id is None):
    print("Player Not Found")
    exit()

num = 1
for udid in accounts_udids:
    print(num)
    try:
        api.request_friend(udid, user_id)
    except:
        print("err")
    num += 1