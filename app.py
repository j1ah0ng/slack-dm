import requests
import time

with open('users', 'r') as file:
    for line in file:
        token    = "REDACTYL PTERODACTYL"       # replace this with a legacy token you have generated
        name     = line.split(".")
        msgs     = ["hello%20" + name[0] + "!", 
                    "hope%20you%27re%20having%20a%20nice%20summer",
                    "just%20wanted%20to%20remind%20you%20that%20our%20team%20banquet%20is%20this%20friday%20at%204%3A30pm%20at%20the%20civic%20center",
                    "if%20you%27re%20coming%2C%20please%20rsvp%20at%20https%3A%2F%2Fdocs.google.com%2Fforms%2Fu%2F3%2Fd%2Fe%2F1FAIpQLSdECmJnDk5SoaMLF6Bd5iVokxdBR1lagvqzfgH7aSUX27r2mw%2Fviewform",
                    "let%20me%20know%20if%20you%20have%20any%20questions"
                    ]
        user     = "firstname.lastname"

        for x in msgs:
            # r = requests.get("https://slack.com/api/chat.postMessage?token=" + token + "&channel=%40" + line + "&text=" + x + "&as_user=" + user + "&pretty=1")
            # uncomment the above line to actually send messages
            print(x)
            time.sleep(0)                       # sleep for longer if your typing is slower

