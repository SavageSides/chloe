import discord
from discord.ext import commands
import aiohttp
import random
import json
import magic_py_ball
import datetime
import requests
import asyncio
import time
import requests
import os

client = commands.Bot(command_prefix="?")

@client.event
async def on_ready():
    print("Chloes Ready")
    
@client.command()
async def on():
    await client.say("I am online on heroku! Wrong, and Savage")

#FUN COMMANDS:
@client.command(pass_context=True, aliases = ["8ball"])
async def eightball(ctx, *, question):
    author = ctx.message.author
    choice = ['Yes', 'No', 'Better not tell you now']
    picked = random.choice(choice)
    embed = discord.Embed(color = 0x00ff00)
    embed.add_field(name= "**"+question+"**", value = picked, inline = False)
    embed.set_footer(icon_url=author.avatar_url, text="Fun Commands!")
    await client.say(embed=embed)
    return    
    
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
 
@client.command(pass_context = True)
async def rate(ctx):
    rating = random.randint(1,100)
    ratings = str(rating)
    await client.say("Your rating is " + ratings + "%")

#CONFIRGURING
@client.command(pass_context=True)
async def setmod(ctx, *, channel_name = None):
    with open("Mod-data.json", "r") as f:
        mod = json.load(f)
    channel = discord.utils.get(ctx.message.server.channels, name = channel_name)
    if ctx.message.author.server_permissions.manage_server:
        if channel is None:
            await client.say("Please say a correct channel.")
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
    Muterole = discord.utils.get(ctx.message.server.roles, name = mute_role)
    if ctx.message.author.server_permissions.manage_server:
        if Muterole is None:
            await client.say("Please say a correct role.")
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
        
@client.command(pass_context=True)
async def setwelcome(ctx, *, text = None):
    with open("Mod-data.json", "r") as f:
        welcome = json.load(f)
    if ctx.message.author.server_permissions.manage_server:
        if text is None:
            await client.say("Please specify a welcome message for me to set!")
            return
        if not ctx.message.server.id in welcome :
            welcome[ctx.message.server.id] = {}
            welcome[ctx.message.server.id]["welcome-message"] = "default"
        welcome[ctx.message.server.id]["welcome-message"] = text
        embed = discord.Embed(color=(random.randint(0, 0xffffff)))
        embed.add_field(name=":white_check_mark: Set welcome to:", value=f"*{text}*", inline=True)
        await client.say(embed=embed)
    else:
        await client.say(f"{ctx.message.author.mention}, You need ``Manage Server`` permissions!")
    with open("Mod-data.json", "w") as f:
        json.dump(welcome,f,indent=4)
        
@client.command(pass_context=True)
async def setgoodbye(ctx, *, text = None):
    with open("Mod-data.json", "r") as f:
        welcome = json.load(f)
    if ctx.message.author.server_permissions.manage_server:
        if text is None:
            await client.say("Please specify a goodbye message for me to set!")
            return
        if not ctx.message.server.id in welcome :
            welcome[ctx.message.server.id] = {}
            welcome[ctx.message.server.id]["goodbye-message"] = "default"
        welcome[ctx.message.server.id]["goodbye-message"] = text
        embed = discord.Embed(color=(random.randint(0, 0xffffff)))
        embed.add_field(name=":white_check_mark: Set goodbye to:", value=f"*{text}*", inline=True)
        await client.say(embed=embed)
    else:
        await client.say(f"{ctx.message.author.mention}, You need ``Manage Server`` permissions!")
    with open("Mod-data.json", "w") as f:
        json.dump(welcome,f,indent=4)
        
@client.command(pass_context=True)
async def setchannel(ctx, *, text = None):
    with open("Mod-data.json", "r") as f:
        welcome = json.load(f)
    channel = discord.utils.get(ctx.message.server.channels, name = text)
    if ctx.message.author.server_permissions.manage_server:
        if channel is None:
            await client.say("Please say a correct channel.")
            return
        if not ctx.message.server.id in welcome :
            welcome[ctx.message.server.id] = {}
            welcome[ctx.message.server.id]["welcome-goodbye-channel"] = "defualt"
        welcome[ctx.message.server.id]["welcome-goodbye-channel"] = text
        embed = discord.Embed(color=(random.randint(0, 0xffffff)))
        embed.add_field(name=":white_check_mark: Set goodbye to:", value=f"*{text}*", inline=True)
        await client.say(embed=embed)
    else:
        await client.say(f"{ctx.message.author.mention}, You need ``Manage Server`` permissions!")
    with open("Mod-data.json", "w") as f:
        json.dump(welcome,f,indent=4)
        

        
        

