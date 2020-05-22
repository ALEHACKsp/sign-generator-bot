from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 

import discord
import config
from discord.ext import commands 

bot = commands.Bot(command_prefix="_")





@bot.event
async def on_ready():
    print("Bot online")
    for guild in bot.guilds:
      print("{} - {} members".format(guild.name, len(guild.members)))

@bot.event
async def on_command_error(ctx, e):
    if isinstance(e, commands.errors.CommandNotFound):
        pass # No need
    elif isinstance(e, commands.errors.BadArgument):
        await ctx.send("You provided a bad argument. Are you sure that I have access to that user or channel?")
    elif isinstance(e, commands.errors.MissingPermissions):
        await ctx.send("I'm sorry Dave, I'm afraid I can't do that. (Missing required permissions)")
    elif isinstance(e, commands.errors.CheckFailure):
        await ctx.send("You don't have permission to use this command.")
    elif isinstance(e, commands.errors.MissingRequiredArgument):
        await ctx.send("You're missing required arguments!")
    else:
        if ctx.command:
            await ctx.send("An error occurred while processing the `{}` command".format(ctx.command.name))
        print("Ignoring exception in command {} in channel {}".format(ctx.command, ctx.message.channel))
        
@bot.command() 
async def generate(ctx, top: str, *, bottom: str):
    img = Image.open("sign.png")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("abel-regular.ttf", 20)
    draw.text((230, 55),  top,(0,0,0),font=font)
    draw.text((230, 105), bottom,(0,0,0),font=font)

    img.save('sign-out.png')

    await ctx.send(file=discord.File("sign-out.png"))




bot.run(config.token)