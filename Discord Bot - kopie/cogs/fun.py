import discord
from discord.ext import commands
import praw
import random
import sr_api
from cryptography.fernet import Fernet



class Fun(commands.Cog):
    
    def __init__(self, client):
        self.client = client

#=========================  API Setups  ==========================#
#---PRAW API aka Reddit API---#
    reddit = praw.Reddit(client_id="not sure which",
                         client_secret="it is a secret so..",
                         password="It is my password not yours. Thats why reddit it deep web",
                         user_agent="P3rZ3r0's bot by /u/P3rZ3r0",
                         username="P3rZ3r0... yeah idc")
#---Some Random API---#
    srclient = sr_api.Client()
#---Cryptography---#
    file = open('key.key', 'rb')
    key = file.read()
    file.close()

#---Commands---#
#---Random CMDS---#
    @commands.command()
    async def avatar(self, ctx, member: discord.Member):
        embed = discord.Embed(
            title = f"{member.name}'s Avatar",
            description = f'{member.avatar_url_as(format="png")}',
            colour = discord.Colour.blue()
        )
        embed.set_image(url=f'{member.avatar_url_as(format="png")}')
        await ctx.send(embed=embed)

    @commands.command()
    async def playlist(self, ctx):
        await ctx.send("P3rZ3r0's playlist that he is currently updating. Please come back later if you already know about this since he is changing playlists each 3-6 months.")
        await ctx.send('https://open.spotify.com/playlist/7wjFX1jXT7b9KDWcEk91xf?si=IoOR9RuBRhmo6A72jMAvvA')

#---Reddit CMDS---#
    @commands.command()
    async def meme(self, ctx):
        print(self.reddit.user.me())
        sreddit = self.reddit.subreddit('memes')
        hot = sreddit.hot(limit=50)
        post = random.randint(1, 50)
        for i in range(0, post):
            subs = next(x for x in hot if not x.stickied)
            embed = discord.Embed(
                name='Memey',
                description='Memey from r/memes',
                colour=discord.Colour.blue())
            embed.set_image(url=f'{subs.url}')
        await ctx.send(embed=embed)

    @commands.command()
    async def dankmeme(self, ctx):
        print(self.reddit.user.me())
        sreddit = self.reddit.subreddit('dankmemes')
        hot = sreddit.hot(limit=50)
        post = random.randint(1, 50)
        for i in range(0, post):
            subs = next(x for x in hot if not x.stickied)
            embed = discord.Embed(
                name='Dank memey',
                description='Memey from r/dankmemes',
                colour=discord.Colour.green())
            embed.set_image(url=f'{subs.url}')
        await ctx.send(embed=embed)

    @commands.command()
    async def meirl(self, ctx):
        print(self.reddit.user.me())
        sreddit = self.reddit.subreddit('me_irl')
        hot = sreddit.hot(limit=50)
        post = random.randint(1, 50)
        for i in range(0, post):
            subs = next(x for x in hot if not x.stickied)
            embed = discord.Embed(
                name='You irl?',
                description='Memey from r/me_irl Is it you irl?',
                colour=discord.Colour.from_rgb(0, 0, 0))
            embed.set_image(url=f'{subs.url}')
        msg = await ctx.send(embed=embed)
        reacts = ['✅', '❌']
        for emo in reacts:
            await msg.add_reaction(emo)

    @commands.command()
    async def tinder(self, ctx):
        print(self.reddit.user.me())
        sreddit = self.reddit.subreddit('tinder')
        hot = sreddit.hot(limit=50)
        post = random.randint(1, 50)
        for i in range(0, post):
            subs = next(x for x in hot if not x.stickied)
            embed = discord.Embed(
                name='Tinder',
                description='Memey from r/tinder',
                colour=discord.Colour.purple())
            embed.set_image(url=f'{subs.url}')
        await ctx.send(embed=embed)

