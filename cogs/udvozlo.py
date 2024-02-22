import discord
from discord.ext import commands


class CogName(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_guild_join(self, guild:discord.Guild):
        print("hozzaadva: " + guild.name)

    @commands.Cog.listener()
    async def on_member_join(self, member:discord.Member):
        embed = discord.Embed(title=f"Üdvözlünk, {member.mention}!", description=f"Köszönjük, hogy csatlakozott szerverünkhöz, reméljük jól fogja érezni magát nálunk!", color=0x00ff00)
        csatorna = await self.bot.get_channel(1210291432124850196)
        uzenet = await csatorna.send(embed=embed)
        uzenet.add_reaction("🥶")


def setup(bot:commands.Bot):
    bot.add_cog(CogName(bot))