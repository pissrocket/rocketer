import asyncio
import random

import discord
from discord.ext import commands

import tax
from db import database


class Coin:
    def __init__(self, bot):
        self.bot = bot                                  # The bot object.
        self.coinActive = True                          # If this is set to false, the coin interval is stopped.
        self.database = database.Database(self.bot)     # database object -> used to update and get coin amount
        self.tax = tax.Tax(self.bot)                    # Tax object used to get the value of taxable
        self.COIN_AMOUNT = 1                           # amount of coins to be given every interval
        self.COIN_INTERVAL = 30                          # interval in seconds for sending out coins.

    @commands.command(name="coins", pass_context=True, help="Get your coin amount")
    async def coins(self, ctx):
        await self.bot.say("{}, you have {} coins".format(ctx.message.author.mention,
                                                          self.database.get_coins(ctx.message.author.id)))

    """@commands.command(name="roll", pass_context=True, help="Gamble coins, reach over 50 - 100")
    async def luck(self, ctx, amount):
        if float(amount) <= 0 :
            await self.bot.say("{}, please enter a valid amount?".format(ctx.message.author.mention))
            return None

        if not self.check_balance(ctx.message.author, float(amount)):
            await self.bot.say("{}, sorry buddy.. you do not have enough coins to do this bet.. You got {}"
                               .format(ctx.message.author.mention, self.database.get_coins(ctx.message.author.id)))
            return None

        rolled = random.randint(0,100)
        if rolled <= 50 :
            self.database.remove_coins(ctx.message.author.id, amount, ctx.message.author.mention)
            await self.bot.say("{}, you lost.. you rolled {} and lost {} coins".format(
                ctx.message.author.mention, rolled, amount))
            pass
        else :

            self.database.insert_coins(ctx.message.author.id, amount, ctx.message.author.mention)
            await self.bot.say(
                "{}, you won! you rolled {} and won {} coins".format(ctx.message.author.mention, rolled, amount))
            pass"""

    @commands.command(name="donate", pass_context=True)
    async def give(self, ctx, toUser :discord.Member, coins):
        member = toUser
        if member is not None :
            if self.check_balance(ctx.message.author, float(coins)):
                if float(coins) > 0 :

                    self.database.remove_coins(userid=ctx.message.author.id, coins=coins, mention=ctx.message.author.mention)
                    self.database.insert_coins(userid=member.id, coins=coins, mention=ctx.message.author.mention)
                    await self.bot.say("{}, you donated {} coins to {}".format(ctx.message.author.mention, coins,
                                                                               member.mention))

                else: await self.bot.say("{}, coins needs to be higher than 0.".format(ctx.message.author.mention))
            else: await self.bot.say("{}, not enough coins.".format(ctx.message.author.mention))
        else: await self.bot.say("Did not find member {}".format(toUser))

    @commands.command(name="toplist", pass_context=False)
    async def toplist(self):
        output = "On the coin top we got: \n \n"
        count = 1
        for user in self.database.get_top_coin_holders() :
            if user["mention"] == None :    # if for some reason mention is not in the db.. Then get it..
                user["mention"] = await self.bot.get_user_info(user["userid"])
                user["mention"] = user["mention"].mention

            output += "#{} {} with {} coins \n".format(count, user["mention"], user["coins"])
            count += 1
        await self.bot.say(output)


    def check_balance(self,user, requestedBalance):
        '''
        check if the user have enough coins to do the transaction 
        :param user: 
        :param requestedBalance: 
        :return: 
        '''
        if self.database.get_coins(user.id) < float(requestedBalance):
            return False
        return True

    
def setup(bot):
    bot.add_cog(Coin(bot))



