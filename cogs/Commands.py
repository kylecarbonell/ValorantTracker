from discord.ext import commands
from discord import Embed
from Main import Functions

class Commands(commands.Cog):
    def __init__(self, client):
        self.stat = Functions()
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Cog is ready")

    def getID(self, ctx):
        return self.stat.getId(str(ctx.message.author))

    @commands.command()
    async def help(self, ctx):
        embed = Embed()
        embed.title = "Commands"
        
        #Commands made
        embed.add_field(name="/kd", value="Sends your K/D Ratio", inline=False)
        embed.add_field(name="/hs", value="Sends the number of headshots you have", inline=False)
        embed.add_field(name="/wins", value="Sends the number of wins you have", inline=False)
        embed.add_field(name="/kills", value="Sends the number of kills you have", inline=False)
        embed.add_field(name="/aces", value="Sends the number of aces you have", inline=False)
        embed.add_field(name="/hikills", value="Sends the highest number of kills you've had", inline=False)
        embed.add_field(name="/all", value="Sends all your stats", inline=False)
        await ctx.send(embed=embed)

    #Sends KD Ratio
    @commands.command()
    async def kd(self,ctx,  user=None):
        if(user == None):
            user = self.getID(ctx=ctx)
        await ctx.send(self.stat.getStat("K/D Ratio", user))

    #Sends Headshots
    @commands.command()
    async def hs(self,ctx, user=None):
        if(user == None):
            user = self.getID(ctx=ctx)
        await ctx.send(self.stat.getStat("Headshots", user))

    #Sends number of wins
    @commands.command()
    async def wins(self,ctx, user=None):
        if(user == None):
            user = self.getID(ctx=ctx)
        await ctx.send(self.stat.getStat("Wins", user)) 

    #Sends number of kills 
    @commands.command()
    async def kills(self,ctx, user=None):
        if(user == None):
            user = self.getID(ctx=ctx)
        await ctx.send(self.stat.getStat("Kills", user))

    #Sends number of aces
    @commands.command()
    async def aces(self,ctx, user=None):
        if(user == None):
            user = self.getID(ctx=ctx)
        await ctx.send(self.stat.getStat("Ace", user))

    #Sends most kills in a game
    @commands.command()
    async def hikills(self,ctx, user=None):
        if(user == None):
            user = self.getID(ctx=ctx)
        await ctx.send(self.stat.getStat("Most Kills (Match)", user))

    @commands.command()
    async def all(self,ctx, user=None):
        if(user == None):
            user = self.getID(ctx=ctx)
        embed = self.stat.getAll(user)
        await ctx.send(embed = embed)

    @commands.command()
    async def connect(self, ctx, user):
        if(self.stat.connect(user=user, discord=str(ctx.message.author))):
            await ctx.send(str(ctx.message.author) + " has connected to " + user)
        else:
            await ctx.send(str(ctx.message.author) + " is already connected to a different user")
    
def setup(client):
    client.add_cog(Commands(client))