import vatbot
import settings
import requests

@vatbot.tree.command(
    name="getmetar",
    description="get metar for current airport"
)
async def getmetar(interaction: vatbot.discord.Interaction, icao: str):
    try:
        # Check if commands are not disabled
        if settings.getmetar == False:
            return
        
        # Fetch data from Vatism api and convert to json
        url: str = f"https://metar.vatsim.net/{icao}"
        res = requests.request("GET", url=url, headers={}, data={})

        # Make sure length isn't greater than 5 lines
        shortmetar: list = str(res.text).split("\n")
        addmetar: str = ""
        addmetarcount: int = 0

        # Loop thru metar by line and add only 5 metars togheter
        for getshortmetar in shortmetar:
            if addmetarcount > 15:
                break
            addmetar += f"{getshortmetar}\n"
            addmetarcount += 1

        # Return the data back to discord
        await interaction.response.send_message(f"{addmetar}\n I can only send the first 15 lines beacuse of Discord limitations")
    except Exception as e:
        print(f"/n Something wrong happend in getmatar: {e}")