#UTILITY
@client.command(pass_context = True)
async def avatar(ctx, user: discord.Member = None):
    author = ctx.message.author
    await client.send_typing(ctx.message.channel)
    if user is None:
        embed = discord.Embed(color=(random.randint(0, 0xffffff)))
        embed.add_field(name=f"**{ctx.message.author.name}'s** Avatar", value="Avatar's!", inline=False)
        embed.set_image(url=author.avatar_url)
        await client.say(embed=embed)

    else:
        embed = discord.Embed(color=(random.randint(0, 0xffffff)))
        embed.add_field(name=f"**{user.name}'s** Avatar", value="Avatar's!", inline=True)
        embed.set_image(url=user.avatar_url)
        await client.say(embed=embed)


#MODERARION COMMANDS:

@client.command(pass_context=True)
async def crole(ctx, *, role = None):
    with open("Mod-data.json", "r") as f:
        mod = json.load(f)
    channel = mod[ctx.message.server.id]["mod-channel"]
    channels = discord.utils.get(ctx.message.server.channels, name = channel)
    server = ctx.message.server
    author = ctx.message.author
    if ctx.message.author.bot:
        await client.say("Bots can't use commands.")
        return
    try:
        if ctx.message.author.server_permissions.manage_roles:
            if role is None:
                await client.say("Please specify a correct role.")
                return
            await client.create_role(server=server, name=role)
            await client.say(f":white_check_mark:***Created {role}***")
            embed = discord.Embed(color=(random.randint(0, 0xffffff)), timestamp=datetime.datetime.utcnow())
            embed.set_author(icon_url=author.avatar_url, name=f"Created Role")
            embed.add_field(name="Information", value=f":tools:Moderator: **{author.name}** \n :thinking:Role: **{role}**")
            await client.send_message(channels, embed=embed)
        else:
            await client.say(f"{ctx.message.author.mention}, You need ``Manage Roles`` permissions!")
    except discord.Forbidden:
            await client.say("I need manage roles permissions.")
    with open("Mod-data.json", "w") as f:
        json.dump(mod,f)
        
@client.command(pass_context=True)
async def drole(ctx, *, name = None):
    with open("Mod-data.json", "r") as f:
        mod = json.load(f)
    channel = mod[ctx.message.server.id]["mod-channel"]
    channels = discord.utils.get(ctx.message.server.channels, name = channel)
    server = ctx.message.server
    author = ctx.message.author
    if ctx.message.author.bot:
        await client.say("Bots can't use commands.")
        return
    try:
        if ctx.message.author.server_permissions.manage_roles:
            role = discord.utils.get(ctx.message.server.roles, name=name)
            if role is None:
                await client.say("Please specify a correct role.")
                return
            await client.delete_role(server=server, role=role)
            await client.say(f":white_check_mark:***Deleted {name}***")
            embed = discord.Embed(color=(random.randint(0, 0xffffff)), timestamp=datetime.datetime.utcnow())
            embed.set_author(icon_url=author.avatar_url, name=f"Deleted Role")
            embed.add_field(name="Information", value=f":tools:Moderator: **{author.name}** \n :thinking:Role: **{name}**")
            await client.send_message(channels, embed=embed)
        else:
            await client.say(f"{ctx.message.author.mention}, You need ``Manage Roles`` permissions!")
    except discord.Forbidden:
            await client.say("I need manage roles permissions.")
    with open("Mod-data.json", "w") as f:
        json.dump(mod,f)
        
