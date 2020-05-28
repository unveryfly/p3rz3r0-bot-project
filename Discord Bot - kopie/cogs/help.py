import discord
from discord.ext import commands

class Help(commands.Cog):
    
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(
            name='Help',
            description='Prefix: .',
            colour=0x2fe800)

        embed.set_author(name=ctx.author.name)
        embed.add_field(name='Moderation', value=f'ban [Member, Minutes], mute [Member, Minutes], muteVC [Member, Minutes], kick [Member] \n unban [Member], unmute [Member], unmuteVC[Member] \n Please keep in mind that these commands require a special role which has to be set by the owner! These commands can only be accessed by people which have View audit logs permission', inline=True)
        embed.add_field(name='Economy', value=f'shop, buy [item], level [Member], coins [Member], flipcoin [Coins], wins [Member], losses [Member], winstreak [Member] \n Roles need to be setuped by the owner in order for them to work!', inline=True)
        embed.add_field(name='Fun', value=f'avatar [member], .playlist (shows p3rz3r0s latest playlist), meme, dankmeme, meirl (You can react to that message with ✅ or ❌ if it is you irl.), tinder, cat, dog, koala, fox, birb, red_panda, panda, racoon, kangaroo, encrypt [message], decrypt [encrypted message]', inline=True)
        embed.add_field(name='Cogs', value=f'load [cog], unload [cog], reload [cog]') 

        await ctx.send(embed=embed) 

def setup(client):
    client.add_cog(Help(client))
