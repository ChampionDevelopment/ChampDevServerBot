import discord
from discord.ext import commands
from discord.ext.commands import BucketType as bt
import os

client = commands.Bot(command_prefix=".", case_insensitive = True, owner_ids={654142589783769117})
token = os.environ.get("TOKEN")

#Events
@client.event
async def on_command_error(ctx, error):
  if isinstance(error, discord.ext.commands.errors.CommandOnCooldown):
    await ctx.send(f"This command is on cooldown for {round(error.cooldown.per)} seconds. \nTry again after {round(error.retry_after)} seconds.")
  elif isinstance(error, discord.ext.commands.CommandNotFound):
    await ctx.send("No such command, try again.")

@client.event
async def on_ready():
  print("ready")
  channel = await client.fetch_channel(830120041705635840)
  await channel.send("ready")

#commands
class SpecialHelp(commands.MinimalHelpCommand):
  async def send_pages(self):
        destination = self.get_destination()
        self.no_category = "Miscellaneous"
        for page in self.paginator.pages:
            embed = discord.Embed(title = "Help", description=page, color=discord.Color(0x1ae7ff))
            await destination.send(embed=embed)
client.help_command= SpecialHelp()

@client.command(name="e", description="Dont ask, just try.")
@commands.cooldown(1, 600, bt.user)
async def e(ctx):
  print("e")
  await ctx.send("e")

@client.command(name="eval", description = "eval command for owners only")
@commands.is_owner()
async def _eval(ctx, *, code):
  await ctx.send(eval(code))

#cogs
cogs = ["cogs.info"]
for cog in cogs:
  try:
    client.load_extension(cog)
  except Exception as e:
    print(e)

@client.command(name = "loadcog", description="load a cog", aliases=["lc"])
async def loadcog(ctx, *, cogname):
  try:
    client.load_extension(cogname)
    await ctx.send("successfully loaded {0}".format(cogname))
  except Exception as e:
    print(e)

@client.command(name = "unloadcog", description="unload a cog", aliases=["uc"])
async def unloadcog(ctx, *, cogname):
  try:
    client.unload_extension(cogname)
    await ctx.send("successfully unloaded {0}".format(cogname))
  except Exception as e:
    print(e)

@client.command(name = "reloadcog", description="reload a cog", aliases=["rc"])
async def reloadcog(ctx, *, cogname):
  try:
    client.reload_extension(cogname)
    await ctx.send("successfully reloaded {0}".format(cogname))
  except Exception as e:
    print(e)
client.run(token)