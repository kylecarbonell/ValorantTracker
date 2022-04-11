from discord.ext import commands
from Main import Functions
from discord import Embed

class Commands(commands.Cog):
    def __init__(self, client):
        self.stat = Functions()
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Cog is ready")

    #Sends KD Ratio
    @commands.command()
    async def kd(self,ctx, user):
        await ctx.send(self.stat.getStat("K/D Ratio", user))

    @commands.command()
    async def link(ctx, getUser):
        link = getUser
        await ctx.send("ballz")

    @commands.command()
    async def hs(self,ctx, user):
        await ctx.send(self.stat.getStat("Headshots", user))

    @commands.command()
    async def wins(self,ctx, user):
        await ctx.send(self.stat.getStat("Wins", user)) 

    @commands.command()
    async def kills(self,ctx, user):
        await ctx.send(self.stat.getStat("Kills", user))

    @commands.command()
    async def aces(self,ctx, user):
        await ctx.send(self.stat.getStat("Ace", user))

    @commands.command()
    async def hikills(self,ctx, user):
        await ctx.send(self.stat.getStat("Most Kills (Match)", user))

    @commands.command()
    async def all(self,ctx):
        embed = Embed()
        embed.title = "Statistics"
        await ctx.send(embed)


    
def setup(client):
    client.add_cog(Commands(client))