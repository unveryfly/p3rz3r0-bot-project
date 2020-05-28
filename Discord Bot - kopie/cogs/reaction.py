import discord
from discord.ext import commands
import asyncio
import json
import os
import discord.utils


class Reaction(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        message_id = payload.message_id
        if message_id == 710127770692485170:
            guild_id = payload.guild_id
            guild = discord.utils.find(lambda g : g.id == guild_id, self.client.guilds)

            role = discord.utils.get(guild.roles, name='Member')
            member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
            await member.add_roles(role)

def setup(client):
    client.add_cog(Reaction(client))
