import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix=".")
token = os.environ.get("TOKEN")

@client.event
async def on_ready():
  print("ready")
  channel = await client.fetch_channel(830120041705635840)
  await channel.send("ready")

@client.command(name="e")
async def e(ctx):
  print("e")
  await ctx.send("e")

client.run(token)