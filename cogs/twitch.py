import discord
from discord.ext import commands, tasks
import aiohttp
import asyncio
from lib import lehanyzo as lehanyzo


class StreamWatcher(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.csatorna_id = int(lehanyzo.get.env_var("STREAM_CSATORNA_ID"))
        self.twitch_client_id = "kimne78kx3ncx6brgo4mv6wki5h1ko" #public client_id soo lopjatok nyugodtan 🤟
        self.lista = {"lehanyzo": False} 
        self.check_stream_status.start()
        self.debug_mode = lehanyzo.get.debug_mode()

    @tasks.loop(seconds=45)
    async def check_stream_status(self):
        if self.debug_mode:
            print("task meghivva")
        channel = self.bot.get_channel(self.csatorna_id)
        if channel:
            for username, stream_status in self.lista.items():
                stream_allapota = await lehanyzo.get.stream_allapot(self.twitch_client_id, username)
                if stream_allapota and not stream_status:  
                    await channel.send(f"{username} elindította a streamet!\nhttps://www.twitch.tv/{username}")
                elif not stream_allapota and stream_status:  
                    await channel.send(f"{username} befejezte a streamet!")
                self.lista[username] = stream_allapota  

    @check_stream_status.before_loop
    async def before_check_stream_status(self):
        await self.bot.wait_until_ready()

def setup(bot):
    bot.add_cog(StreamWatcher(bot))
