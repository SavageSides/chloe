import discord
from discord.ext import commands
import aiohttp
import random
import json
import asyncio
import time
import os

client = commands.Bot(command_prefix="?")

@client.event
async def on_ready():
    print("Chloes Ready")
    
@client.command()
async def on():
    await client.say("I am online on heroku! Wrong, and Savage")

#FUN COMMANDS:
@client.command(pass_context = True)
@commands.cooldown(5, 10, commands.BucketType.user)
async def meme(ctx):
    async with aiohttp.ClientSession() as cs:
        async with cs.get("https://api.reddit.com/r/me_irl/random") as r:
            author = ctx.message.author
            data = await r.json()
            embed = discord.Embed(title="Your Daily Meme",
                                  color=0x00ff00)
            embed.set_image(url = data[0]["data"]["children"][0]["data"]["url"])
            embed.set_footer(icon_url=author.avatar_url, text="| Fun Commands!")

            await client.say(embed=embed)            
@meme.error
async def cooldown_error(error, ctx):
    if isinstance(error, commands.CommandOnCooldown):
        remainder = divmod(error.retry_after, 10)
        embed = discord.Embed(color=(random.randint(0, 0xffffff)))
        embed.add_field(name="Slowdown :stuck_out_tongue_winking_eye: ", value=f"Cooldown: **{remainder}** \n Each Command: **5**", inline=False)
        await client.say(embed=embed)
        
#CONFIRGURING


#UTILITY
@client.command(pass_context=True)
async def nickname(ctx, member: discord.User=None, *, newnick=None):
    author = ctx.message.author
    try:
        if ctx.message.author.server_permissions.manage_nicknames:
            if member is None:
                embed = discord.Embed(color=0xff0200)
                embed.add_field(name=':x: Error:', value='```Please specify a user!```', inline=False)
                embed.set_footer(icon_url=author.avatar_url, text="| Utility commands!")
                await client.say(embed=embed)
            
        else:
            embed = discord.Embed(color=0xff0200)
            embed.add_field(name=':x: Error', value='You are missing the following permission: ``Manage Nicknames``', inline=False)
            embed.set_footer(icon_url=author.avatar_url, text='You cant use this command!')
            await client.say(embed=embed)
            
        await client.change_nickname(member, newnick)
        embed = discord.Embed(color=0x00ff00)
        embed.add_field(name='Changed:', value=f"You have changed {member.name}'s name to `{newnick}`", inline=True)
        embed.set_footer(icon_url=author.avatar_url, text="| Utility commands!")
        await client.say(embed=embed) 
            
    except discord.Forbidden:
        embed = discord.Embed(color=0xff0200)
        author = ctx.message.author
        embed.set_author(name="Something went wrong ;-;")
        embed.add_field(name=":x: Error", value="I'm missing the following permission: ```Manage Nicknames```", inline=False)
        embed.set_footer(icon_url=author.avatar_url, text=f"Make sure my role is higher than {author.name}, that can be another error ;-;")
        await client.say(embed=embed)

    except discord.HTTPException:
        embed = discord.Embed(color=0xff0200)
        embed.add_field(name=":x: Error", value="Sorry, I can't nickname other bots at the moment ;-;")
        await client.say(embed=embed)    

#MODERARION COMMANDS:
  
    
client.run(os.environ.get('BOT_TOKEN'))
