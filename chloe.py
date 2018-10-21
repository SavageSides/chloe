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
client.remove_command('help')

@client.event
async def on_server_join(server):
    await client.change_presence(game=discord.Game(name=f"{len(client.servers)} server(s)", type=3))

@client.event
async def on_server_remove(server):
    await client.change_presence(game=discord.Game(name=f"{len(client.servers)} server(s)", type=3))

@client.event
async def on_ready():
    print("Chloes Ready")
    await client.change_presence(game=discord.Game(name=f"{len(client.servers)} server(s)", type=3))
    
@client.command()
async def on():
    await client.say("I am online on heroku! Wrong, and Savage")
    
@client.event
async def on_member_join(member):
    with open("Mod-data.json", "r") as f:
        join = json.load(f)
    server = member.server
    joinrole = mod[ctx.message.server.id]["autorole"] = mute_role
    joined = discord.utils.get(ctx.message.server.roles, name = joinrole)
    welcomes = join[member.server.id]["welcome-message"]
    channels = join[member.server.id]["welcome-goodbye-channel"]
    channel = discord.utils.get(server.channels, name=channels)
    await client.send_message(channel, f"{member.mention}, {welcomes}")
    await client.add_roles(member, joined)
    with open("Mod-data.json", "w") as f:
        json.dump(join,f)

@client.event
async def on_member_remove(member):
    with open("Mod-data.json", "r") as f:
        bye = json.load(f)
    server = member.server
    goodbyess = bye[member.server.id]["goodbye-message"]
    channels = bye[member.server.id]["welcome-goodbye-channel"]
    channel = discord.utils.get(server.channels, name=channels)
    await client.send_message(channel, f"{member.mention}, {goodbyess}")
    with open("Mod-data.json", "w") as f:
        json.dump(bye,f)
   

@client.command(pass_context=True)
async def suggestion(ctx, *, suggestion = None):
    server = client.get_server("498179637990522880")
    channel = client.get_channel("503667719015497741")
    embed = discord.Embed(color=(random.randint(0, 0xffffff)))
    embed.add_field(name=":white_check_mark: Sucess", value="**[Suggestion was sent](https://discord.gg/fzAVzp)**", inline=False)
    await client.say(embed=embed)
    embed = discord.Embed(color=(random.randint(0, 0xffffff)))
    embed.add_field(name="Suggestion Occured", value="Following Data is collected below!", inline=False)
    embed.add_field(name="Author:", value=f"{ctx.message.author.name}", inline=False)
    embed.add_field(name="Suggestion:", value=f"***{suggestion}***", inline=False)
    await client.send_message(channel, embed=embed)
    
@client.command(pass_context=True)
async def bug(ctx, *, suggestion = None):
    server = client.get_server("498179637990522880")
    channel = client.get_channel("503667732856832000")
    embed = discord.Embed(color=(random.randint(0, 0xffffff)))
    embed.add_field(name=":white_check_mark: Sucess", value="**[Bug will be resolved as quick as possible!](https://discord.gg/fzAVzp)**", inline=False)
    await client.say(embed=embed)
    embed = discord.Embed(color=(random.randint(0, 0xffffff)))
    embed.add_field(name="Bug Occured", value="Following Data is collected below!", inline=False)
    embed.add_field(name="Author:", value=f"{ctx.message.author.name}", inline=False)
    embed.add_field(name="Bug:", value=f"***{suggestion}***", inline=False)
    await client.send_message(channel, embed=embed)
    
