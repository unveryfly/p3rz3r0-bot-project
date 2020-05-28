import discord
from discord.ext import commands
import asyncio
class Moderation(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Mod is online.')
    
    @commands.command()
    @commands.has_permissions(view_audit_log=True)
    async def ban(self, ctx, member : discord.Member, minutes):
        guild = ctx.guild
        role = discord.utils.get(guild.roles, name="BANNED")
        if minutes == "999999":
            await ctx.send(f"@{member} was banned forever and can only be unbanned by staff")
            await member.add_roles(role)
        else:
            await ctx.send(f"@{member} was banned for {minutes} minutes")
            await member.add_roles(role)
            await asyncio.sleep(float(minutes)*60)
            await ctx.send(f"@{member} was unbanned after {minutes} minutes")
            await member.remove_roles(role)

    @commands.command()
    @commands.has_permissions(view_audit_log=True)
    async def mute(self, ctx, member: discord.Member, minutes):
        guild = ctx.guild
        role = discord.utils.get(guild.roles, name="Muted")
        if minutes == "999999":
            await ctx.send(f"@{member} was muted forever and can only be unmuted by staff")
            await member.add_roles(role)
        else:
            await ctx.send(f"@{member} was muted for {minutes} minutes")
            await member.add_roles(role)
            await asyncio.sleep(float(minutes)*60)
            await ctx.send(f"@{member} was unmuted after {minutes} minutes")
            await member.remove_roles(role)

    @commands.command()
    @commands.has_permissions(view_audit_log=True)
    async def muteVC(self, ctx, member: discord.Member, minutes):
        guild = ctx.guild
        role = discord.utils.get(guild.roles, name="Muted VC")
        if minutes == "999999":
            await ctx.send(f"@{member} was muted forever and can only be unmuted by staff")
            await member.add_roles(role)
        else:
            await ctx.send(f"@{member} was muted for {minutes} minutes")
            await member.add_roles(role)
            await asyncio.sleep(float(minutes)*60)
            await ctx.send(f"@{member} was unmuted after {minutes} minutes")
            await member.remove_roles(role)

    @commands.command()
    @commands.has_permissions(view_audit_log=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await ctx.send(f"@{member} was kicked from this server")
        await member.kick(reason)

    @commands.command()
    @commands.has_permissions(view_audit_log=True)
    async def unban(self, ctx, member: discord.Member):
        guild = ctx.guild
        role = discord.utils.get(guild.roles, name="BANNED")
        await ctx.send(f"@{member} was unbanned")
        await member.remove_roles(role)

    @commands.command()
    @commands.has_permissions(view_audit_log=True)
    async def unmute(self, ctx, member: discord.Member):
        guild = ctx.guild
        role = discord.utils.get(guild.roles, name="Muted")
        await ctx.send(f"@{member} was unmuted")
        await member.remove_roles(role)
    
    @commands.command()
    @commands.has_permissions(view_audit_log=True)
    async def unmuteVC(self, ctx, member: discord.Member):
        guild = ctx.guild
        role = discord.utils.get(guild.roles, name="Muted VC")
        await ctx.send(f"@{member} was unmuted")
        await member.remove_roles(role)

def setup(client):
    client.add_cog(Moderation(client))
