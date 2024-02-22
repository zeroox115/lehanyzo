import discord 
from discord.ext import commands
import os
from dotenv import load_dotenv


load_dotenv()


intents = discord.Intents.all()
client = commands.Bot(command_prefix = '!', intents = intents)

@client.event
async def on_ready(): 
    await client.change_presence(activity=discord.Streaming(name="Twitch", url="https://www.twitch.tv/lehanyzo"))
    print('uwu')





client.run(os.getenv('TOKEN'))