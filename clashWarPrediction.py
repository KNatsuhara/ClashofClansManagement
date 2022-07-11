from ast import parse
from inspect import getfile
import json
import requests
import csv

# --------------------- INPUT VARIABLES ----------------------- #

# Clan Tag
clan_tag = "2QJ8Q2LRU"

# ------------------------------------------------------------- #

headers = {
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6ImNjMTEyZWJjLTU3MjItNDJjNC1hNDYyLWJiNzJiZmFiN2IxMiIsImlhdCI6MTY0ODQxNjMzMSwic3ViIjoiZGV2ZWxvcGVyL2MxNGZmYTU1LWFkYWYtMjM5Mi1kNmJjLTM2ODE5ZTZlNDk0MiIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjY5LjE2Ni40Ny4xNDUiXSwidHlwZSI6ImNsaWVudCJ9XX0.XbkvYNocQ71zGcCNkb42e6bdqk5zpu0o0ga8jfigUH6Qk_CLyO3762PcIrGCRwGvpVHO9Q2LIHOMCYlzPdUgDg'
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

