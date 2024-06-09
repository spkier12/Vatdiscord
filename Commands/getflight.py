import vatbot
import requests

@vatbot.tree.command(
    name="getflights",
    description="Find a flight by ID or name",
    # guild=vatbot.discord.Object(id=971816793704386630)
)
async def getflights(interaction: vatbot.discord.Interaction, vname: str = "", vatid: int = 0, callsign: str = ""):
    try:
        # If Parameters are empty then exit function
        if vname == "" and vatid == 0 and callsign == "":
            await interaction.response.send_message("Name or CID cannot be empty, i can only check for either name or id")
            return

        # Fetch data from Vatism api and convert to json
        url: str = "https://data.vatsim.net/v3/vatsim-data.json"
        res = requests.request("GET", url=url, headers={}, data={})
        pilots = res.json()["pilots"]

        # Check if username is found or CID and return data and exit function
        for cid in pilots:
            if cid['cid'] == vatid or str(cid['name']).startswith(vname) or cid['callsign'] == callsign:
                await interaction.response.send_message(embed=await sendvatsimembed(interaction, cid))
                return
        await interaction.response.send_message(f"No flights was found by ID or name/callsign")
        return

    except Exception as err:
        print(f"\nError: {err}")

# Convert all flight profile data into embeds and return it back to main fucntion to be sendt
async def sendvatsimembed(interaction: vatbot.discord.Interaction, cid):
    embed = vatbot.discord.Embed(
        title=f"Flight for {cid['name']}",
        description=f"Live Vatsim data for {cid['callsign']}",
        color=58
    )
    embed.add_field(name='Vatsim ID', value=cid['cid'], inline=True)
    embed.add_field(name='Callsign', value=cid['callsign'], inline=True)
    embed.add_field(name='From-TO', value=f"{cid['flight_plan']['departure']}:{cid['flight_plan']['arrival']}", inline=True)
    embed.add_field(name='Heading and speed', value=f"{cid['heading']}:{cid['groundspeed']}", inline=True)
    embed.add_field(name='Transponder', value=cid['transponder'], inline=True)
    embed.add_field(name='Route', value=cid['flight_plan']['route'], inline=True)
    embed.add_field(name='Vatsim ID', value=cid['cid'], inline=True)
    embed.add_field(name='Latitude', value=cid['latitude'], inline=True)
    embed.add_field(name='Longitude', value=cid['longitude'], inline=True)
    embed.add_field(name='Live Map', value=f"https://simaware.ca/?user={cid['cid']}", inline=True)
    return embed
