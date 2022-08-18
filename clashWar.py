from ast import parse
from inspect import getfile
import json
import requests
import csv

# --------------------- INPUT VARIABLES ----------------------- #

# Clan Tag
clan_tag = "2QJ8Q2LRU"

# 2QU0V8PP2

# ------------------------------------------------------------- #

headers = {
    'Authorization' : 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjlmMzg5ZTk4LTg1M2EtNDExZS1hNTlhLTlmYTNlNTJhNjc1NSIsImlhdCI6MTY2MDQ5NTUyNCwic3ViIjoiZGV2ZWxvcGVyL2MxNGZmYTU1LWFkYWYtMjM5Mi1kNmJjLTM2ODE5ZTZlNDk0MiIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjcxLjE5Ny4yMzQuNDIiLCI2Ny4xODUuNzUuNDIiLCI2OS4xNjYuNDcuMTQ1IiwiNjkuMTY2LjQ2LjE1MyJdLCJ0eXBlIjoiY2xpZW50In1dfQ.15UzvGBTiZqXNu18PwQOGl54OT_ITE9cjAAFz4I4BatcmH-w7jw8BpYPBKGQuFcHOaTrsfCcesrehGU7f3BusQ'
}

fields = ['Tag', 'Name', 'Map Position', 'Attack 1 Stars', 'Attack 1 Percent', 'Attack 2 Stars', 'Attack 2 Percent', 'Total Stars', 'Total Percent']

warList = []

def get_current_war():
    # return clan member informations
    response = requests.get('https://api.clashofclans.com/v1/clans/%23'+ clan_tag + '/currentwar', headers=headers)
    war_json = response.json()
    return war_json

def populateWarList(war_json):
    count = 0
    for member in war_json["clan"]["members"]:
        total_stars = 0
        total_percent = 0
        count += 1
        print(member["name"])
        warInfo = []
        # Tag
        warInfo.append(member["tag"])
        # Name
        warInfo.append(member["name"])
        # Map Position
        warInfo.append(member["mapPosition"])
        # Attacks
        try:
            attackList = member["attacks"]
            total_stars, total_percent = parseAttacks(warInfo, attackList)
        except:
            # If member did not attack
            # Attack 1 Stars
            warInfo.append(0)
            # Attack 1 Percent
            warInfo.append(0)
            # Attack 2 Stars
            warInfo.append(0)
            # Attack 2 Percent
            warInfo.append(0)
        # Total Stars
        warInfo.append(total_stars)
        # Total Percent
        warInfo.append(total_percent)
        warList.append(warInfo)

def parseAttacks(warInfo, attack_list):
    atk_count = 0
    total_stars = 0
    total_percent = 0
    for attack in attack_list:
        atk_count += 1
        # Attack 1 and 2 Stars
        warInfo.append(attack["stars"])
        total_stars += attack["stars"]
        # Attack 1 and 2 Percents
        warInfo.append(attack["destructionPercentage"])
        total_percent += attack["destructionPercentage"]
    
    if atk_count < 2:
        # If member only attacked once
        warInfo.append(0)
        warInfo.append(0)
    
    return total_stars, total_percent


def createFilename(war_json):
    # Clan name + Opponent Clan name + War size + Date
    clan_name = war_json["clan"]["name"]
    opponent_clan_name = war_json["opponent"]["name"]
    date = war_json["startTime"]
    war_date = parseWarDate(date)
    filename = str(war_date) + '-' + clan_name + "vs" + opponent_clan_name + ".csv"
    return filename

def parseWarDate(war_date):
    date = str(war_date)
    newDate = ''
    for i in range(8):
        if (i == 4 or i == 6):
            newDate += '.'
        newDate += date[i]
    return newDate

def createCSV(filename):
    # writing to csv file 
    with open(filename, 'w', encoding='utf-8', newline='') as csvfile: 
        # creating a csv writer object 
        csvwriter = csv.writer(csvfile) 
        
        # writing the fields 
        csvwriter.writerow(fields) 
        
        # writing the data rows 
        csvwriter.writerows(warList)


war_json = get_current_war()
filename = createFilename(war_json)
print(filename)
populateWarList(war_json)
print(warList)
createCSV(filename)