@client.command(pass_context=True)
async def help(ctx):
    embed = discord.Embed(color=(random.randint(0, 0xfffff)))
    embed.add_field(name="Help", value="If you need help controling me join the [support server](https://discord.gg/V3TG65a)")
    embed.add_field(name="Fun Commands", value="``?rate`` ``?meme`` ``?8ball`` ``?on``", inline=False)
    embed.add_field(name="Config Commands", value="``?setmod`` ``?setmute`` ``?setwelcome`` ``?setgoodbye`` ``?setchannel``", inline=False)
    embed.add_field(name="Utility Commands", value="``?serverinfo`` ``?userinfo`` ``?avatar`` ``?giveaway`` ``?suggestion`` ``?bug``", inline=False)
    embed.add_field(name="Roleplay Commands", value="``?crole`` ``?drole`` ``?addrole`` ``?removerole`` ``?rolecolor``", inline=False)
    embed.add_field(name="Moderation Commands", value="``?kick`` ``?ban`` ``?mute`` ``?unmute`` ``?purge``", inline=False)
    embed.add_field(name="Currency Commands", value="``?addmoney`` ``?removemoney`` ``?work`` ``?daily`` ``?slots`` ``?givemoney`` ``?crate`` ``?crates`` ``?bal``", inline=False)
    embed.add_field(name="Image Commands", value="``?dog`` ``?cat`` ``?shibe`` ``?duck`` ``?bird``", inline=False)
    embed.add_field(name="Neko Commands", value="``?slap`` ``?hug`` ``?cuddle`` ``?kiss``", inline=False)
    embed.add_field(name="Help", value="If you want to know more about me to go my [wesbite](https://ytsparkyt.github.io/Chloe/Home.html)", inline=False)
    await client.say(embed=embed)

@client.command(pass_context = True)
async def invite(ctx):
    embed = discord.Embed(color = 0x00ff00)
    embed.add_field(name = "Inivte me to the server by clicking on 'link' below", value = "[link](https://discordapp.com/oauth2/authorize?client_id=503386558976622593&permissions=2146958839&scope=bot)", inline = False)
    await client.say(embed = embed)
    
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
async def autorole(ctx, *, mute_role = None):
    with open("Mod-data.json", "r") as f:
        mod = json.load(f)
    joinrole = discord.utils.get(ctx.message.server.roles, name = mute_role)
    if ctx.message.author.server_permissions.manage_server:
        if joinrole is None:
            await client.say("Please say a correct role.")
            return
        if not ctx.message.server.id in mod:
            mod[ctx.message.server.id] = {}
            mod[ctx.message.server.id]["autorole"] = "defualt"
        mod[ctx.message.server.id]["autorole"] = mute_role
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
            embed = discord.Embed(color=(random.randint(0, 0xffffff)), timestamp=datetime.datetime.utcnow())
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
            await asyncio.sleep(4)
            await client.delete_message(msg)
        else:
            await client.say(f"{ctx.message.author.mention}, You need ``Manage Messages`` permissions!")
    except discord.Forbidden:
        await client.say("I can't clear the chat, I do not have permissions!")
    with open("Mod-data.json", "r") as f:
        json.dump(mod,f)
        
#Economy
@client.command(pass_context=True)
async def addmoney(ctx, user: discord.Member = None, amount: int = None):
    with open("economy.json", "r") as f:
       	coins = json.load(f)
    if ctx.message.author.bot:
        await client.say("Bot's will not use my commands. Those other bots will store my data full of junk!")
        return
    if ctx.message.author.server_permissions.manage_server:
        if user == ctx.message.author:
            await client.say("I can't give you money. You are cheating my system!")
            return
        if user is None:
            embed = discord.Embed(color=(random.randint(0, 0xffffff)))
            embed.add_field(name=":x: Error", value="You need a user name!\n **Example:** \n ?addmoney @User")
            await client.say(embed=embed)
            return
        if amount is None:
            embed = discord.Embed(color=(random.randint(0, 0xffffff)))
            embed.add_field(name=":x: Error", value="You need a amount!\n **Example:** \n ?addmoney @User 5")
            await client.say(embed=embed)
            return
        if not ctx.message.server.id in coins:
            coins[ctx.message.server.id] = {}
        if not user.id in coins[ctx.message.server.id]:
            coins[ctx.message.server.id][user.id] = 0
        coins[ctx.message.server.id][user.id] += amount
        embed = discord.Embed(color=(random.randint(0, 0xffffff)))
        embed.add_field(name="Money Added!", value=f"Added **${amount}** to {user.mention}!", inline=False)
        embed.set_thumbnail(url=user.avatar_url)
        await client.say(embed=embed)
    else:
        embed = discord.Embed(color=(random.randint(0, 0xffffff)))
        embed.add_field(name=":x: Error", value="You're missing permissions!", inline=False)
        embed.add_field(name="Permissions:", value="``Manage Server``")
        embed.set_footer(text="Missing Permissions!", icon_url=author.avatar_url)
        await client.say(embed=embed)
    with open("economy.json", "w") as f:
        json.dump(coins, f, indent=4)

