# ClashofClansManagement
Clash of Clans related Python Scripts that will return member stats, war stats, and league stats of the current clan season

Planning on to create a clashWarPrediction.py script that will predict the outcome of a clan war.

REMEMBER: To use these scripts you will need to register an account on the clash of clans api website and give them your IP Address to generate your own API token to use these scripts.

clashMembers.py
- Make sure to change the filename and clan_tag at the beginning of the file
- This will return each member's:
  - Tag
  - Name
  - Role
  - Townhall Level
  - Trophy Count
  - Best Trophy Count
  - Total War Stars
  - Troops Donated
  - Troops Received
  - Clan Games (YOU WILL HAVE TO INPUT MANUALLY)


clashWar.py AND clashWarOpponent.py
- Make sure to change the clan_tag at the beginning of the file
- This script will auto generate a filename for you (Date, Clan, Opponent)
- THIS WILL ONLY GRAB DATA FROM THE CURRENT/LAST WAR THE CLAN IS IN
- This will return each member's:
  - Tag
  - Name
  - Map Position/Rank
  - Attack 1 Stars
  - Attack 1 Destruction Percent
  - Attack 2 Stars
  - Attack 2 Destruction Percent
  - Total Stars
  - Total Destruction Percent
  
clashWarOpponent.py
- There was a time where the clan war data did not appear for my clan, but could be found using the opposing clan's tag instead.
- This script outputs the exact same data as clashWar.py, but uses the opposing clan's tag to retrieve the data.

clashLeague.py
- Make sure to change the clan_tag and directory_name at the beginning of the file
- The directory_name will be the name of the file you are saving each clan war you fought in the clan league
- This will also return a final summary/report of each member who fought
- THIS WILL ONLY GRAB DATA FROM THE CURRENT CLAN LEAGUE
- Individual Clan League War report contains info about each member's:
  - Tag
  - Name
  - Map Position/Rank
  - Attack Stars
  - Attack Destruction Percent
  - If they attacked
- Final/Summary Clan League Report contains info about each member's:
  - Tag
  - Name
  - Map Position/Rank
  - Total Stars
  - Total Destruction Percent
  - Average Stars per attack
  - Average Destruction per attack


ENDNOTE:
These scripts will all generate a .csv file. However, I still recommend opening a new excel sheet and importing the .csv data to enable you to sort by each column.