#---Some Random API CMDS---#
    @commands.command()
    async def cat(self, ctx):
        img = await self.srclient.get_image('cat')
        embed = discord.Embed(
            name='Cat',
            description='Image of a cat. This was provided by Some Random API.',
            colour=discord.Colour.from_hsv(255, 255, random.randint(0, 255)))
        embed.set_image(url=img.url)
        await ctx.send(embed=embed)
        random.seed()

    @commands.command()
    async def dog(self, ctx):
        img = await self.srclient.get_image('dog')
        embed = discord.Embed(
            name='Dog',
            description='Image of a dog. This was provided by Some Random API.',
            colour=discord.Colour.from_hsv(random.randint(0, 255), 255, random.randint(0, 255)))
        embed.set_image(url=img.url)
        await ctx.send(embed=embed)
        random.seed()
    
    @commands.command()
    async def koala(self, ctx):
        img = await self.srclient.get_image('koala')
        embed = discord.Embed(
            name='Koala',
            description='Image of a koala. This was provided by Some Random API.',
            colour=discord.Colour.from_hsv(255, 255, random.randint(0, 255)))
        embed.set_image(url=img.url)
        await ctx.send(embed=embed)
        random.seed()

    @commands.command()
    async def fox(self, ctx):
        img = await self.srclient.get_image('fox')
        embed = discord.Embed(
            name='Fox',
            description='Image of a fox. This was provided by Some Random API.',
            colour=discord.Colour.from_hsv(255, 255, random.randint(0, 255)))
        embed.set_image(url=img.url)
        await ctx.send(embed=embed)
        random.seed()

    @commands.command()
    async def bird(self, ctx):
        img = await self.srclient.get_image('birb')
        embed = discord.Embed(
            name='Koala',
            description='Image of a bird. This was provided by Some Random API.',
            colour=discord.Colour.from_hsv(255, 255, random.randint(0, 255)))
        embed.set_image(url=img.url)
        await ctx.send(embed=embed)
        random.seed()

    @commands.command()
    async def red_panda(self, ctx):
        img = await self.srclient.get_image('red_panda')
        embed = discord.Embed(
            name='Red panda',
            description='Image of a red panda. This was provided by Some Random API.',
            colour=discord.Colour.from_hsv(255, 255, random.randint(0, 255)))
        embed.set_image(url=img.url)
        await ctx.send(embed=embed)
        random.seed()

    @commands.command()
    async def panda(self, ctx):
        img = await self.srclient.get_image('panda')
        embed = discord.Embed(
            name='Panda',
            description='Image of a panda. This was provided by Some Random API.',
            colour=discord.Colour.from_hsv(255, 255, random.randint(0, 255)))
        embed.set_image(url=img.url)
        await ctx.send(embed=embed)
        random.seed()

    @commands.command()
    async def racoon(self, ctx):
        img = await self.srclient.get_image('racoon')
        embed = discord.Embed(
            name='Racoon',
            description='Image of a racoon. This was provided by Some Random API.',
            colour=discord.Colour.from_hsv(255, 255, random.randint(0, 255)))
        embed.set_image(url=img.url)
        await ctx.send(embed=embed)
        random.seed()

    @commands.command()
    async def kangaroo(self, ctx):
        img = await self.srclient.get_image('kangaroo')
        embed = discord.Embed(
            name='Kangaroo',
            description='Image of a kangaroo. This was provided by Some Random API.',
            colour=discord.Colour.from_hsv(255, 255, random.randint(0, 255)))
        embed.set_image(url=img.url)
        await ctx.send(embed=embed)
        random.seed()

    @commands.command()
    async def gay(self, ctx, member: discord.Member):
        col = random.randint(1, 6)
        avalcols=[discord.Colour.red(), discord.Colour.orange(), discord.Colour.from_rgb(255, 255, 0), discord.Colour.green(), discord.Colour.blue(), discord.Colour.magenta()]
        for i in range(1, col):
            color = next(x for x in avalcols)

        img = member.avatar_url_as(format="png")
        imgfin = await self.srclient.beta('gay', str(img))
        embed = discord.Embed(name='LGBT', 
                              description=f'It is {member.name}, in LGBT colors.',
                              colour=color)

        embed.set_image(url=f'{imgfin}')
        print(imgfin)
        await ctx.send(imgfin)
        await ctx.send(embed=embed)

#---Cryptography---#
    @commands.command()
    async def encrypt(self, ctx, *, message):
        encoded = message.encode()

        f = Fernet(self.key)
        encrypted = f.encrypt(encoded)
        messagefin = encrypted.decode()
        await ctx.send(messagefin)

    @commands.command()
    async def decrypt(self, ctx, message):
        decryptpls = message.encode()
        f = Fernet(self.key)
        encrypted = f.decrypt(decryptpls)
        messagefin = encrypted.decode()
        await ctx.send(messagefin)

def setup(client):
    client.add_cog(Fun(client))