@client.command(pass_context=True)
async def removemoney(ctx, user: discord.Member = None):
    with open("economy.json", "r") as f:
       	coins = json.load(f)
    author = ctx.message.author
    channel = ctx.message.channel
    amount = coins[ctx.message.server.id][user.id]
    if ctx.message.author.bot:
        await client.say("Bot's will not use my commands. Those other bots will store my data full of junk!")
        return
    if ctx.message.author.server_permissions.manage_server:
        if user == author:
            await client.say("I can't remove your money. You are making me feel like I haven't done good for you!")
            return
        if user is None:
            embed = discord.Embed(color=(random.randint(0, 0xffffff)))
            embed.add_field(name=":x: Error", value="You need a user name!\n **Example:** \n ?remove @User")
            await client.say(embed=embed)
            return
        if not ctx.message.server.id in coins:
            coins[ctx.message.server.id] = {}
        if not user.id in coins[ctx.message.server.id]:
            coins[ctx.message.server.id][user.id] = 0
        coins[ctx.message.server.id][user.id] -= amount
        embed = discord.Embed(color=(random.randint(0, 0xffffff)))
        embed.add_field(name="Mone Removed!", value=f"I have removed **${amount}** from {user.mention}!", inline=False)
        embed.set_thumbnail(url=user.avatar_url)
        await client.say(embed=embed)
    else:
        embed = discord.Embed(color=(random.randint(0, 0xffffff)))
        embed.add_field(name=":x: Error", value="You're missing permissions!", inline=False)
        embed.add_field(name="Permissions:", value="``Manage Server``")
        embed.set_footer(text="Missing Permissions!", icon_url=author.avatar_url)
        await client.say(embed=embed)
    with open("economy.json", "w") as f:
        json.dump(coins, f, indent=4)

@client.command(pass_context=True)
@commands.cooldown(1, 120, commands.BucketType.user)
async def work(ctx):
    with open("economy.json", "r") as f:
       	coins = json.load(f)
    author = ctx.message.author
    coinsc = random.randint(100, 700)
    if ctx.message.author.bot:
        await client.say("Bot's will not use my commands. Those other bots will store my data full of junk!")
        return
    if not ctx.message.server.id in coins:
       	coins[ctx.message.server.id] = {}
    if not author.id in coins[ctx.message.server.id]:
        coins[ctx.message.server.id][author.id] = 0
    coins[ctx.message.server.id][author.id] += coinsc
    embed = discord.Embed(color=(random.randint(0, 0xffffff)))
    embed.add_field(name=":moneybag: | Work Reward", value=f"{author.mention}, I have put $**{coinsc}** in your account!", inline=False)
    await client.say(embed=embed)
    with open("economy.json", "w") as f:
        json.dump(coins, f, indent=4)
@work.error
async def cooldown_error(error, ctx):
    if isinstance(error, commands.CommandOnCooldown):
        remainder = divmod(error.retry_after, 120)
        embed = discord.Embed(color=(random.randint(0, 0xffffff)))
        embed.add_field(name="Slowdown :stuck_out_tongue_winking_eye: ", value=f"Cooldown: **{remainder}** \n Each Command: **1**", inline=False)
        await client.say(embed=embed)

@client.command(pass_context=True)
@commands.cooldown(1, 864000, commands.BucketType.user)
async def daily(ctx):
    with open("economy.json", "r") as f:
       	coins = json.load(f)
    author = ctx.message.author
    coinsc = random.randint(100, 700)
    if ctx.message.author.bot:
        await client.say("Bot's will not use my commands. Those other bots will store my data full of junk!")
        return
    if not ctx.message.server.id in coins:
       	coins[ctx.message.server.id] = {}
    if not author.id in coins[ctx.message.server.id]:
        coins[ctx.message.server.id][author.id] = 0
    coins[ctx.message.server.id][author.id] += coinsc
    embed = discord.Embed(color=(random.randint(0, 0xffffff)))
    embed.add_field(name=":moneybag: | Daily Reward", value=f"{author.mention}, I have put $**{coinsc}** in your account!", inline=False)
    await client.say(embed=embed)
    with open("economy.json", "w") as f:
        json.dump(coins, f, indent=4)
