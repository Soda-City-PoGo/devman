# Work with Python 3.7
import discord
import subprocess
from discord.utils import get
import os, fnmatch

TOKEN = 'BOT_TOKEN'

client = discord.Client()

def find(pattern, path):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    return result
@client.event
async def on_message(message):
    devices={'iphone1':'UUID',
			'iphone2':'UUID'}

    # we do not want the bot to reply to itself
    if message.author == client.user:
        return
    # to reboot device
    if message.content.startswith('!reboot'):
        
        args = message.content.split(" ")
        MyOut = subprocess.Popen(['idevicediagnostics', '-u', devices.get(args[1]), 'restart'],stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        stdout,stderr = MyOut.communicate()
        await client.send_message(message.channel, stdout.decode("utf-8") )

    # take screenshot of device
    if message.content.startswith('!sc'):
        args = message.content.split(" ")
        MyOut = subprocess.Popen(['idevicescreenshot', '-u', devices.get(args[1]), args[1]+'.png'],stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        stdout,stderr = MyOut.communicate()
        
        await client.send_file(message.channel, args[1]+'.png')
    # in progress: Send last 10 lines of full log of device
    if message.content.startswith('!flog'):
        args = message.content.split(" ")
        name = '"*'+args[1]+'*"'
        fulllog = '"*full*"'
        MyOut = subprocess.Popen(['find', '.', '-amin' , '1', '-name', name, '!', '-name', fulllog, '-print'],stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        stdout,stderr = MyOut.communicate()
        #await client.send_message(message.channel, r[0] )
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    
client.run(TOKEN)
