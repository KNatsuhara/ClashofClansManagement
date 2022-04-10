# ClashofClansManagement
3 Python Scripts that will return member stats, war stats, and league stats of the current clan season

REMEMBER: To use these scripts you will need to register an account on the clash of clans api website and give them your IP Address to generate your own API token to use these scripts.

clashMembers.py
- Make sure to change the filename and clan_tag at the beginning of the file
- This will return each member's:
--Tag
--Name
--Role
--Townhall Level
--Trophy Count
--Best Trophy Count
--Total War Stars
--Troops Donated
--Troops Received
--Clan Games (YOU WILL HAVE TO INPUT MANUALLY)

clashWar.py
- Make sure to change the clan_tag at the beginning of the file
- This script will auto generate a filename for you (Date, Clan, Opponent)
- THIS WILL ONLY GRAB DATA FROM THE CURRENT/LAST WAR THE CLAN IS IN
- This will return each member's:
-   Tag
-   Name
-   Map Position/Rank
-   Attack 1 Stars
-   Attack 1 Percent
-   Attack 2 Stars
-   Attack 2 Percent
-   Total Stars
-   Total Percent

clashLeague.py
- STILL IN PROGRESS

ENDNOTE:
These scripts will all generate a .csv file. However, I still recommend opening a new excel sheet and importing the .csv data to enable you to sort by each column.