@daily.error
async def cooldown_error(error, ctx):
    if isinstance(error, commands.CommandOnCooldown):
        remainder = divmod(error.retry_after, 864000)
        embed = discord.Embed(color=(random.randint(0, 0xffffff)))
        embed.add_field(name="Slowdown :stuck_out_tongue_winking_eye: ", value=f"Cooldown: **{remainder}** \n Each Command: **1**", inline=False)
        await client.say(embed=embed)

@client.command(pass_context=True)
async def slots(ctx, *, amount: int = None):
    with open("economy.json", "r") as f:
        coins = json.load(f)
    choices = random.randint(0, 1)
    author = ctx.message.author
    amountt = coins[ctx.message.server.id][author.id]
    if author.bot:
        await client.say("Bot's will not use my commands. Those other bots will store my data full of junk!")
        return
    if amount is None:
        embed = discord.Embed(color=(random.randint(0, 0xffffff)))
        embed.add_field(name=":x: Error", value="You need a slotting number! **Example:** \n ?slots 5")
        await client.say(embed=embed)
        return
    if coins[ctx.message.server.id][author.id] <= 1:
        embed = discord.Embed(color=(random.randint(0, 0xffffff)))
        embed.add_field(name=":x: Error", value="You need at least 2 coins in your account for this command!")
        await client.say(embed=embed)
        return
    if amount > coins[ctx.message.server.id][author.id]:
        embed = discord.Embed(color=(random.randint(0, 0xffffff)))
        embed.add_field(name=":x: Error", value="You don't have any coins avliable in your balance!")
        await client.say(embed=embed)
        return
    if amount <= 0:
        embed = discord.Embed(color=(random.randint(0, 0xffffff)))
        embed.add_field(name=":x: Error", value="You can't use any number less than 0")
        await client.say(embed=embed)
        return
    if choices == 0:
        coins[ctx.message.server.id][author.id] += amount * 2
        won = amount * 2
        slots = [
            ":tada: :tools: :timer:",
            ":timer: :tada: :timer:",
            ":tools: :timer: :tada:"
        ]
        embed = discord.Embed(color=(random.randint(0, 0xffffff)))
        embed.add_field(name=":slot_machine: Slots! :slot_machine:", value=(random.choice(slots)), inline=False)
        msg =  await client.say(embed=embed)
        await asyncio.sleep(.50)
        embed = discord.Embed(color=(random.randint(0, 0xffffff)))
        embed.add_field(name=":slot_machine: Slots! :slot_machine:", value=(random.choice(slots)), inline=False)
        await client.edit_message(msg, embed=embed)
        await asyncio.sleep(.50)
        embed = discord.Embed(color=(random.randint(0, 0xffffff)))
        embed.add_field(name=":slot_machine: Slots! :slot_machine:", value=(random.choice(slots)), inline=False)
        await client.edit_message(msg, embed=embed)
        await asyncio.sleep(.50)
        embed = discord.Embed(color=(random.randint(0, 0xffffff)))
        embed.add_field(name=":slot_machine: Slots! :slot_machine:", value=(random.choice(slots)), inline=False)
        embed.add_field(name="Win Or Lose?", value=f"**You Won: {won}**")
        await client.edit_message(msg, embed=embed)
    else:
        coins[ctx.message.server.id][author.id] -= amount
        slots1 = [
            ":tada: :tools: :timer:",
            ":timer: :tada: :timer:",
            ":tools: :timer: :tada:"
        ]
        embed = discord.Embed(color=(random.randint(0, 0xffffff)))
        embed.add_field(name=":slot_machine: Slots! :slot_machine:", value=(random.choice(slots1)), inline=False)
        msg =  await client.say(embed=embed)
        await asyncio.sleep(.50)
        embed = discord.Embed(color=(random.randint(0, 0xffffff)))
        embed.add_field(name=":slot_machine: Slots! :slot_machine:", value=(random.choice(slots1)), inline=False)
        await client.edit_message(msg, embed=embed)
        await asyncio.sleep(.50)
        embed = discord.Embed(color=(random.randint(0, 0xffffff)))
        embed.add_field(name=":slot_machine: Slots! :slot_machine:", value=(random.choice(slots1)), inline=False)
        await client.edit_message(msg, embed=embed)
        await asyncio.sleep(.50)
        embed = discord.Embed(color=(random.randint(0, 0xffffff)))
        embed.add_field(name=":slot_machine: Slots! :slot_machine:", value=(random.choice(slots1)), inline=False)
        embed.add_field(name="Win Or Lose?", value=f"**You Lost: {amount}**")
        await client.edit_message(msg, embed=embed)
    with open("economy.json", "w") as f:
        json.dump(coins, f, indent=4)

