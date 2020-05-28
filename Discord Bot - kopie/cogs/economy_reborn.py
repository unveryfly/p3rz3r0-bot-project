import discord
from discord.ext import commands
import discord.utils
import mysql.connector
import random

class Level(commands.Cog):

    def __init__(self, client):
        self.client = client

    red = 100
    pink = 160
    yellow = 75
    orange = 90
    green = 50
    blue = 150
    voicechanger = 6000


    mydb = mysql.connector.connect(
        host='localhost',
        user='yesyes not yours brugh',
        passwd='hmmmmmmmmmmmmmmmmm',
        database='levels',
        auth_plugin='mysql_native_password'
    )
    print(mydb)

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return

        xp = len(message.content)
        cursor = self.mydb.cursor()
        cursor.execute("SELECT * FROM users WHERE client_id = " + str(message.author.id))
        result = cursor.fetchall()
        if len(result) == 0:
            cursor.execute("INSERT INTO users VALUES(" + str(message.author.id) + "," + str(xp) + ", 1, 0, 0, 0, 0)")
            self.mydb.commit()
        else:
            currentXP = result[0][1] + xp
            addcoin = result[0][3] + xp
            cursor.execute("UPDATE users SET user_xp = " + str(currentXP) + " WHERE client_id = " + str(message.author.id))
            cursor.execute("UPDATE users SET user_coins = " + str(addcoin) + " WHERE client_id = " + str(message.author.id))
            lvl_end = int(currentXP ** (1/4))
            if result[0][2] < lvl_end:
                cursor.execute("UPDATE users SET user_level = " + str(lvl_end) + " WHERE client_id = " + str(message.author.id))
                await message.channel.send(f'{message.author.mention} reached level {lvl_end}')
            self.mydb.commit()

    @commands.command()
    async def coins(self, ctx, member: discord.Member):
        cursor = self.mydb.cursor()
        cursor.execute("SELECT user_coins FROM users WHERE client_id = " + str(member.id))
        result = cursor.fetchall()
        await ctx.send(f'{member.mention} has {result[0][0]} coins.')

    @commands.command()
    async def level(self, ctx, member: discord.Member):
        cursor = self.mydb.cursor()
        cursor.execute("SELECT user_level FROM users WHERE client_id = " + str(member.id))
        result = cursor.fetchall()
        await ctx.send(f'{member.mention} has {result[0][0]} level.')

    @commands.command()
    async def flipcoin(self, ctx, coin):
        cursor = self.mydb.cursor()
        cursor.execute("SELECT * FROM users WHERE client_id = " + str(ctx.author.id))
        result = cursor.fetchall()
        coins = result[0][3]
        if coins > int(coin):
            chance = random.randrange(100)
            print(chance)
            if chance > 50:
                newCoins = coins + int(coin)
                newWins = result[0][4] + 1
                newWS = result[0][6] + 1
                await ctx.send(f'{ctx.author.mention} just won {coin} coins!')
                cursor.execute("UPDATE users SET user_wins = " + str(newWins) + " WHERE client_id = " + str(ctx.author.id))
                cursor.execute("UPDATE users SET user_winstreak = " + str(newWS) + " WHERE client_id = " + str(ctx.author.id))
            else:
                newCoins = coins - int(coin)
                newLoss = result[0][5] + 1
                await ctx.send(f'{ctx.author.mention} just lost {coin} coins...')
                cursor.execute("UPDATE users SET user_losses = " + str(newLoss) + " WHERE client_id = " + str(ctx.author.id))
                cursor.execute("UPDATE users SET user_winstreak = " + "0" + " WHERE client_id = " + str(ctx.author.id))

            cursor.execute("UPDATE users SET user_coins = " + str(newCoins) + " WHERE client_id = " + str(ctx.author.id))
        
        self.mydb.commit()

    @commands.command()
    async def wins(self, ctx, member: discord.Member):
        cursor = self.mydb.cursor()
        cursor.execute("SELECT user_wins FROM users WHERE client_id = " + str(member.id))
        result = cursor.fetchall()
        await ctx.send(f'{member.mention} has {result[0][0]} wins.')

    @commands.command()
    async def losses(self, ctx, member: discord.Member):
        cursor = self.mydb.cursor()
        cursor.execute("SELECT user_losses FROM users WHERE client_id = " + str(member.id))
        result = cursor.fetchall()
        await ctx.send(f'{member.mention} has {result[0][0]} losses.')

    @commands.command()
    async def winstreak(self, ctx, member: discord.Member):
        cursor = self.mydb.cursor()
        cursor.execute("SELECT user_winstreak FROM users WHERE client_id = " + str(member.id))
        result = cursor.fetchall()
        await ctx.send(f'{member.mention} has a winstreak of {result[0][0]} wins.')

    @commands.command()
    async def buy(self, ctx, *, item):
        await self.buythis(ctx, ctx.author.id, item)

    async def buythis(self, ctx, user, item):
        thing = item.lower()
        thingy = eval('item.lower()')
        print(thingy)
        cursor = self.mydb.cursor()
        cursor.execute("SELECT user_coins FROM users WHERE client_id = " + str(user))
        result = cursor.fetchall()
        if result[0][0] > thingy:
            guild = ctx.guild
            role = discord.utils.get(guild.roles, name=item)
            newCoins = result[0][0] - thingy
            cursor.execute("UPDATE users SET user_coins = " + str(newCoins) + " WHERE client_id = " + str(user))
            await ctx.author.add_roles(role)

def setup(client):
    client.add_cog(Level(client))