@client.command(pass_context=True)
async def addrole(ctx, user: discord.Member = None, *, name = None):
    with open("Mod-data.json", "r") as f:
        mod = json.load(f)
    channel = mod[ctx.message.server.id]["mod-channel"]
    channels = discord.utils.get(ctx.message.server.channels, name = channel)
    author = ctx.message.author
    if ctx.message.author.bot:
        await client.say("Bots can't use commands.")
        return
    try:
        if ctx.message.author.server_permissions.manage_roles:
            role = discord.utils.get(ctx.message.server.roles, name=name)
            if user is None:
                await client.say("Please specify a user!")
                return
            if role is None:
                await client.say("Please specify a correct role.")
                return
            await client.add_roles(user, role)
            await client.say(f":white_check_mark:***Added {name} to {user.name}***")
            embed = discord.Embed(color=(random.randint(0, 0xffffff)), timestamp=datetime.datetime.utcnow())
            embed.set_author(icon_url=author.avatar_url, name=f"Added Role")
            embed.add_field(name="Information", value=f":tools:Moderator: **{author.name}** \n :thinking:Role: **{name}** \n :wave:User: **{user.name}**")
            await client.send_message(channels, embed=embed)
        else:
            await client.say(f"{ctx.message.author.mention}, You need ``Manage Roles`` permissions!")
    except discord.Forbidden:
            await client.say("I need manage roles permissions.")
    with open("Mod-data.json", "w") as f:
        json.dump(mod,f)
        
@client.command(pass_context=True)
async def removerole(ctx, user: discord.Member = None, *, name = None):
    with open("Mod-data.json", "r") as f:
        mod = json.load(f)
    channel = mod[ctx.message.server.id]["mod-channel"]
    channels = discord.utils.get(ctx.message.server.channels, name = channel)
    author = ctx.message.author
    if ctx.message.author.bot:
        await client.say("Bots can't use commands.")
        return
    try:
        if ctx.message.author.server_permissions.manage_roles:
            role = discord.utils.get(ctx.message.server.roles, name=name)
            if user is None:
                await client.say("Please specify a user!")
                return
            if role is None:
                await client.say("Please specify a correct role.")
                return
            await client.remove_roles(user, role)
            await client.say(f":white_check_mark:***Removed {name} from {user.name}***")
            embed.set_author(icon_url=author.avatar_url, name=f"Removed Role")
            embed.add_field(name="Information", value=f":tools:Moderator: **{author.name}** \n :thinking:Role: **{name}** \n :wave:User: **{user.name}**")
            await client.send_message(channels, embed=embed)
        else:
            await client.say(f"{ctx.message.author.mention}, You need ``Manage Roles`` permissions!")
    except discord.Forbidden:
            await client.say("I need manage roles permissions.")
    with open("Mod-data.json", "w") as f:
        json.dump(mod,f)
        
@client.command(pass_context=True, no_pm=True)
async def rolecolor(ctx, colour : discord.Colour = None, *, name = None):
    with open("Mod-data.json", "r") as f:
        mod = json.load(f)
    channel = mod[ctx.message.server.id]["mod-channel"]
    channels = discord.utils.get(ctx.message.server.channels, name = channel)
    author = ctx.message.author
    if ctx.message.author.bot:
        await client.say("Bots can't use commands.")
        return
    try:
        if ctx.message.author.server_permissions.manage_roles:
            roles = discord.utils.get(ctx.message.server.roles, name=name)
            if roles is None:
                await client.say("Please specify a correct role.")
                return
            if colour is None:
                await client.say("Please specify a color for me to edit the role")
                return
            await client.edit_role(ctx.message.server, roles, colour=colour)
            await client.say(f":white_check_mark:***Edited {name}'s color***")
            embed = discord.Embed(color=(random.randint(0, 0xffffff)), timestamp=datetime.datetime.utcnow())
            embed.set_author(icon_url=author.avatar_url, name=f"Edited Role")
            embed.add_field(name="Information", value=f":tools:Moderator: **{author.name}** \n :thinking:Role: **{name}** \n :tada:Color: **#{colour}**")
            await client.send_message(channels, embed=embed)
        else:
            await client.say(f"{ctx.message.author.mention}, You need ``Manage Roles`` permissions!")
    except discord.Forbidden:
        await client.say("I need manage roles permissions.")
    with open("Mod-data.json", "w") as f:
        json.dump(mod,f)

