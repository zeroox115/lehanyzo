import discord 
from discord.ext import commands
import os
from dotenv import load_dotenv


load_dotenv()


#get hex color code from env
def get_color():
    hex = os.getenv('HEX_COLOR_CODE')
    return discord.Colour(int(hex, 16))

intents = discord.Intents.all()
client = commands.Bot(command_prefix = '!', intents = intents)

@client.event
async def on_ready(): 
    await client.change_presence(activity=discord.Streaming(name="Twitch", url="https://www.twitch.tv/lehanyzo"))
    print('uwu')



@client.command()
async def ping(ctx):
    color = get_color()
    embed = discord.Embed(
        title = 'Pong!',
        description = f'A bot pingje: {round(client.latency * 1000)}ms',
        color = color
    )
    await ctx.send(embed=embed)




client.run(os.getenv('TOKEN'))