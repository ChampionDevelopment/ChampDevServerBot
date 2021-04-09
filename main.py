# pog bot has been started nice

import discord
from discord.ext import commands
import os
intents = discord.Intents()
intents.guild = True
intents.members = True
client = commands.Bot(command_prefix=when_mentioned_or("cd ", "cd"), intents = intents, case_insensitive = True)

@client.event
async def on_ready():
    print("serverBot online")
    channel1 = client.get_channel(830120041705635840)
    await channel1.send("Wassup, ive become online")

cogs = []