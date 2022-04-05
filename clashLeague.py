from fileinput import filename
import requests
import csv
import os
# --------------------- INPUT VARIABLES ----------------------- #

# Clan Tag
clan_tag = "2QJ8Q2LRU"
# Name of folder you want to save the war files to... Ex: clanLeague1

directory_name = "clanLeague1"

# ------------------------------------------------------------- #

headers = {
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6ImNjMTEyZWJjLTU3MjItNDJjNC1hNDYyLWJiNzJiZmFiN2IxMiIsImlhdCI6MTY0ODQxNjMzMSwic3ViIjoiZGV2ZWxvcGVyL2MxNGZmYTU1LWFkYWYtMjM5Mi1kNmJjLTM2ODE5ZTZlNDk0MiIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjY5LjE2Ni40Ny4xNDUiXSwidHlwZSI6ImNsaWVudCJ9XX0.XbkvYNocQ71zGcCNkb42e6bdqk5zpu0o0ga8jfigUH6Qk_CLyO3762PcIrGCRwGvpVHO9Q2LIHOMCYlzPdUgDg'
    # 'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjIyYzFmZWM5LTA1NWQtNGViMy04ZjNhLWQ4NjQyMzFlNmZiNCIsImlhdCI6MTY0ODQ5MTYxOSwic3ViIjoiZGV2ZWxvcGVyL2MxNGZmYTU1LWFkYWYtMjM5Mi1kNmJjLTM2ODE5ZTZlNDk0MiIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjY5LjE2Ni40Ni4xNTMiXSwidHlwZSI6ImNsaWVudCJ9XX0.JcG65LcQ5fjREUPrHDv09Jox-MRGdcPn0mk5xD-XirwT31AuySxN6YIbCyohl_7aswIZfOkWu3P9lDRj3c6n8A'
}

fields = ['Tag', 'Name', 'Map Position', 'Attack 1 Stars', 'Attack 1 Percent', 'ifAttacked']

# Create directory
os.mkdir(directory_name)

# Get clan league group json to retieve individual clan war groups
def get_current_leaguegroup():
    # return clan league group information
    response = requests.get('https://api.clashofclans.com/v1/clans/%23'+ clan_tag + '/currentwar/leaguegroup', headers=headers)
    leaguegroup_json = response.json()
    return leaguegroup_json

# Get individual clan league war from war tag
def get_current_clan_league_war(tag):
    # remove # from warTag
    warTag = tag.replace("#","") # removes '#' from league war tag
    # return individual clan league war information
    response = requests.get('https://api.clashofclans.com/v1/clanwarleagues/wars/%23' + warTag, headers=headers)
    individual_war_json = response.json()
    return individual_war_json

# Go through clan league group and collect all clan tags from each round
def get_individual_clan_war_tags(leaguegroup_json):
    warTagList = []
    for warTags in leaguegroup_json["rounds"]:
        for warTag in warTags["warTags"]:
            warTagList.append(warTag)
    return warTagList

# Go through each clan war info from warTagList and check if clan_tag is in the clan war info
def check_relevant_clan_war_tag(warTagList):
    relevant_clan_war_list = []
    for war in warTagList:
        if (war != "#0"):
            clan_war_json = get_current_clan_league_war(war)

            # get opponent and clan tags
            opponent_tag = clan_war_json["opponent"]["tag"]
            main_tag = clan_war_json["clan"]["tag"]

            # remove # from tag
            opponent = opponent_tag.replace("#","")
            clan = main_tag.replace("#","")

            # check and see if the war contains my clan
            if opponent == clan_tag or clan == clan_tag:
                war_tag = war.replace("#", "")
                relevant_clan_war_list.append(war_tag)

    return relevant_clan_war_list

def get_each_clan_war(clan_war_tag_list):
    for clan_war_tag in clan_war_tag_list:
        print(clan_war_tag)
        war_json = get_current_clan_league_war(clan_war_tag)
        warList = populateWarList(war_json)
        filename = createFilename(war_json)
        createCSV(filename, warList)

# Will out a list of lists containing stats on each member in the war
def populateWarList(war_json):
    warList = []
    count = 0

    # Remove # from clan tag in json file
    temp_clan_tag = war_json["clan"]["tag"]
    check_clan_tag = temp_clan_tag.replace("#", "")

    # Find whether your clan is under "clan" or "opponent" in the json file
    if (check_clan_tag == clan_tag):
        my_clan_name = war_json["clan"]["members"]
    else:
        my_clan_name = war_json["opponent"]["members"]

    # Increment through each member in your clan
    for member in my_clan_name:
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
        ifAttacked = False
        try:
            warInfo.append(member["attacks"][0]["stars"])
            warInfo.append(member["attacks"][0]["destructionPercentage"])
            if (member["attacks"][0]["destructionPercentage"] > 0):
                ifAttacked = True
            warInfo.append(ifAttacked)
        except:
            # If member did not attack
            # Attack 1 Stars
            warInfo.append(0)
            # Attack 1 Percent
            warInfo.append(0)
            warInfo.append(ifAttacked)
        warList.append(warInfo)
    return warList

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

def createCSV(filename, warList):
    # writing to csv file 
    with open(os.path.join(directory_name,'') + filename, 'w', encoding='utf-8', newline='') as csvfile: 
        # creating a csv writer object 
        csvwriter = csv.writer(csvfile) 
        
        # writing the fields 
        csvwriter.writerow(fields) 
        
        # writing the data rows 
        csvwriter.writerows(warList)

leaguegroup_json = get_current_leaguegroup()
warTagList = get_individual_clan_war_tags(leaguegroup_json)
print(warTagList)
relevant_clan_war_list = check_relevant_clan_war_tag(warTagList)
print(relevant_clan_war_list)
get_each_clan_war(relevant_clan_war_list)
