import api
import string
import random
import threading


def get_random_name():
    name = ""
    letters = string.ascii_letters
    name += "".join(random.choice(letters) for i in range(14))
    return name


def donate():
    while True:
        api.crews_donate_stones("4bZcU1y24fWlpw71JNPocw", 1)


for i in range(6):
    thr = threading.Thread(target=donate)
    thr.start()