@client.command(pass_context=True)
async def givemoney(ctx, user: discord.Member = None, amount: int = None):
    with open("economy.json", "r") as f:
       	coins = json.load(f)
    author = ctx.message.author
    if ctx.message.author.bot:
        await client.say("Bot's will not use my commands. Those other bots will store my data full of junk!")
        return
    if user == ctx.message.author:
        await client.say("I can't give you money. You are cheating my system!")
        return
    if user is None:
        embed = discord.Embed(color=(random.randint(0, 0xffffff)))
        embed.add_field(name=":x: Error", value="You need a user name!\n **Example:** \n ?givemoney @User")
        await client.say(embed=embed)
        return
    if amount is None:
        embed = discord.Embed(color=(random.randint(0, 0xffffff)))
        embed.add_field(name=":x: Error", value="You need a amount!\n **Example:** \n ?givemoney @User 5")
        await client.say(embed=embed)
        return
    if amount > coins[ctx.message.server.id][author.id]:
        embed = discord.Embed(color=(random.randint(0, 0xffffff)))
        embed.add_field(name=":x: Error", value="You have no money in your balance!")
        await client.say(embed=embed)
        return
    if not ctx.message.server.id in coins:
        coins[ctx.message.server.id] = {}
    if not user.id in coins[ctx.message.server.id]:
        coins[ctx.message.server.id][user.id] = 0
    coins[ctx.message.server.id][user.id] += amount
    coins[ctx.message.server.id][author.id] -= amount
    embed = discord.Embed(color=(random.randint(0, 0xffffff)))
    embed.add_field(name="Money Added!", value=f"Added **${amount}** to {user.mention}!", inline=False)
    embed.set_thumbnail(url=user.avatar_url)
    await client.say(embed=embed)
    with open("economy.json", "w") as f:
        json.dump(coins, f, indent=4)

@client.command(pass_context=True)
@commands.cooldown(1, 864000, commands.BucketType.user)
async def crate(ctx):
    with open("economy.json", "r") as f:
        coins = json.load(f)
    author = ctx.message.author
    crate = random.randint(100, 900)
    cratenames = [
        "King Crate",
        "Savage Crate",
        "Med Crate"
    ]
    if not ctx.message.server.id in coins:
        coins[ctx.message.server.id] = {}
    if not author.id in coins[ctx.message.server.id]:
        coins[ctx.message.server.id][author.id] = 0
    coins[ctx.message.server.id][author.id] += crate
    embed = discord.Embed(color=(random.randint(0, 0xffffff)))
    embed.add_field(name=":inbox_tray: | Crate Opened!", value=f"You have opened the ***{(random.choice(cratenames))}***", inline=False)
    embed.add_field(name=":moneybag: | Coin Amount:", value=f"**${crate}**", inline=False)
    await client.say(embed=embed)
    with open("economy.json", "w") as f:
        json.dump(coins, f, indent=4)
@crate.error
async def cooldown_error(error, ctx):
    if isinstance(error, commands.CommandOnCooldown):
        remainder = divmod(error.retry_after, 864000)
        embed = discord.Embed(color=(random.randint(0, 0xffffff)))
        embed.add_field(name="Slowdown :stuck_out_tongue_winking_eye: ", value=f"Cooldown: **{remainder}** \n Each Command: **1**", inline=False)
        await client.say(embed=embed)

@client.command(pass_context=True)
async def crates(ctx):
    embed = discord.Embed(color=(random.randint(0, 0xffffff)))
    embed.add_field(name="Crates Avaliable", value="King Crate \n Savage Crate \n Med Crate")
    embed.add_field(name="How to get them", value="**Type ?crate for a random crate out of those 3**")
    await client.say(embed=embed)





