import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print("Bot's ready")
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="on prefix '.'"))

client.remove_command('help')

@client.command()
async def load(ctx, extension):
    if ctx.author.id == 325972560346873858:
        client.load_extension(f'cogs.{extension}')
        await ctx.send(f'{extension} was loaded.')

@client.command()
async def unload(ctx, extension):
    if ctx.author.id == 325972560346873858:
        client.unload_extension(f'cogs.{extension}')
        await ctx.send(f'{extension} was unloaded')

@client.command()
async def reload(ctx, extension):
    if ctx.author.id == 325972560346873858:
        client.unload_extension(f'cogs.{extension}')
        client.load_extension(f'cogs.{extension}')
        await ctx.send(f'Reloaded {extension}, please check the console for any errors.')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

        
client.run('This code is a mystery hmm')


