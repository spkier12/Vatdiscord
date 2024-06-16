import os

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
    client.run("MTI0OTM4Mjk4Njk5MTAwOTkzMw.GnvBhf._rkYibse4P7fRXh6_kly2LNKELuUxyUCTcqpzg")