@client.command(pass_context=True)
async def bal(ctx, user: discord.Member = None):
    with open("economy.json", "r") as f:
        coins = json.load(f)
    author = ctx.message.author
    if ctx.message.author.bot:
        await client.say("Bot's will not use my commands. Those other bots will store my data full of junk!")
        return
    if user is None:
        if not author.id in coins[ctx.message.server.id]:
            coins[ctx.message.server.id][author.id] = 0
        coinss = coins[ctx.message.server.id][author.id]
        embed = discord.Embed(color=(random.randint(0, 0xffffff)))
        embed.add_field(name="Account Owner:", value=f"{author.mention}", inline=False)
        embed.add_field(name="Account Balance:", value=f"**${coinss}**", inline=False)
        embed.set_thumbnail(url=author.avatar_url)
        embed.set_footer(icon_url=author.avatar_url, text=f"Requested by: {author.name}")
        await client.say(embed=embed)
        return
    if not user.id in coins[ctx.message.server.id]:
        coins[ctx.message.server.id][user.id] = 0
    coinss = coins[ctx.message.server.id][user.id]
    embed = discord.Embed(color=(random.randint(0, 0xffffff)))
    embed.add_field(name="Account Owner:", value=f"{user.mention}", inline=False)
    embed.add_field(name="Account Balance:", value=f"**${coinss}**", inline=False)
    embed.set_thumbnail(url=user.avatar_url)
    embed.set_footer(icon_url=user.avatar_url, text=f"Requested by: {author.name}")
    await client.say(embed=embed)


#Action Commands

@client.command(pass_context=True)
async def cat(ctx):
    if ctx.message.author.bot:
        await client.say("Bots can't use commands.")
        return
    response = requests.get('https://aws.random.cat/meow')
    data = response.json()
    embed = discord.Embed(title= "Cute Cat!", color=0x08202D)
    embed.set_image(url=f"{data['file']}")
    embed.set_footer(text=f"Requested By: {ctx.message.author}")
    await client.say(embed=embed)

@client.command(pass_context=True)
async def dog(ctx):
    if ctx.message.author.bot:
        await client.say("Bots can't use commands.")
        return
    response = requests.get('https://random.dog/woof.json')
    data = response.json()
    embed = discord.Embed(title="Cute Doggys!", color=0x08202D)
    embed.set_image(url=f"{data['url']}")
    embed.set_footer(text=f"Requested By: {ctx.message.author}")
    await client.say(embed=embed)


@client.command(pass_context=True)
async def kiss(ctx, user: discord.Member = None):
    if ctx.message.author.bot:
        await client.say("Bots can't use commands.")
        return
    if user is None:
        await client.say("Specify a user please.")
        return
    response = requests.get("https://nekos.life/api/v2/img/kiss")
    data = response.json()
    data = response.json()
    embed = discord.Embed(title=f"Kiss {user.name}", color=0x08202D)
    embed.set_image(url=f"{data['url']}")
    embed.set_footer(text=f"Requested By: {ctx.message.author}")
    await client.say(embed=embed)

    
@client.command(pass_context=True)
async def cuddle(ctx, user: discord.Member = None):
    if ctx.message.author.bot:
        await client.say("Bots can't use commands.")
        return
    if user is None:
        await client.say("Specify a user please.")
        return
    response = requests.get("https://nekos.life/api/v2/img/cuddle")
    data = response.json()
    data = response.json()
    embed = discord.Embed(title=f"Cuddle {user.name}", color=0x08202D)
    embed.set_image(url=f"{data['url']}")
    embed.set_footer(text=f"Requested By: {ctx.message.author}")
    await client.say(embed=embed)

@client.command(pass_context=True)
async def slap(ctx, user: discord.Member = None):
    if ctx.message.author.bot:
        await client.say("Bots can't use commands.")
        return
    if user is None:
        await client.say("Specify a user please.")
        return
    response = requests.get("https://nekos.life/api/v2/img/slap")
    data = response.json()
    data = response.json()
    embed = discord.Embed(title=f"Slapped The Fuck Out Of {user.name}", color=0x08202D)
    embed.set_image(url=f"{data['url']}")
    embed.set_footer(text=f"Requested By: {ctx.message.author}")
    await client.say(embed=embed)

