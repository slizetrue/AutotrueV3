import discord
import os
import random
from discord.ext import commands
from time import sleep

class Social(commands.Cog):

    def _init_(self, client):
        self.client = client

    @commands.command()
    async def ig(self, ctx):
        await ctx.send(f'https://www.instagram.com/slizetrue/')


def setup(client):
    client.add_cog(Social(client))
