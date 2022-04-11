from discord.ext import commands
from discord import Embed, File
from Main import Functions

class Commands(commands.Cog):
    user = "hi"
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


    
def setup(client):
    client.add_cog(Commands(client))