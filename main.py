# pog bot has been started nice

import discord
from discord.ext import commands
import os
intents = discord.Intents()
intents.guilds = True
intents.members = True
client = commands.Bot(command_prefix=">>", intents = intents, case_insensitive = True)
TOKEN = os.environ.get("TOKEN")

@client.event
async def on_ready():
    print("serverBot online")
    channel1 = client.get_channel(830120041705635840)
    await channel1.send("Wassup, ive become online")

@client.command(name="test", description = "its a test")
async def test(ctx):
    print("test")
    await ctx.delete()
    await ctx.send("test")

client.run(TOKEN)