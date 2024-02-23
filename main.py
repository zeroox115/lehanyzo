import discord 
from discord.ext import commands
import os
from lib import lehanyzo as lehanyzo

#get hex color code from env
def get_color():
    hex = lehanyzo.get.env_var('HEX_COLOR_CODE')
    return discord.Colour(int(hex, 16))

intents = discord.Intents.all()
client = commands.Bot(command_prefix = '!', intents = intents, case_insensitive = True)

@client.event
async def on_ready(): 
    await client.change_presence(activity=discord.Streaming(name="Twitch", url="https://www.twitch.tv/lehanyzo"))
    print('uwu')
    cogok = ['cogs.twitch', 'cogs.udvozlo', 'cogs.reakcio_rangok', 'cogs.embedsay']
    for cog in cogok:
        client.load_extension(cog)




@client.command()
async def ping(ctx):
    color = get_color()
    embed = discord.Embed(
        title = 'Pong!',
        description = f'A bot pingje: {round(client.latency * 1000)}ms',
        color = color
    )
    embed.set_footer(text=lehanyzo.get.kranem_footer(lehanyzo.get.env_var('FOOTER'), "ping"))
    await ctx.send(embed=embed)




client.run(os.getenv('TOKEN'))