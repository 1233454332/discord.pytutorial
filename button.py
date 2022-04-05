import discord
from discord.ext import commands
from discord.ui import Button, View
intents = discord.Intents.default() 
intents.members = True 
intents.message_content = True 
client = commands.Bot(command_prefix="m!",help_command=None, intents=intents)

@client.command()
async def b(ctx):
  button = Button(label="押せ",style=discord.ButtonStyle.green)
  view = View()
  view.add_item(button)
  await ctx.send("ボタン", view=view)
  
