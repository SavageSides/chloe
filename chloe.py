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


#MODERARION COMMANDS:
  
    
client.run(os.environ.get('BOT_TOKEN'))
