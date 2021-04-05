import json
from games.CookieClicker.assets import handler


def writeSave():
    data = {}
    data["configs"] = []
    data["configs"].append({
        "cookies" : int(handler.cookies),
        "cookiesPerSeconds" : int(handler.cookiesPerSeconds),
        "cookiesPerSecondsPrice" : int(handler.cookiesPerSecondsPrice),
        "cookiesPerClick" : int(handler.cookiesPerClick),
        "cookiesPerClickPrice" : int(handler.cookiesPerClickPrice)
    })

    with open("games/CookieClicker/saves/config.json", "w") as outfile:
        json.dump(data, outfile)

def readSaveFile():
    try:
        with open("games/CookieClicker/saves/config.json", "r") as readfile: 
            data = json.load(readfile)
            for c in data["configs"]:
                handler.cookies = c["cookies"]
                handler.cookiesPerClick = c["cookiesPerClick"]
                handler.cookiesPerClickPrice = c["cookiesPerClickPrice"]
                handler.cookiesPerSeconds = c["cookiesPerSeconds"]
                handler.cookiesPerSecondsPrice = c["cookiesPerSecondsPrice"]
    except IOError:
        print("No previous save file exists...")