@client.command(pass_context=True)
async def kick(ctx, user: discord.Member = None, *, reason = None):
    with open("Mod-data.json", "r") as f:
        kick = json.load(f)
    server = ctx.message.server
    author = ctx.message.author
    channel = kick[ctx.message.server.id]["mod-channel"]
    channels = discord.utils.get(ctx.message.server.channels, name = channel)
    try:
        if ctx.message.author.server_permissions.kick_members:
            if author == user:
                await client.say("You can't kick your self!")
                return
            if user is None:
                await client.say("Please specify a user for me to kick!")
                return
            await client.send_message(user, f"You were kicked from **{server.name}** for the reason of: **{reason}**")
            await client.kick(user)
            await client.say(f":white_check_mark:***Kicked {user.mention}***")
            embed = discord.Embed(color=(random.randint(0, 0xffffff)), timestamp=datetime.datetime.utcnow())
            embed.set_author(icon_url=user.avatar_url, name=f"{user.name} was kicked")
            embed.add_field(name="Information", value=f":tools:Moderator: **{author.name}** \n :wave:User: **{user.name}** \n :interrobang:Reason:**{reason}**")
            await client.send_message(channels, embed=embed)
        else:
            await client.say(f"{ctx.message.author.mention}, You need ``Kick Members`` permissions!")
    except discord.Forbidden:
        await client.say("Looks like I can't kick this member! Check my permissions.")
    with open("Mod-data.json", "w") as f:
        json.dump(kick,f)
        
@client.command(pass_context=True)
async def ban(ctx, user: discord.Member = None, *, reason = None):
    with open("Mod-data.json", "r") as f:
        kick = json.load(f)
    server = ctx.message.server
    author = ctx.message.author
    channel = kick[ctx.message.server.id]["mod-channel"]
    channels = discord.utils.get(ctx.message.server.channels, name = channel)
    try:
        if ctx.message.author.server_permissions.ban_members:
            if author == user:
                await client.say("You can't ban your self!")
                return
            if user is None:
                await client.say("Please specify a user for me to ban!")
                return
            await client.send_message(user, f"You were banned from **{server.name}** for the reason of: **{reason}**")
            await client.ban(user)
            await client.say(f":white_check_mark:***Banned {user.mention}***")
            embed = discord.Embed(color=(random.randint(0, 0xffffff)), timestamp=datetime.datetime.utcnow())
            embed.set_author(icon_url=user.avatar_url, name=f"{user.name} was banned")
            embed.add_field(name="Information", value=f":tools:Moderator: **{author.name}** \n :wave:User: **{user.name}** \n :interrobang:Reason:**{reason}**")
            await client.send_message(channels, embed=embed)
        else:
            await client.say(f"{ctx.message.author.mention}, You need ``Ban Members`` permissions!")
    except discord.Forbidden:
        await client.say("Looks like I can't ban this member! Check my permissions.")
    with open("Mod-data.json", "w") as f:
        json.dump(kick,f)
        
@client.command(pass_context=True)
async def mute(ctx, user: discord.Member = None, *, reason = None):
    with open("Mod-data.json", "r") as f:
        mute = json.load(f)
    author = ctx.message.author
    role = mute[ctx.message.server.id]["mute-role"]
    MutedRole = discord.utils.get(ctx.message.server.roles, name = role)
    modchannel = mute[ctx.message.server.id]["mod-channel"]
    channels = discord.utils.get(ctx.message.server.channels, name = modchannel)
    try:
        if ctx.message.author.server_permissions.mute_members:
            if author == user:
                await client.say("You can't unmute your self!")
                return
            if MutedRole is None:
                await client.say("Please set a muted role! ``?setmute <role>``")
                return
            if user is None:
                await client.say("Please specify a user for me to mute!")
                return
            await client.add_roles(user, MutedRole)
            await client.send_message(user, f"You were muted in **{ctx.message.server.name}** for the reason of: **{reason}**")
            await client.say(f":white_check_mark:***Muted {user.mention}***")
            embed = discord.Embed(color=(random.randint(0, 0xffffff)), timestamp=datetime.datetime.utcnow())
            embed.set_author(icon_url=user.avatar_url, name=f"{user.name} was kicked")
            embed.add_field(name="Information", value=f":tools:Moderator: **{author.name}** \n :wave:User: **{user.name}** \n :interrobang:Reason:**{reason}** \n :thinking:Role:**{MutedRole}**")
            await client.send_message(channels, embed=embed)
        else:
            await client.say(f"{ctx.message.author.mention}, You need ``Mute Members`` permissions!")
    except discord.Forbidden:
        await client.say("I can't add the muted role to the user I do not have permissions!")
    with open("Mod-data.json", "r") as f:
        json.dump(mute,f)
        
