import os

# If any of these equals false then commands will be disabled
getallcontrollers: bool = True
getcontrollers: bool = True
getflight: bool = True
getmetar: bool = True

# Import token, and returns none if dosnt exist
discordtoken: str = os.getenv("discordtoken")
print(f"/n Discord Token: {discordtoken}")