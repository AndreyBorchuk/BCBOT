import api
import string
import random
import threading


def get_random_name():
    name = ""
    letters = string.ascii_letters
    name += "".join(random.choice(letters) for i in range(14))
    return name


def rename():
    while True:
        api.rename("4bZcU1y24fWlpw71JNPocw", get_random_name(), "AtaZHtuMDPPQ3V2KubPhBA")


for i in range(6):
    thr = threading.Thread(target=rename)
    thr.start()