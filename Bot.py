import discord
import os
import random
from discord.ext import commands


client  = commands.Bot('/')
TOKEN = 'ODA5NTUxMzgwOTIyMTA1ODY2.YCWveQ.PENDJaT4UnApVrokQlqKvWWpMXs'
client.remove_command('help')

@client.event
async def on_ready():
    print('We have logged')

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(TOKEN)