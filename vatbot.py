import discord
from discord import app_commands

class DiscordBot(discord.Client):
    async def on_ready(self):
        global treesynced
        print(f"\n Logged on as {self.user}")
        if not treesynced:
            await tree.sync()
            print("\n Tree synced..")
            treesynced = True


intents = discord.Intents.default()
intents.message_content = False
client = DiscordBot(intents=intents)
tree = app_commands.CommandTree(client)
treesynced = False

from Commands import getflight, getcontrollers, getallcontrollers

def startbot():
    client.run("OTgzMzYwNjkzOTYzMjE4OTQ1.GY6Aun.xvkt30YTDxueczecwiKzJvmHYmB_GWujMI3Itw")


# guild=discord.Object(id=971816793704386630)
