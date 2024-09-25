import random
import api
import threading

from api import login_search

name = ""
target = ""


def send_friend():
    user_id = ""
    while True:
        try:
            udid = api.create_bot(f"{name}{random.randint(10000, 99999)}")
            if (user_id == ""):
                user_id = login_search(target, udid)
            api.request_room(udid, "playcamp", "playcamp")
            api.request_friend(udid, user_id)
        except:
            print("errs")

for i in range(8):
    thread = threading.Thread(target=send_friend)
    thread.start()
