import discord
from discord.ext import commands
import asyncio
import time
import random
import aiohttp
import re
import datetime
import traceback
import os
import sys

version = "0.4.5"
owner = ["361534796830081024"]
bot = commands.Bot(command_prefix='r-', description=None)
message = discord.Message
Staff_Member = ["424927133522067467"]
server = discord.Server
member = discord.Member

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    print(discord.utils.oauth_url(bot.user.id))
    await bot.change_presence(game=discord.Game(name='Hmmmm... :))'))   

@bot.command()
async def game(play):
    await bot.change_presence(game=discord.Game(name=play))
    em = discord.Embed(title="Game Status", description=f"Game status changed to __{play}__!", colour=0x3498db)
    await bot.say(embed=em)

@bot.command(pass_context=True)
async def suggest(ctx, pref, text):
    try:
        if pref is "S":
            msg = "𝓢𝓾𝓰𝓰𝒆𝓼𝓽𝓲𝓸𝓷"
        if pref is "Q":
            msg = "𝓠𝓾𝒆𝓼𝓽𝓲𝓸𝓷"
    except discord.Exceptions.UnboundLocalError:
        bot.say("**Please use a valid prefix! The available prefixes: __Q__, __S__**")
    finally:
        colours = [0x11806a, 0x1abc9c, 0x2ecc71, 0x1f8b4c, 0x3498db, 0x206694, 0x9b59b6, 0x71368a, 0xe91e63, 0xad1457, 0xf1c40f, 0xc27c0e, 0xe67e22, 0xa84300, 0xe74c3c, 0x992d22, 0x95a5a6, 0x607d8b, 0x979c9f, 0x546e7a]
        col = random.choice(colours)
        em = discord.Embed(title=f"{msg}", description=f"**From {member.nick}**\n⋙ {text}", colour=col)
        channel = bot.get_channel(id="444837114258128916")
        room = bot.get_channel(id="444837114258128916")
        await bot.reply(f"**:white_check_mark: Sent in {channel}**")
        await bot.send_message(room, embed=em)

@bot.command()
async def polladd(emote):
    msg = await bot.send_message(message.channel, "**A Poll has started! `24 hour remaining`**")
        if emote == "yes":
            await bot.add_reaction(msg, "\U0001F44D")
        elif emote == "no":
            await bot.add_reaction(msg, "\U0001F44E")
        elif emote == "one":
            await bot.add_reaction(msg, u"\u0031")
        elif emote == "two":
            await bot.add_reaction(msg, u"\u0032")
        elif emote == "three":
            await bot.add_reaction(msg, u"\u0033")
        elif emote == "four":
            await bot.add_reaction(msg, u"\u0034")
        elif emote == "five":
            await bot.add_reaction(msg, u"\u0035")
        elif emote == "six":
            await bot.add_reaction(msg, u"\u0036")
        elif emote == "seven":
             await bot.add_reaction(msg, u"\u0037")
        elif emote == "eight":
            await bot.add_reaction(msg, u"\u0038")
        elif emote == "nine":
             await bot.add_reaction(msg, u"\u0039")
        elif emote == "zero":
            await bot.add_reaction(msg, u"\u0030")
    await asyncio.sleep(86400)
    await bot.send_message(message.channel, "**:alarm_clock: The Poll has ended**!")

@bot.command()
async def joined(member):
    if member is None:
        member = message.author
    await bot.say(f'{member.name} joined in {member.joined_at}')
    