@client.command(pass_context=True)
async def hug(ctx, user: discord.Member = None):
    if ctx.message.author.bot:
        await client.say("Bots can't use commands.")
        return
    if user is None:
        await client.say("Specify a user please.")
        return
    response = requests.get("https://nekos.life/api/v2/img/hug")
    data = response.json()
    data = response.json()
    embed = discord.Embed(title=f"Hugged {user.name}", color=0x08202D)
    embed.set_image(url=f"{data['url']}")
    embed.set_footer(text=f"Requested By: {ctx.message.author}")
    await client.say(embed=embed)



@client.command(pass_context=True)
async def shibe(ctx):
    if ctx.message.author.bot:
        await client.say("Bots can't use commands.")
        return
    request = requests.get('http://shibe.online/api/shibes')
    link = request.json()[0]
    embed = discord.Embed(title='Shibe', color=0x08202D)
    embed.set_image(url=link)
    embed.set_footer(text=f"Requested By: {ctx.message.author}")
    await client.say(embed=embed)

@client.command(pass_context=True)
async def bird(ctx):
    if ctx.message.author.bot:
        await client.say("Bots can't use commands.")
        return
    response = requests.get('https://some-random-api.ml/birbimg')
    data = response.json()
    embed = discord.Embed(color=0x08202D)
    embed.set_image(url=f"{data['link']}")
    await client.say(embed=embed)

@client.command(pass_context=True)
async def duck(ctx, module="img"):
    module = module.lower()
    if ctx.message.author.bot:
        await client.say("Bots can't use commands.")
        return
    if module == "gif":
        response = requests.get('https://random-d.uk/api/v1/random?type=gif')
        data = response.json()
        embed = discord.Embed(color=0x08202D)
        embed.set_image(url=f"{data['url']}")
        await client.say(embed=embed)
    if module == "img":
        response = requests.get('https://random-d.uk/api/v1/random?type=jpg')
        data = response.json()
        embed = discord.Embed(color=0x08202D)
        embed.set_image(url=f"{data['url']}")
        await client.say(embed=embed)
                        
