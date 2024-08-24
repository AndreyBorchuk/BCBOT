import json
import requests
import string
import random
import copy

account = open("account.json")
create_account_data = json.load(account)

gacha_pull = open("monster_gacha2_pull.json")
gacha_pull_data = json.load(gacha_pull)

decr_energy_file = open("decr_energy.json")
decr_energy_data = json.load(decr_energy_file)

battle_won_file = open("battle_won.json")
battle_won_data = json.load(battle_won_file)

gacha_info_file = open("gacha_info.json")
gacha_info_data = json.load(gacha_info_file)

login_search_file = open("login_search.json")
login_search_data = json.load(login_search_file)

request_friend_file = open("request_friend.json")
request_friend_data = json.load(request_friend_file)

daily_claim_file = open("daily_claim.json")
daily_claim_data = json.load(daily_claim_file)

miss_out_file = open("miss_out.json")
miss_out_data = json.load(miss_out_file)

request_room_file = open("request_room.json")
request_room_data = json.load(request_room_file)

character_update = open("character_update.json")
character_update_data = json.load(character_update)

finished_tutorial = open("finished_tutorial.json")
finished_tutorial_data = json.load(finished_tutorial)

settings = open("settings.json")
settings_data = json.load(settings)

init = open("init.json")
init_data = json.load(init)

register_push = open("register_push.json")
register_push_data = json.load(register_push)

url = "http://battlecamp.com/api/"
headers = {'User-Agent': 'Monsters/a.5.32.1'}


def get_token():
    token = ""
    letters = string.ascii_letters + "0123456789"
    token += "".join(random.choice(letters) for i in range(11))
    letters += "-_"
    token += "".join(random.choice(letters) for i in range(140))
    return token


def create_bot(name):
    new_data = copy.copy(create_account_data)
    new_data["login"] = name
    new_data["email"] = new_data["email"].replace("NULL", name)
    response_create = requests.post(url + "register_email", json=new_data, headers=headers)
    if (response_create.json()["status_code"] != 0):
        return None
    udid = response_create.json()["udid"]
    new_init = init_data
    new_init["udid"] = udid
    response_init = requests.post(url + "init", json=new_init, headers=headers)
    new_register_push = register_push_data
    new_register_push["udid"] = udid
    new_register_push["token"] = get_token()
    response_register = requests.post(url + "register_push", json=new_register_push, headers=headers)
    return udid


def finished_tutorial_do(udid):
    new_finished_tutorial_data = finished_tutorial_data
    new_finished_tutorial_data["udid"] = udid
    response_finished_tutorial = requests.post(url + "finished_tutorial", json=new_finished_tutorial_data, headers=headers)
    if (response_finished_tutorial.json()["status_code"] != 0):
        return None
    return True


def request_room(udid, place, place_codename):
    new_request_room_data = request_room_data
    new_request_room_data["udid"] = udid
    new_request_room_data["place"] = place
    new_request_room_data["place_codename"] = place_codename
    response_request_room = requests.post(url + "request_room", json=new_request_room_data, headers=headers)
    if (response_request_room.json()["status_code"] != 0):
        return None
    return True


def gacha_pulling(udid):
    new_gacha_pull_data = gacha_pull_data
    new_gacha_pull_data["udid"] = udid
    response_gacha_pull = requests.post(url + "monster_gacha2_pull", json=new_gacha_pull_data, headers=headers)
    if (response_gacha_pull.json()["status_code"] != 0):
        return None
    return response_gacha_pull.json()["reward"]["id"]


def settings_do(udid):
    new_settings_data = copy.copy(settings_data)
    new_settings_data["udid"] = udid
    response_settings = requests.post(url + "settings", json=new_settings_data, headers=headers)
    if (response_settings.json()["status_code"] != 0):
        return None
    return True


def character_updating(event_id, udid, place):
    new_character_update = character_update_data
    new_character_update["udid"] = udid
    new_character_update["event_id"] = event_id
    new_character_update["place"] = place
    response_character_update = requests.post(url + "monster_character_update", json=new_character_update, headers=headers)
    if (response_character_update.json()["status_code"] != 0):
        return None
    return True


def login_search(login, udid):
    new_login_search = copy.copy(login_search_data)
    new_login_search["udid"] = udid
    new_login_search["login"] = login
    response_login_search = requests.post(url + "login_search", json=new_login_search, headers=headers)
    if (response_login_search.json()["status_code"] != 0):
        return None
    return response_login_search.json()["user"]["user_id"]


def request_friend(udid, user_id):
    new_request_friend = copy.copy(request_friend_data)
    new_request_friend["udid"] = udid
    new_request_friend["user_id"] = user_id
    response_request_friend = requests.post(url + "request_friend", json=new_request_friend, headers=headers)
    if (response_request_friend.json()["status_code"] != 0):
        return None
    return True


def decr_energy(udid, count=5):
    new_decr_energy = copy.copy(decr_energy_data)
    new_decr_energy["udid"] = udid
    new_decr_energy["amount"] = count
    response_decr_energy = requests.post(url + "monster_decr_energy", json=new_decr_energy, headers=headers)
    if (response_decr_energy.json()["status_code"] != 0):
        return None
    return response_decr_energy.json()["battle_id"]


def daily_claim(udid):
    new_daily_claim = copy.copy(daily_claim_data)
    new_daily_claim["udid"] = udid
    response_daily_claim = requests.post(url + "monster_daily_claim", json = new_daily_claim, headers=headers)
    if (response_daily_claim.json()["status_code"] != 0):
        return None
    return response_daily_claim.json()["monster_energy"]["level"]


def gacha_info(udid):
    new_gacha_info = copy.copy(gacha_info_data)
    new_gacha_info["udid"] = udid
    response_gacha_info = requests.post(url + "monster_gacha2_info", json=new_gacha_info, headers=headers)
    if (response_gacha_info.json()["status_code"] != 0):
        return None
    return True


def miss_out():
    response_gacha_info = requests.post(url + "miss_out", json=miss_out_data, headers=headers)
    print(response_gacha_info.json())


def battle_won(udid, battle_id):
    new_battle_won = copy.copy(battle_won_data)
    new_battle_won["udid"] = udid
    new_battle_won["battle_id"] = battle_id
    response_battle_won = requests.post(url + "monster_battle_won", json=new_battle_won, headers=headers)
    if (response_battle_won.json()["status_code"] != 0):
        return None
    return response_battle_won.json()["xp"]["level"]