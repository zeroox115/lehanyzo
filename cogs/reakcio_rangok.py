import discord
from discord.ext import commands
import json

class ReakcioRangok(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.reakcio_uzenetek = {}
        self.load_config()

    def load_config(self):
        try:
            with open('config.json', 'r') as f:
                self.reakcio_uzenetek = json.load(f)
        except FileNotFoundError:
            self.reakcio_uzenetek = {}

    def save_config(self):
        with open('config.json', 'w') as f:
            json.dump(self.reakcio_uzenetek, f, indent=4)

    @commands.command(name="add")
    async def add_reaction_role_to_msg(self, ctx, uzenet_id, rang: discord.Role, emoji):
        try:
            uzenet_id = int(uzenet_id)
            uzenet = await ctx.channel.fetch_message(uzenet_id)

            if str(uzenet.id) not in self.reakcio_uzenetek:
                self.reakcio_uzenetek[str(uzenet.id)] = {}

            try:
                emoji = str(emoji)
                await uzenet.add_reaction(emoji)

            except discord.HTTPException:
                emoji_obj = discord.utils.get(self.bot.emojis, name=emoji)
                if emoji_obj is None:
                    await ctx.send("Nem letezik ilyen emoji.")
                    return
                emoji = str(emoji_obj)
                await uzenet.add_reaction(emoji)

            self.reakcio_uzenetek[str(uzenet.id)][emoji] = rang.id
            self.save_config()
            await ctx.message.add_reaction("✅")

        except (discord.NotFound, ValueError):
            await ctx.message.add_reaction("❌")


    @commands.command(name="remove")
    async def remove_reaction_role_to_msg(self, ctx, uzenet_id, emoji):
        try:
            uzenet_id = int(uzenet_id)
            uzenet = await ctx.channel.fetch_message(uzenet_id)

            try:
                emoji = str(emoji)
                await uzenet.remove_reaction(emoji, self.bot.user)
    
            except discord.HTTPException:
                emoji_obj = discord.utils.get(self.bot.emojis, name=emoji)
                if emoji_obj is None:
                    await ctx.send("Nem letezik ilyen emoji.")
                    return
                emoji = str(emoji_obj)
                await uzenet.remoev_reaction(emoji, self.bot.user)

            del self.reakcio_uzenetek[str(uzenet.id)][emoji]
            self.save_config()
            await ctx.message.add_reaction("✅")
        except (discord.NotFound, ValueError, KeyError):
            await ctx.message.add_reaction("❌")

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        uzenet_data = self.reakcio_uzenetek.get(str(payload.message_id))
        if uzenet_data:
            rang_id = uzenet_data.get(str(payload.emoji))
            if rang_id:
                guild = self.bot.get_guild(payload.guild_id)
                rang = guild.get_role(rang_id)
                if rang:
                    felhasznalo = guild.get_member(payload.user_id)
                    if felhasznalo:
                        await felhasznalo.add_roles(rang)

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        uzenet_data = self.reakcio_uzenetek.get(str(payload.message_id))
        if uzenet_data:
            rang_id = uzenet_data.get(str(payload.emoji))
            if rang_id:
                guild = self.bot.get_guild(payload.guild_id)
                rang = guild.get_role(rang_id)
                if rang:
                    felhasznalo = guild.get_member(payload.user_id)
                    if felhasznalo:
                        await felhasznalo.remove_roles(rang)

def setup(bot):
    bot.add_cog(ReakcioRangok(bot))
