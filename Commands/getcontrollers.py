import vatbot
import requests

@vatbot.tree.command(
    name='getcontrollers',
    description='Search for online atc by country code',
    # guild=vatbot.discord.Object(id=971816793704386630)

)
async def getcontrollers(interaction: vatbot.discord.Interaction, icao: str):
    try:
        # Check if icao isnt empty and contains atleast 2 chars
        if len(icao) < 2 or icao == "":
            await interaction.response.send_message("Icao cannot be empty or has to be atleast 2 chars in length")
            return

        # Fetch data from Vatism api and convert to json
        url: str = "https://data.vatsim.net/v3/vatsim-data.json"
        res = requests.request("GET", url=url, headers={}, data={})
        controllers = res.json()["controllers"]

        # Check if controller is found in list and return it
        for ctrls in controllers:
            if icao in str(ctrls['callsign']):
                await interaction.response.send_message(embed=await sendvatsimembed(interaction, ctrls))
                return

        await interaction.response.send_message(f"No Controllers was found online with the given icao: {icao}")
        return

    except Exception as e:
        print(f"\n Error: {e}")

async def sendvatsimembed(interaction: vatbot.discord.Interaction, ctrls):
    embed = vatbot.discord.Embed(
        title=f"Controller information for {ctrls['name']}",
        description=f"Live Vatsim data for {ctrls['callsign']}",
        color=55
    )
    embed.add_field(name='VID:', value=ctrls['cid'], inline=True)
    embed.add_field(name='Position:', value=ctrls['callsign'], inline=True)
    embed.add_field(name='Frequency:', value=ctrls['frequency'], inline=True)
    embed.add_field(name='Visual Range:', value=f"{ctrls['visual_range']}NM", inline=True)
    embed.add_field(name='Atis:', value=ctrls['text_atis'], inline=False)
    return embed
