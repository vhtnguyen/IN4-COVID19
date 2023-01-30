import requests
import json
from unidecode import unidecode
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
import pandas as pd
import sys

sys.stdin.reconfigure(encoding="utf-8")
sys.stdout.reconfigure(encoding="utf-8")

# define
URL = "https://api.apify.com/v2/key-value-stores/EaCBL1JNntjR3EakU/records/LATEST?disableRedirect=true."


def getData():
    global URL
    respone = requests.get(URL).json()
    VNdata = json.dumps(respone)
    dataFile = open("dataVN.json", "w", encoding="utf-8")
    dataFile.write(VNdata)
    dataFile.close()
    return respone


#


def getDataFromDB():
    with open("dataVN.json") as dataVN:
        data = json.load(dataVN)
    dataVN.close()
    return data


def getInfo7day():
    res = {}
    data = getDataFromDB()
    res["overview"] = data["overview"]
    return res


def draw7daysChart():
    data = getDataFromDB()
    df = pd.json_normalize(data["overview"])
    ax = df.plot.bar(
        x="date",
        y=["cases", "death", "recovered"],
        figsize=[8, 6],
        title="VIET NAM 7 DAYS COVID-19'S STATICS OVERVIEW",
    )
    df.plot(
        x="date",
        y="avgCases7day",
        c="b",
        ax=ax,
        style="--",
    )
    df.plot(
        x="date",
        y="avgRecovered7day",
        c="g",
        ax=ax,
        style="--",
    )
    # plt.xticks(label=none)#xoay label
    plt.legend(fontsize=6, loc="upper right")
    plt.gca().axes.set(xlabel=None)  # hide xlabel
    # plt.show()

    fig = plt.gcf()
    fig.set_size_inches(7, 5)

    plt.savefig("7daysChart.png", dpi=100)


def shortProvinceName(proviceName):
    shortName = ""
    name = unidecode(proviceName).split()
    ln = len(name)
    if ln == 2:
        shortName += name[0][0]
        shortName += name[1]
        return shortName
    elif ln == 3:
        return "Hue"
    elif ln == 4:
        return "TPHCM"
    elif ln == 5:
        return "BRVT"
    else:
        return ""


def getAllKey(proviceName):
    namelist = []
    namelist.append(proviceName)
    namelist.append(proviceName.lower())
    namelist.append(unidecode(proviceName))
    namelist.append(unidecode(proviceName.lower()))
    namelist.append(shortProvinceName(proviceName))
    namelist.append(shortProvinceName(proviceName).lower())
    return namelist


def makeVNProvinceDict():
    VNDict = {}
    data = getDataFromDB()
    for i in data["locations"]:
        name = i["name"]
        key = name
        val = getAllKey(name)
        VNDict[key] = val
    VNdata = json.dumps(VNDict)
    dataFile = open("VNLocationsDict.json", "w", encoding="utf-8")
    dataFile.write(VNdata)
    dataFile.close()


def getKeyName(prvName):
    with open("VNLocationsDict.json") as dataVN:
        data = json.load(dataVN)
    dataVN.close()
    for key, val in data.items():
        for othername in val:
            if othername == prvName:
                return key
    return ""


def getDataByPrvName(name):
    key = getKeyName(name)
    if key != "none":
        with open("dataVN.json") as dataVN:
            data = json.load(dataVN)
        dataVN.close()
        for loc in data["locations"]:
            if loc["name"] == key:
                return loc
    else:
        return ""


def processName():
    snlist = []
    data = getDataFromDB()
    for i in data["locations"]:
        nameProvice = unidecode(i["name"])
        snlist.append(nameProvice.lower())
    snlist.sort()
    for i in snlist:
        print(i, shortProvinceName(i))


def processInfo(info):
    res = ""
    for key, val in info.items():
        if key != "name":
            res += key + ": "
        res += str(val) + "\n"
    return res


def getInfoToday():
    today = {}
    data = getDataFromDB()
    j = 0
    res = ""
    for key, val in data.items():
        if j == 8:
            break
        res += key.lower() + ": " + str(val) + "\n"
        j += 1
    return res


##getData(URL)
# draw7daysChart()
# VNLocationsDict()
# makeVNProvinceDict


def search(nameprv):
    try:
        res = processInfo(getDataByPrvName(nameprv))
        return res
    except AttributeError:
        return "NOT FOUND"


def login(inputID, inputPW):
    try:
        userDict = open("userData.json")
        data = json.load(userDict)
        userDict.close()
        userData = data[inputID]
        password_data = userData["password"]
        # If password is wrong
        if password_data != inputPW:
            print("wrong")
            return "wrong pw"
        # If password is right, then login successfully
        else:
            print("ok")
            return "login ok"

    except KeyError:
        print("not found")
        return "user not found"


def addUser0(fullname, username, pw, pin):
    newUser = {}
    newUser = {"id": username, "password": pw, "fullname": fullname, "pin": pin}
    with open("userData.json", "w") as userDict:
        json.dump(newUser, userDict)
    userDict.close()


def checkExist(username):
    try:
        userDict = open("userData.json")
        data = json.load(userDict)
        userDict.close()
        userData = data[username]
        user_data = userData["id"]
        if user_data == username:
            return True
    except KeyError:
        return False


def addUser(fullname, username, pw, pin):
    userDict = open("userData.json")
    data = json.load(userDict)
    newUser = {}
    newUser = {"id": username, "password": pw, "fullname": fullname, "pin": pin}
    data[username] = newUser
    with open("userData.json", "w") as userDict:
        json.dump(data, userDict)
    userDict.close()


def checkPIN(username, pin):
    userDict = open("userData.json")
    data = json.load(userDict)
    userDict.close()
    userData = data[username]
    user_data = userData["pin"]
    if user_data == pin:
        return True
    else:
        return False


def changePassword(username, new_password):
    userDict = open("userData.json")
    data = json.load(userDict)
    userDict.close()
    userData = data[username]
    userData["password"] = new_password
    with open("userData.json", "w") as userDict:
        json.dump(data, userDict)
    userDict.close()