@client.command(pass_context=True)
async def unmute(ctx, user: discord.Member = None):
    with open("Mod-data.json", "r") as f:
        mute = json.load(f)
    author = ctx.message.author
    role = mute[ctx.message.server.id]["mute-role"]
    MutedRole = discord.utils.get(ctx.message.server.roles, name = role)
    modchannel = mute[ctx.message.server.id]["mod-channel"]
    channels = discord.utils.get(ctx.message.server.channels, name = modchannel)
    try:
        if ctx.message.author.server_permissions.mute_members:
            if author == user:
                await client.say("You can't unmute your self!")
                return
            if MutedRole is None:
                await client.say("Please set a muted role! ``?setmute <role>``")
                return
            if user is None:
                await client.say("Please specify a user for me to mute!")
                return
            await client.remove_roles(user, MutedRole)
            await client.send_message(user, f"You were unmuted in **{ctx.message.server.name}**")
            await client.say(f":white_check_mark:***Unmuted {user.mention}***")
            embed = discord.Embed(color=(random.randint(0, 0xffffff)), timestamp=datetime.datetime.utcnow())
            embed.set_author(icon_url=user.avatar_url, name=f"{user.name} was unmuted")
            embed.add_field(name="Information", value=f":tools:Moderator: **{author.name}** \n :wave:User: **{user.name}** \n :thinking:Role:**{MutedRole}**")
            await client.send_message(channels, embed=embed)
        else:
            await client.say(f"{ctx.message.author.mention}, You need ``Mute Members`` permissions!")
    except discord.Forbidden:
        await client.say("I can't remove the muted role to the user I do not have permissions!")
    with open("Mod-data.json", "r") as f:
        json.dump(mute,f)
        
@client.command(pass_context=True)
async def purge(ctx, *, amount: int = None):
    with open("Mod-data.json", "r") as f:
        mod = json.load(f)
    modchannel = mod[ctx.message.server.id]["mod-channel"]
    channels = discord.utils.get(ctx.message.server.channels, name = modchannel)
    try:
        if ctx.message.author.server_permissions.manage_messages:
            if amount is None:
                await client.say("Please specify a amount you want me to clear!")
                return
            channel = ctx.message.channel
            author = ctx.message.author
            messages = []
            async for message in client.logs_from(channel, limit=int(amount)):
                messages.append(message)
            await client.delete_messages(messages)
            msg = await client.say(f":white_check_mark:***Cleared {amount}***")
            embed = discord.Embed(color=(random.randint(0, 0xffffff)), timestamp=datetime.datetime.utcnow())
            embed.set_author(icon_url=author.avatar_url, name=f"Chat Was Cleared")
            embed.add_field(name="Information", value=f":tools:Moderator: **{author.name}**\n :thinking:Amount:**{amount}**\n:inbox_tray:Channel:**{channel.mention}**")
            await client.send_message(channels, embed=embed)
            await asynco.sleep(4)
            await client.delete_message(msg)
        else:
            await client.say(f"{ctx.message.author.mention}, You need ``Manage Messages`` permissions!")
    except discord.Forbidden:
        await client.say("I can't clear the chat, I do not have permissions!")
    with open("Mod-data.json", "r") as f:
        json.dump(mod,f)
        
#Logging Actions Of Users


        
    
        
  
client.run(os.environ.get('BOT_TOKEN'))
