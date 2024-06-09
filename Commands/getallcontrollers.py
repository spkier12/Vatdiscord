import vatbot
import requests

@vatbot.tree.command(
    name="getallcontrollers",
    description="get all controllers online in a given country",
)
async def getallcontrollers(interaction: vatbot.discord.Interaction, icao: str):
    try:
        # Fetch data from Vatism api and convert to json
        url: str = "https://data.vatsim.net/v3/vatsim-data.json"
        res = requests.request("GET", url=url, headers={}, data={})
        controllers = res.json()["controllers"]

        ctrlsdata: list = []
        ctrlsdatacount: int = 0

        for ctrls in controllers:
            if str(ctrls['callsign']).startswith(icao):
                ctrlsdatacount += 1
                ctrlsdata.insert(ctrlsdatacount, f"{ctrls['callsign']}:{ctrls['frequency']}:{ctrls['name']}")
        await interaction.response.send_message(embed=await sendvatsimembed(ctrlsdata, icao))
        return

    except Exception as e:
        print(f"\n Error {e}")

async def sendvatsimembed(ctrlsdata: list, icao: str):
    embed = vatbot.discord.Embed(
        title=f"Controller information for {icao}",
        description=f"All Online vatsim data for {icao}",
        color=10
    )

    # Loop through all positions online and split observers/supervisors online out of picture and bad controllers
    for x in ctrlsdata:
        splitx = str(x).split(':')
        if splitx[1] != '199.998':
            embed.add_field(name=splitx[0], value=f"{splitx[1]}:{splitx[2]}")
            if str(splitx[2]).lower().startswith("roald"):
                embed.add_field(name="Bad Controller", value=f"**{splitx[2]} is Online**")
    return embed
