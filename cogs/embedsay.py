import discord
from discord.ext import commands

class EmbedSay(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="embedsay")
    async def embed_say(self, ctx, *args):
        title = args[0] if args else ""  
        description = " ".join(args[1:-1]) if len(args) > 2 else "" 
        footer = args[-1] if len(args) > 1 else "" 

        embed = discord.Embed(title=title, description=description, color=discord.Color.green())
        embed.set_footer(text=footer)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(EmbedSay(bot))
