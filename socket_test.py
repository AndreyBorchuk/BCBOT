import requests
import api


session = requests.Session()
headers = {'User-Agent': 'Monsters/a.5.32.1'}
room = api.request_room("UWiWZDxK4ToqDS1uILqs1w", "playcamp", "playcamp")
cookie = {"_rails-support_session": room["session_key"]}
print(room)
print(session.get(f"http://{room["room"]["host"]}:{room["room"]["port"]}", cookies=cookie, headers=headers, data={"client_version": "a.5.32.1"}).json())