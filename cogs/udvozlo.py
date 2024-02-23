import discord
from discord.ext import commands
from lib import lehanyzo as lehanyzo


class Udvozlo(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot
        self.rangok = lehanyzo.get.env_var("RANGOK")
        self.udvozlo_csatorna_id = int(lehanyzo.get.env_var("UDVOZLO_CSATORNA_ID"))
        self.kilepes_csatorna_id = int(lehanyzo.get.env_var("KILEPES_CSATORNA_ID"))


    @commands.Cog.listener()
    async def on_guild_join(self, guild:discord.Guild):
        print("hozzaadva: " + guild.name)

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        csatorna = self.bot.get_channel(self.udvozlo_csatorna_id)
        embed = discord.Embed(title=f"Üdvözlünk, {member.name}! 👋", description=f"Köszönjük, hogy csatlakozott szerverünkhöz, reméljük jól fogja érezni magát nálunk!", color=0x00ff00)
        embed.set_thumbnail(url=member.avatar.url)
        await self.send_embed(embed)
        await self.give_roles(member)

    @commands.Cog.listener()
    async def on_member_remove(self, member: discord.Member):
        csatorna = self.bot.get_channel(self.kilepes_csatorna_id)
        embed = discord.Embed(title=f"{member.name} távozott 👋", description=f"Reméljük még találkozunk!", color=0xff0000)
        embed.set_thumbnail(url=member.avatar.url)
        await self.send_embed(embed)

    async def send_embed(self, embed, csatorna_id = None):
        csatorna = self.bot.get_channel(csatorna_id or self.udvozlo_csatorna_id)
        if csatorna:
            uzenet = await csatorna.send(embed=embed)
            await uzenet.add_reaction("🥶")
        else:
            print("Csatorna ID hibas.")

    async def give_roles(self, member: discord.Member):
        guild = member.guild
        for rang_id in self.rangok:
            rang_id = int(rang_id)
            rang = guild.get_role(rang_id)
            if rang:
                await member.add_roles(rang)


def setup(bot:commands.Bot):
    bot.add_cog(Udvozlo(bot))