import discord
import os
from discord.ext import commands









bot = commands.Bot(command_prefix = 'fst!')





@bot.event
async def on_ready():
  # On run. Declares when ready
  await bot.change_presence(activity=discord.Game(name="fst!help"))
  print("Logged in as {0.user}".format(bot))









@bot.command(brief="- Returs the github page of the user and repo specified", usage=" - fst!ghub {user} {repo}")
async def ghub(ctx, user, repo):
  try:
    embedVar = discord.Embed(title="Repo Found:", color=0x00FF00)
    embedVar.add_field(name="Link: ", value="https://github.com/"+user+"/"+repo, inline=True)
    await ctx.send(embed=embedVar)
    
    await ctx.message.delete()
  except:
    embedVar = discord.Embed(title="Error:", color=0xFF0000)
    embedVar.add_field(name="Info:", value="Please make sure you supply the right arguments. Use fst!help for more info", inline=True)
    await ctx.send(embed=embedVar)
    
    await ctx.message.delete()

@bot.command(brief="- Returs the curseforge page of the mod specified", usage=" - fst!cf {slug}")
async def cf(ctx, slug):
  try:
    embedVar = discord.Embed(title="Curseforge:", color=0x00FF00)
    embedVar.add_field(name="Link: ", value="https://curseforge.com/minecraft/mc-mods/"+slug, inline=True)
    await ctx.send(embed=embedVar)
    await ctx.message.delete()
  except:
    embedVar = discord.Embed(title="Error:", color=0xFF0000)
    embedVar.add_field(name="Info:", value="Please make sure you supply the right arguments. Use fst!help for more info", inline=True)
    await ctx.send(embed=embedVar)
    
    await ctx.message.delete()







# start the bot
bot.run(os.getenv('TOKEN'))




