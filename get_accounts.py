import api
import random
import string
import time
import threading

def get_random_name():
    name = ""
    letters = string.ascii_letters
    name += "".join(random.choice(letters) for i in range(14))
    return name


def create_account():
    for i in range(50):
        udid = api.create_bot(get_random_name())
        if (udid is None):
            time.sleep(0.5)
            continue
        api.request_room(udid, "playcamp", "playcamp")
        print(udid)


for i in range(20):
    thr = threading.Thread(target=create_account)
    thr.start()
    time.sleep(0.5)