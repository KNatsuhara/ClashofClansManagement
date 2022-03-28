import json
import requests
import csv

# --------------------- INPUT VARIABLES ----------------------- #
# Name of csv file
filename = "fancyFriendsSeason1.csv"

# Clan Tag
clan_tag = "2QJ8Q2LRU"

# ------------------------------------------------------------- #

headers = {
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6ImNjMTEyZWJjLTU3MjItNDJjNC1hNDYyLWJiNzJiZmFiN2IxMiIsImlhdCI6MTY0ODQxNjMzMSwic3ViIjoiZGV2ZWxvcGVyL2MxNGZmYTU1LWFkYWYtMjM5Mi1kNmJjLTM2ODE5ZTZlNDk0MiIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjY5LjE2Ni40Ny4xNDUiXSwidHlwZSI6ImNsaWVudCJ9XX0.XbkvYNocQ71zGcCNkb42e6bdqk5zpu0o0ga8jfigUH6Qk_CLyO3762PcIrGCRwGvpVHO9Q2LIHOMCYlzPdUgDg'
}

fields = ['Tag', 'Name', 'Role', 'Townhall Level', 'Trophy Count', 'Best Trophy Count', 'War Stars', 'Troops Donated', 'Troops Received', 'Clan Game Points']

membersList = []

def get_user(tag):
    # return user profile information
    user_tag = tag.replace("#","") # removes '#' from user tag
    memberLink = 'https://api.clashofclans.com/v1/players/%23' + user_tag
    response = requests.get(memberLink, headers=headers)
    user_json = response.json()
    return user_json

def get_clan():
    # return clan member informations
    response = requests.get('https://api.clashofclans.com/v1/clans/%23'+ clan_tag + '/members', headers=headers)
    clan_json = response.json()
    return clan_json

def populateMemberList(clan_json):
    count = 0
    for member in clan_json["items"]:
        count += 1
        memberInfo = []
        user_json = get_user(member['tag'])
        print(count, member['name'])
        #Tag
        memberInfo.append(member['tag'])
        #Name
        memberInfo.append(member['name'])
        #Role
        memberInfo.append(member['role'])
        #Townhall Level
        memberInfo.append(user_json['townHallLevel'])
        #Trophy count
        memberInfo.append(user_json['trophies'])
        # #Best Trophy count
        memberInfo.append(user_json['bestTrophies'])
        # #War Stars
        memberInfo.append(user_json['warStars'])
        #Troops Donated
        memberInfo.append(member['donations'])
        #Troops Received
        memberInfo.append(member['donationsReceived'])
        #Clan Game Points
        memberInfo.append(0)
        # Append clan member information to total list
        membersList.append(memberInfo)


def createCSV():
    # writing to csv file 
    with open(filename, 'w', encoding='utf-8', newline='') as csvfile: 
        # creating a csv writer object 
        csvwriter = csv.writer(csvfile) 
        
        # writing the fields 
        csvwriter.writerow(fields) 
        
        # writing the data rows 
        csvwriter.writerows(membersList)

clan_json = get_clan()
populateMemberList(clan_json)
print(membersList)
createCSV()