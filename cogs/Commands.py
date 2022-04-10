from discord.ext import commands
from discord import Embed, File
from Main import Functions

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
        

    
def setup(client):
    client.add_cog(Commands(client))