import os
import settings
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

# Import all files in Commands direcotry
for files in os.listdir('./Commands'):
    if str(files).endswith('.py'):
        print(f"\n Importing {files}")

from Commands import (
    getflight,
    getcontrollers,
    getallcontrollers,
    getmetar)

def startbot():
    if settings.discordtoken == None:
        print("/n Discord Token is invalid and dosnt contain anything except None.. Shuting down bot")
        return
    client.run(settings.discordtoken)


