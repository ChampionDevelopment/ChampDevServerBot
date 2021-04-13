import discord
from discord.ext import commands

class Info(commands.Cog):
  def __init__(self, client):
    self.client = client
  
  @commands.command(name="champdev", aliases=["cd", "cdinfo", "cdi"], description="Information on ChampionDevelopment")
  async def champdev(self, ctx):
    await ctx.send("<@654142589783769117> is the owner")

def setup(client):
  client.add_cog(Info(client))
  print("info is up")