@bot.event
async def on_message(message):
    if message.content.upper().startswith('R-AMIOWNER?'):
        if message.author.id in owner:
            await bot.send_message(message.channel, ':white_check_mark: **You are the Owner.**')
        else:
            await bot.send_message(message.channel, ':negative_squared_cross_mark: **You aren\'t the Owner.**')
    if message.content.startswith('r-ping'):
        e = discord.Embed(title=':ping_pong: **Pong!**', colour=0x3498db)
        msg = await bot.send_message(message.channel, embed=e)
        ping = time.time()
        complete = "Its %.8f MS" % ping
        em = discord.Embed(title=complete, colour=0x3498db)
        await bot.edit_message(msg, embed=em)
    if message.content.startswith('r-say'):
        args = message.content.split(' ')
        await bot.send_message(message.channel, '**%s**' % (' '.join(args[1:])))
    if message.content.startswith('r-bigdigits'):
        await bot.send_message(message.channel, ':globe_with_meridians: **DIGITS:\n'
                               '-Zero, One, Two, Three, Four, Five, Six, Seven, Eight, Nine\n'
                               'Type `r-digits {0-9}` for the digits**')
    if message.content.startswith('r-digits 0'):
        await bot.send_message(message.channel, ':radio_button: **Zero:**')
        await bot.send_message(message.channel, ":black_circle::large_blue_circle::large_blue_circle::large_blue_circle::black_circle:\n" 
                                    ":large_blue_circle::black_circle::black_circle::black_circle::large_blue_circle:\n"
                                    ":large_blue_circle::black_circle::black_circle::black_circle::large_blue_circle:\n"
                                    ":large_blue_circle::black_circle::black_circle::black_circle::large_blue_circle:\n"
                                    ":large_blue_circle::black_circle::black_circle::black_circle::large_blue_circle:\n"
                                    ":large_blue_circle::black_circle::black_circle::black_circle::large_blue_circle:\n"
                                    ":black_circle::large_blue_circle::large_blue_circle::large_blue_circle::black_circle:")
    if message.content.startswith('r-digits 1'):
        await bot.send_message(message.channel, ':radio_button: **One:**')
        await bot.send_message(message.channel, ":black_circle::black_circle::large_blue_circle::black_circle::black_circle:\n"
                                ":black_circle::large_blue_circle::large_blue_circle::black_circle::black_circle:\n"
                                ":black_circle::black_circle::large_blue_circle::black_circle::black_circle:\n"
                                ":black_circle::black_circle::large_blue_circle::black_circle::black_circle:\n"
                                ":black_circle::black_circle::large_blue_circle::black_circle::black_circle:\n"
                                ":black_circle::black_circle::large_blue_circle::black_circle::black_circle:\n"
                                ":black_circle::large_blue_circle::large_blue_circle::large_blue_circle::black_circle:\n")
    if message.content.startswith('r-digits 2'):
        await bot.send_message(message.channel, ':radio_button: **Two:**')
        await bot.send_message(message.channel, ":black_circle::large_blue_circle::large_blue_circle::large_blue_circle::black_circle:\n"
                               ":large_blue_circle::black_circle::black_circle::black_circle::large_blue_circle:\n"
                               ":black_circle::black_circle::black_circle::large_blue_circle::black_circle:\n"
                               ":black_circle::black_circle::large_blue_circle::black_circle::black_circle:\n"
                               ":black_circle::large_blue_circle::black_circle::black_circle::black_circle:\n"
                               ":large_blue_circle::black_circle::black_circle::black_circle::black_circle:\n"
                               ":large_blue_circle::large_blue_circle::large_blue_circle::large_blue_circle::large_blue_circle:")
    if message.content.startswith('r-digits 3'):
        await bot.send_message(message.channel, ':radio_button: **Three:**')
        await bot.send_message(message.channel, ":black_circle::large_blue_circle::large_blue_circle::large_blue_circle::black_circle:\n"
                               ":large_blue_circle::black_circle::black_circle::black_circle::large_blue_circle:\n"
                               ":black_circle::black_circle::black_circle::black_circle::large_blue_circle:\n"
                               ":black_circle::black_circle::large_blue_circle::large_blue_circle::large_blue_circle:\n"
                               ":black_circle::black_circle::black_circle::black_circle::large_blue_circle:\n"
                               ":large_blue_circle::black_circle::black_circle::black_circle::large_blue_circle:\n"
                               ":black_circle::large_blue_circle::large_blue_circle::large_blue_circle::black_circle:")
    if message.content.startswith('r-digits 4'):
        await bot.send_message(message.channel, ':radio_button: **Four:**')
        await bot.send_message(message.channel, ":black_circle::black_circle::black_circle::large_blue_circle::black_circle:\n"
                               ":black_circle::black_circle::large_blue_circle::large_blue_circle::black_circle:\n"
                               ":black_circle::large_blue_circle::black_circle::large_blue_circle::black_circle:\n"
                               ":large_blue_circle::black_circle::black_circle::large_blue_circle::black_circle:\n"
                               ":large_blue_circle::black_circle::black_circle::large_blue_circle::black_circle:\n"
                               ":large_blue_circle::large_blue_circle::large_blue_circle::large_blue_circle::large_blue_circle:\n"
                               ":black_circle::black_circle::black_circle::large_blue_circle::black_circle:")
    if message.content.startswith('r-digits 5'):
        await bot.send_message(message.channel, ':radio_button: **Five:**')
        await bot.send_message(message.channel, ":large_blue_circle::large_blue_circle::large_blue_circle::large_blue_circle::black_circle:\n"
                               ":large_blue_circle::black_circle::black_circle::black_circle::black_circle:\n"
                               ":large_blue_circle::black_circle::black_circle::black_circle::black_circle:\n"
                               ":large_blue_circle::large_blue_circle::large_blue_circle::black_circle::black_circle:\n"
                               ":black_circle::black_circle::black_circle::large_blue_circle::black_circle:\n" 
                               ":black_circle::black_circle::black_circle::large_blue_circle::black_circle:\n"
                               ":large_blue_circle::large_blue_circle::large_blue_circle::black_circle::black_circle:")
    if message.content.startswith('r-digits 6'):
        await bot.send_message(message.channel, ':radio_button: **Six:**')
        await bot.send_message(message.channel, ":black_circle::large_blue_circle::large_blue_circle::large_blue_circle::black_circle:\n"
                               ":large_blue_circle::black_circle::black_circle::black_circle::black_circle:\n"
                               ":large_blue_circle::black_circle::black_circle::black_circle::black_circle:\n"
                               ":large_blue_circle::large_blue_circle::large_blue_circle::large_blue_circle::black_circle:\n"
                               ":large_blue_circle::black_circle::black_circle::black_circle::large_blue_circle:\n"
                               ":large_blue_circle::black_circle::black_circle::black_circle::large_blue_circle:\n"
                               ":black_circle::large_blue_circle::large_blue_circle::large_blue_circle::black_circle:")
    if message.content.startswith('r-digits 7'):
        await bot.send_message(message.channel, ':radio_button: **Seven:**')
        await bot.send_message(message.channel, ":black_circle::black_circle::black_circle::black_circle::black_circle:\n"
                               ":large_blue_circle::large_blue_circle::large_blue_circle::large_blue_circle::large_blue_circle:\n"
                               ":black_circle::black_circle::black_circle::black_circle::large_blue_circle:\n"
                               ":black_circle::black_circle::black_circle::large_blue_circle::black_circle:\n"
                               ":black_circle::black_circle::large_blue_circle::black_circle::black_circle:\n"
                               ":black_circle::large_blue_circle::black_circle::black_circle::black_circle:\n"
                               ":black_circle::large_blue_circle::black_circle::black_circle::black_circle:")
    if message.content.startswith('r-digits 8'):
        await bot.send_message(message.channel, ':radio_button: **Eight:**')
        await bot.send_message(message.channel, ":black_circle::large_blue_circle::large_blue_circle::large_blue_circle::black_circle:\n"
                               ":large_blue_circle::black_circle::black_circle::black_circle::large_blue_circle:\n"
                               ":large_blue_circle::black_circle::black_circle::black_circle::large_blue_circle:\n"
                               ":black_circle::large_blue_circle::large_blue_circle::large_blue_circle::black_circle:\n"
                               ":large_blue_circle::black_circle::black_circle::black_circle::large_blue_circle:\n"
                               ":large_blue_circle::black_circle::black_circle::black_circle::large_blue_circle:\n"
                               ":black_circle::large_blue_circle::large_blue_circle::large_blue_circle::black_circle:")
    if message.content.startswith('r-digits 9'):
        await bot.send_message(message.channel, ':radio_button: **Nine:**')
        await bot.send_message(message.channel, ":black_circle::large_blue_circle::large_blue_circle::large_blue_circle::black_circle:\n"
                               ":large_blue_circle::black_circle::black_circle::black_circle::large_blue_circle:\n"
                               ":large_blue_circle::black_circle::black_circle::black_circle::large_blue_circle:\n"
                               ":black_circle::large_blue_circle::large_blue_circle::large_blue_circle::large_blue_circle:\n"
                               ":black_circle::black_circle::black_circle::black_circle::large_blue_circle:\n"
                               ":black_circle::black_circle::black_circle::black_circle::large_blue_circle:\n"
                               ":black_circle::large_blue_circle::large_blue_circle::large_blue_circle::black_circle:")
    if message.content.startswith('r-8ball'):
        await bot.send_message(message.channel, random.choice(['**It is certain :8ball:**',
                                                              '**It is decidedly so :8ball:**',
                                                              '**Without a doubt :8ball:**',
                                                              '**No U :8ball:**',
                                                              '**Boi, go sleep... :8ball:**',
                                                              '**As i see it, yes :8ball:**',
                                                              '**As i see it, *No U*   :8ball:**',
                                                              '**Most likely :8ball:**',
                                                              '**Outlook good :8ball:**',
                                                              '**Yes :8ball:**',
                                                              '**Signs point to yes :8ball:**',
                                                              '**Reply hazy try again :8ball:**',
                                                              '**Ask again later, nub :8ball:**',
                                                              '**Better not tell you :8ball:**',
                                                              '**Cannot predict now :8ball:**',
                                                              '**Concentrate and ask again :8ball:**',
                                                              '**8ball.exe not found :8ball:**',
                                                              '**Dont count on it :8ball:**',
                                                              '**My reply is no :8ball:**',
                                                              '**My sources say no :8ball:**',
                                                              '**Outloook not so good :8ball:**',
                                                              '**Very doubtful :8ball:**',
                                                              '**Ha! :8ball:**',
                                                              '**Ask it to ur mum :8ball:**',
                                                              '**:feelsUltraREE: *REEEE* :8ball:**',]))
    if message.content.startswith('r-lenny'):
        ears = ['q{}p', 'ʢ{}ʡ', '⸮{}?', 'ʕ{}ʔ', 'ᖗ{}ᖘ', 'ᕦ{}ᕥ', 'ᕦ({})ᕥ', 'ᕙ({})ᕗ', 'ᘳ{}ᘰ', 'ᕮ{}ᕭ', 'ᕳ{}ᕲ', '({})', '[{}]', '୧{}୨', '୨{}୧', '⤜({})⤏', '☞{}☞', 'ᑫ{}ᑷ', 'ᑴ{}ᑷ', 'ヽ({})ﾉ', '乁({})ㄏ', '└[{}]┘', '(づ{})づ', '(ง{})ง', '|{}|']
        eyes = ['⌐■{}■', ' ͠°{} °', '⇀{}↼', '´• {} •`', '´{}`', '`{}´', 'ó{}ò', 'ò{}ó', '>{}<', 'Ƹ̵̡ {}Ʒ', 'ᗒ{}ᗕ', '⪧{}⪦', '⪦{}⪧', '⪩{}⪨', '⪨{}⪩', '⪰{}⪯', '⫑{}⫒', '⨴{}⨵', "⩿{}⪀", "⩾{}⩽", "⩺{}⩹", "⩹{}⩺", "◥▶{}◀◤", "≋{}≋", "૦ઁ{}૦ઁ", "  ͯ{}  ͯ", "  ̿{}  ̿", "  ͌{}  ͌", "ළ{}ළ", "◉{}◉", "☉{}☉", "・{}・", "▰{}▰", "ᵔ{}ᵔ", "□{}□", "☼{}☼", "*{}*", "⚆{}⚆", "⊜{}⊜", ">{}>", "❍{}❍", "￣{}￣", "─{}─", "✿{}✿", "•{}•", "T{}T", "^{}^", "ⱺ{}ⱺ", "@{}@", "ȍ{}ȍ", "x{}x", "-{}-", "${}$", "Ȍ{}Ȍ", "ʘ{}ʘ", "Ꝋ{}Ꝋ", "๏{}๏", "■{}■", "◕{}◕", "◔{}◔", "✧{}✧", "♥{}♥", " ͡°{} ͡°", "¬{}¬", " º {} º ", "⍜{}⍜", "⍤{}⍤", "ᴗ{}ᴗ", "ಠ{}ಠ", "σ{}σ"]
        mouth = ['v', 'ᴥ', 'ᗝ', 'Ѡ', 'ᗜ', 'Ꮂ', 'ヮ', '╭͜ʖ╮', ' ͟ل͜', ' ͜ʖ', ' ͟ʖ', ' ʖ̯', 'ω', '³', ' ε ', '﹏', 'ل͜', '╭╮', '‿‿', '▾', '‸', 'Д', '∀', '!', '人', '.', 'ロ', '_', '෴', 'ѽ', 'ഌ', '⏏', 'ツ', '益']
        lenny = random.choice(ears).format(random.choice(eyes)).format(random.choice(mouth))
        await bot.send_message(message.channel, "**A wild Lenny has appeard:**\n\n\t" + lenny)
    if message.content.startswith('r-verify'):
        room = bot.get_channel(id='420141568486408203')
        em = discord.Embed(title='VERIFICATION', description='**Hey __' + message.author.name + '__, if you want to get verified, you need to answer 3 questions:\n'
                                ':one: Do you play __.io games__?\n'
                                ':two: What else games do you play?\n'
                                ':three: How did you get here?\n'
                                '__Note__: if you play a game, and you want to get this game\'s special role, you need to ask it to an Admin (or higher) in {0.mention}, __and you must certify it!__)\n'
                                '\n'
                                '__Type `!verify` to finish the verification__**'.format(room), colour=0x3498db)
        em.set_thumbnail(url=message.author.avatar_url)
        await bot.send_message(message.channel, embed=em)
    if message.content.startswith('r-leavepls'):
        em5 = discord.Embed(title=":warning: WARNING :warning:", description="THE BOT WILL LEAVE THE SERVER IN:\n"
                            ":large_blue_circle::large_blue_circle::large_blue_circle::large_blue_circle::black_circle:\n"
                            ":large_blue_circle::black_circle::black_circle::black_circle::black_circle:\n"
                            ":large_blue_circle::black_circle::black_circle::black_circle::black_circle:\n"
                            ":large_blue_circle::large_blue_circle::large_blue_circle::black_circle::black_circle:\n"
                            ":black_circle::black_circle::black_circle::large_blue_circle::black_circle:\n" 
                            ":black_circle::black_circle::black_circle::large_blue_circle::black_circle:\n"
                            ":large_blue_circle::large_blue_circle::large_blue_circle::black_circle::black_circle:", colour=0x3498db)
        msg = await bot.send_message(message.channel, embed=em5)
        await asyncio.sleep(1)
        em4 = discord.Embed(title=":warning: WARNING :warning:", description="THE BOT WILL LEAVE THE SERVER IN:\n"
                            ":black_circle::black_circle::black_circle::large_blue_circle::black_circle:\n"
                            ":black_circle::black_circle::large_blue_circle::large_blue_circle::black_circle:\n"
                            ":black_circle::large_blue_circle::black_circle::large_blue_circle::black_circle:\n"
                            ":large_blue_circle::black_circle::black_circle::large_blue_circle::black_circle:\n"
                            ":large_blue_circle::black_circle::black_circle::large_blue_circle::black_circle:\n"
                            ":large_blue_circle::large_blue_circle::large_blue_circle::large_blue_circle::large_blue_circle:\n"
                            ":black_circle::black_circle::black_circle::large_blue_circle::black_circle:", colour=0x3498db)
        await bot.edit_message(msg,  embed=em4)
        await asyncio.sleep(1)
        em3 = discord.Embed(title=":warning: WARNING :warning:", description="THE BOT WILL LEAVE THE SERVER IN:\n"
                            ":black_circle::large_blue_circle::large_blue_circle::large_blue_circle::black_circle:\n"
                            ":large_blue_circle::black_circle::black_circle::black_circle::large_blue_circle:\n"
                            ":black_circle::black_circle::black_circle::black_circle::large_blue_circle:\n"
                            ":black_circle::black_circle::large_blue_circle::large_blue_circle::large_blue_circle:\n"
                            ":black_circle::black_circle::black_circle::black_circle::large_blue_circle:\n"
                            ":large_blue_circle::black_circle::black_circle::black_circle::large_blue_circle:\n"
                            ":black_circle::large_blue_circle::large_blue_circle::large_blue_circle::black_circle:", colour=0x3498db)
        await bot.edit_message(msg,  embed=em3)
        await asyncio.sleep(1)
        em2 = discord.Embed(title=":warning: WARNING :warning:", description="THE BOT WILL LEAVE THE SERVER IN:\n"
                            ":black_circle::large_blue_circle::large_blue_circle::large_blue_circle::black_circle:\n"
                            ":large_blue_circle::black_circle::black_circle::black_circle::large_blue_circle:\n"
                            ":black_circle::black_circle::black_circle::large_blue_circle::black_circle:\n"
                            ":black_circle::black_circle::large_blue_circle::black_circle::black_circle:\n"
                            ":black_circle::large_blue_circle::black_circle::black_circle::black_circle:\n"
                            ":large_blue_circle::black_circle::black_circle::black_circle::black_circle:\n"
                            ":large_blue_circle::large_blue_circle::large_blue_circle::large_blue_circle::large_blue_circle:", colour=0x3498db)
        await bot.edit_message(msg,  embed=em2)
        await asyncio.sleep(1)
        em1 = discord.Embed(title=":warning: WARNING :warning:", description="THE BOT WILL LEAVE THE SERVER IN:\n"
                            ":black_circle::black_circle::large_blue_circle::black_circle::black_circle:\n"
                            ":black_circle::large_blue_circle::large_blue_circle::black_circle::black_circle:\n"
                            ":black_circle::black_circle::large_blue_circle::black_circle::black_circle:\n"
                            ":black_circle::black_circle::large_blue_circle::black_circle::black_circle:\n"
                            ":black_circle::black_circle::large_blue_circle::black_circle::black_circle:\n"
                            ":black_circle::black_circle::large_blue_circle::black_circle::black_circle:\n"
                            ":black_circle::large_blue_circle::large_blue_circle::large_blue_circle::black_circle:\n", colour=0x3498db)
        await bot.edit_message(msg,  embed=em1)
        await asyncio.sleep(1)
        em0 = discord.Embed(title=":warning: WARNING :warning:", description="THE BOT WILL LEAVE THE SERVER IN:\n"
                            ":black_circle::large_blue_circle::large_blue_circle::large_blue_circle::black_circle:\n" 
                            ":large_blue_circle::black_circle::black_circle::black_circle::large_blue_circle:\n"
                            ":large_blue_circle::black_circle::black_circle::black_circle::large_blue_circle:\n"
                            ":large_blue_circle::black_circle::black_circle::black_circle::large_blue_circle:\n"
                            ":large_blue_circle::black_circle::black_circle::black_circle::large_blue_circle:\n"
                            ":large_blue_circle::black_circle::black_circle::black_circle::large_blue_circle:\n"
                            ":black_circle::large_blue_circle::large_blue_circle::large_blue_circle::black_circle:", colour=0x3498db)
        await bot.edit_message(msg,  embed=em0)
        await asyncio.sleep(1)
        em = discord.Embed(title="lol Joke", colour=0x3498db)
        em.set_thumbnail(url="https://cdn.discordapp.com/emojis/423864027610087426.png?v=1")
        await bot.edit_message(msg,  embed=em)
    if message.content.startswith('r-invite'):
        em = discord.Embed(title='MY LINKS:', description=':cyclone: PissRocket: https://discord.gg/Cf833k8\n'
                           ':link: Website: https://hegyiaron101.wixsite.com/pissrocket', colour=0x3498db)
        await bot.send_message(message.channel, embed=em)
    if message.content.startswith('r-list'):
        em = discord.Embed(title='MY COMMANDS:', description=':white_small_square: r-bot\n'
                            ':white_small_square: r-game {game}\n'
                            ':white_small_square: r-say {words}\n'
                            ':white_small_square: r-ping\n'
                            ':white_small_square: r-AmiOwner?\n'
                            ':white_small_square: r-bigdigits\n'
                            ':white_small_square: r-digits {0-9}\n'
                            ':white_small_square: r-help\n'
                            ':small_blue_diamond: r-clear\n'
                            ':white_small_square: r-8ball\n'
                            ':white_small_square: r-verify\n'
                            ':white_small_square: r-leavepls\n'
                            ':white_small_square: Poll\n'
                            ':white_small_square: r-invite\n'
                            ':white_small_square: r-latest\n'
                            ':white_small_square: r-lenny\n'
                            '\n'
                            ':white_small_square: Free for everyone\n'
                            ':small_blue_diamond: Staff commands', colour=0x3498db)
        em.set_thumbnail(url="https://cdn.discordapp.com/emojis/385152309090451467.png?v=1")
        em.set_footer(text="The Official Bot of PissRocket, inviting and using the Bot in other servers breaks the Term of Use.")
        await bot.send_message(message.channel, embed=em)  
    if message.content.startswith('r-latest'):
        emb = discord.Embed(title="LATEST UPDATES", description=":high_brightness: The Currently version is __" + version + "__ :high_brightness:\n\n"
                            ":white_small_square: r-game {game}", colour=0x3498db)
        emb.set_thumbnail(url="https://cdn.discordapp.com/emojis/438035428386275340.png?v=1")
        await bot.send_message(message.channel, embed=emb)
    if message.content.startswith('r-bot'):
        em = discord.Embed(description= "```md\n"
                                "<⊐______⊐______⊏THE-ROCKETER-BOT⊐______⊏______⊏>\n"
                                "<                                                >\n"
                                "<▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒>\n"
                                "<                                                >\n"
                                "<▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒>\n"
                                "<˙˙˙˙˙˙˙˙˙The-Official-Bot-of-PissRocket.˙˙˙˙˙˙˙˙>\n"
                                "<˙˙˙˙˙˙˙˙The-currently-version-is-{}-!˙˙˙˙˙˙˙˙>\n"
                                "<                                                >\n"
                                "<▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒>\n"
                                "<                                                >\n"
                                "<▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒>\n"
                                "\n"
                                "         for the commands, type: \"r-help\"```".format(version), colour=0x3498db)
        await bot.send_message(message.channel, embed=em)
    await bot.process_commands(message) #IMPORTANT



    
    
        













token = os.environ.get('DISCORD_TOKEN')
bot.run(token)
