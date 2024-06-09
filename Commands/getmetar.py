import vatbot
import requests

@vatbot.tree.command(
    name="getmetar",
    description="get metar for current airport"
)
async def getmetar(interaction: vatbot.discord.Interaction, icao: str):
    # Fetch data from Vatism api and convert to json
    url: str = f"https://metar.vatsim.net/{icao}"
    res = requests.request("GET", url=url, headers={}, data={})

    # Return the data back to discord
    await interaction.response.send_message(res.text)