#Give away
@client.command(pass_context = True)
async def giveaway(ctx):
    if ctx.message.author.server_permissions.manage_server:
        if ctx.message.author.bot:
            await client.say("Bots can't use commands.")
            return
        """Create a giveaway throught an interactive setup!"""
        await client.say(":tada: WooHoo!!!! We will create your giveaway :tada:")
        await asyncio.sleep(1)
        await ctx.bot.say("What channel will the Giveaway be help in?\n"
                        "\n"
                        "`Ex. Do a channel in your server. ('general' not #general)`")
        channel_name = await client.wait_for_message(author = ctx.message.author)
        g_channel = discord.utils.get(ctx.message.server.channels, name = channel_name.content)
    
        #Check if the channel even exists!
        if not g_channel:
            await client.say(":x: | Channel Not Found! | Start Over!")
        if g_channel:
            await client.say(":white_check_mark: | Channel Found And Selected!")
            await asyncio.sleep(1)
            await client.say("How long will the Giveaway Be?\n"
                            "\n"
                            "Ex. 5 Minutes, say 5m, 1 Hour, say 1h ,etc. (Please only use Whole Numbers!")
            duration = await client.wait_for_message(author = ctx.message.author)
            await asyncio.sleep(1)
            await client.say(":tada: Giveaway set to end {} after the start".format(duration.content))
            await asyncio.sleep(1)
            await client.say("How many winner will be selected?\n"
                              "\n"
                              "`Pick a Number 1 (More Winners Coming Soon!)`")
            msg = await client.wait_for_message(author = ctx.message.author)
            g_winners = int(msg.content)
            await asyncio.sleep(1)
            await client.say(":tada: {} Winner(s) will be Chosen".format(g_winners))
            await asyncio.sleep(1)
            await client.say("What are you giving away?\n"
                            "\n"
                            "`This Will Become The Title Of The Giveaway`\n"
                            "`Ex. If I'm Giving away Free Steam Keys I Would say Free Steam Keys`")
            g_prize = await ctx.bot.wait_for_message(author = ctx.message.author)
            await asyncio.sleep(1)
            await client.say("Giving away {}".format(g_prize.content))
            await asyncio.sleep(1)
            await client.say(":tada: Almost Done Please Confirm Below")
            await asyncio.sleep(1)
            await client.say("You are Giving away `{}` with `{}` Winners, that will Last `{}`?\n"
                            "\n"
                            "`If This Is Correct Say Yes. If Not Say No (You Will Have To Start Over)`".format(g_prize.content, g_winners, duration.content))
            response = await client.wait_for_message(author = ctx.message.author, channel = ctx.message.channel)
            response = response.content.lower()

            duration = duration.content

            unit = duration[-1]
            if unit == 's':
                time = int(duration[:-1])
                longunit = 'seconds'
            elif unit == 'm':
                time = int(duration[:-1]) * 60
                longunit = 'minutes'
            elif unit == 'h':
                time = int(duration[:-1]) * 60 * 60
                longunit = 'hours'
            else:
                return

            yesres = 'yes'
            nores = 'no'
            if response.lower() == nores.lower():
                await asyncio.sleep(1)
                await client.say(":x: | Giveaway Canceled, Please Restart The Setup")
            if response.lower() == yesres.lower():
                await client.say(":tada: Giveaway Started! :tada:")

                color = ''.join([random.choice('0123456789ABCDEF') for x in range(6)])
                color = int(color, 16)
                embed=discord.Embed(title=":tada: __**Giveaway: {}**__ :tada:".format(g_prize.content), colour = discord.Colour(value=color), timestamp = datetime.datetime.utcnow())
                embed.add_field(name = "Prize: ",value = "{}".format(g_prize.content))
                embed.add_field(name = "Winners: ", value = "{} Winner(s)".format(g_winners))
                embed.add_field(name = "Time: ", value = "{}".format(duration), inline = True)
                embed.set_footer(text = "Add The Reaction to join! Started @ ")
                give_away = await client.send_message(g_channel, embed = embed)
                ga_message = await client.add_reaction(give_away, "\U0001f389")
                await asyncio.sleep(time)#Sleep for the duration

                ga_message = await client.get_message(give_away.channel, give_away.id)
                ga_users=[]
                for user in await client.get_reaction_users(ga_message.reactions[0]):
                    ga_users.append(user.mention)
                ga_client = ctx.message.server.get_member('503386558976622593') #giveaways id 396464677032427530
                ga_users.remove(ga_client.mention)
                if len(ga_users) == 0:
                    error = discord.Embed(title=":warning: Error!",description="The giveaway ended with no participants, could not chose a winner",color=0xff0000)
                    await client.say(embed=error)
                else:
                    winner_list=[]
                    for loop in range(g_winners):
                        winner = random.choice(ga_users)
                        ga_users.remove(winner)
                        winner_list.append(winner)
                        msg = ""
            
                color = ''.join([random.choice('0123456789ABCDEF') for x in range(6)])#Winning Embed
                color = int(color, 16)
                embed=discord.Embed(title=":tada: __**Giveaway Ended!**__ :tada:", colour = discord.Colour(value=color), timestamp = datetime.datetime.utcnow())
                embed.add_field(name = "Winners: ", value = "{} Winner(s)".format(g_winners))
                embed.add_field(name = "Winner(s): ", value = ",\n".join(winner_list))
                embed.add_field(name = "Prize: ", value = "{}".format(g_prize.content))
                embed.set_footer(text = "Better Luck Next Time! Ended @ ")
                await client.edit_message(give_away, embed = embed)
                for winner in winner_list:
                    msg += ", " + winner
                await client.send_message(g_channel, ":tada: " + ", ".join(winner_list) + " won **{}**".format(g_prize.content))
    else:
        embed = discord.Embed(color=0xff0200)
        author = ctx.message.author
        embed.set_author(icon_url=author.avatar_url, name="Uh Oh.")
        embed.add_field(name=":x: Error", value="You are missing some permissions there bud. ```Permissions: Manage Server```", inline=False)
        await client.say(embed=embed)
                        
        
    
        
  
client.run(os.environ.get('BOT_TOKEN'))
