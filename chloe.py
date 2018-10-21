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
@client.command(pass_context=True)
async def setmod(ctx, *, channel_name = None):
    with open("Mod-data.json", "r") as f:
        mod = json.load(f)
    if ctx.message.author.server_permissions.manage_server:
        if channel_name is None:
            await client.say("Please specify a channel for me to set!")
            return
        if not ctx.message.server.id in mod:
            mod[ctx.message.server.id] = {}
            mod[ctx.message.server.id]["mod-channel"] = "defualt"
        mod[ctx.message.server.id]["mod-channel"] = channel_name
        embed = discord.Embed(color=(random.randint(0, 0xffffff)))
        embed.add_field(name=":white_check_mark: Mod-Log set to", value=f"***{channel_name}***", inline=False)
        await client.say(embed=embed)
    else:
        await client.say(f"{ctx.message.author.mention}, You need ``Manage Server`` permissions!")
    with open("Mod-data.json", "w") as f:
        json.dump(mod,f,indent=4)
        
@client.command(pass_context=True)
async def setmute(ctx, *, mute_role = None):
    with open("Mod-data.json", "r") as f:
        mod = json.load(f)
    if ctx.message.author.server_permissions.manage_server:
        if mute_role is None:
            await client.say("Please specify a mute role for me to set!")
            return
        if not ctx.message.server.id in mod:
            mod[ctx.message.server.id] = {}
            mod[ctx.message.server.id]["mute-role"] = "defualt"
        mod[ctx.message.server.id]["mute-role"] = mute_role
        embed = discord.Embed(color=(random.randint(0, 0xffffff)))
        embed.add_field(name=":white_check_mark: Muted Role set to", value=f"***{mute_role}***", inline=False)
        await client.say(embed=embed)
    else:
        await client.say(f"{ctx.message.author.mention}, You need ``Manage Server`` permissions!")
    with open("Mod-data.json", "w") as f:
        json.dump(mod,f,indent=4)
        
        

#UTILITY


#MODERARION COMMANDS:

@client.command(pass_context=True)
async def kick(ctx, user: discord.Member = None, *, reason = None):
    with open("Mod-data.json", "r") as f:
        kick = json.load(f)
    server = ctx.message.server
    author = ctx.message.author
    channel = kick[ctx.message.server.id]["mod-channel"]
    try:
        if ctx.message.author.server_permissions.kick_members:
            if user is None:
                await client.say("Please specify a user for me to kick!")
                return
            await client.send_message(user, f"You were kicked from **{server.name}** for the reason of: **{reason}**")
            await client.kick(user)
            await client.say(f":white_check_mark:***Kicked {user.mention}***")
            embed = discord.Embed(color=(random.randint(0, 0xffffff)))
            embed.set_author(icon_url=user.avatar_url, name="{user.name} was kicked")
            embed.add_field(name="Information", value=":tools:Moderator: **{author.name}*** \n :wave:User: **{user.name}** \n :interrobang:Reason:**{reason}")
            embed.send_message(channel, embed=embed)
        else:
            await client.say(f"{ctx.message.author.mention}, You need ``Kick Members`` permissions!")
    except discord.Forbidden:
        await client.say("Looks like I can't kick this member! Check my permissions.")
    with open("Mod-data.json", "w") as f:
        json.dump(mod,f)

    
 
    
    
    
client.run(os.environ.get('BOT_TOKEN'))
