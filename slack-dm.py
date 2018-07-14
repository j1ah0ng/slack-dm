import requests
import time
import json

with open('users.txt', 'r') as file:
    for line in file:
        line    = json.loads(line)
        token    = "YOUR-TOKEN"       # replace this with a legacy token you have generated
        name     = line["user_name"]
        msgs     = ["a",
                    "b",
                    "c",
                    "d",
                    "f"]
        user     = "firstname.lastname"

        for x in msgs:				# iterate through the list msgs
            r = requests.get("https://slack.com/api/chat.postMessage?token=" + token + "&channel=%40" + name + "&text=" + x + "&as_user=" + user + "&pretty=1")
            					# (un)comment the above line to actually send messages
            print(x)				# so the console won't be dead
            time.sleep(0)                       # sleep for longer if your typing is slower
