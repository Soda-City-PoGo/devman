# devman
this is a bot to control devices thru discord, using **USB connected devices only**!!! 

wifi support soon!
https://github.com/libimobiledevice/libimobiledevice
https://github.com/libimobiledevice/libimobiledevice/issues/845


I did not make this, i found it on discord and put it on github for others to use.

Create a discord bot here -> https://discordapp.com/developers/applications/me

once you have it setup in your portal, invite it to your server.

clone this to the pc/vm that phones are running on

`git clone https://github.com/Soda-City-PoGo/devman.git`

then `cd devman`


############## INSTRUCTIONS to install discord py for python 3.7 ############

`python3 -m pip install discord.py==0.16.12`

`python3 -m pip install -U https://github.com/Rapptz/discord.py/archive/async.zip#egg=discord.py[voice]`

`pip3 install --upgrade aiohttp`

`pip3 install --upgrade websockets`

############## INSTRUCTIONS to install libmobiledevice ############

`brew update`

`brew uninstall --ignore-dependencies libimobiledevice`

`brew uninstall --ignore-dependencies usbmuxd`

`brew install --HEAD usbmuxd`

`brew unlink usbmuxd`

`brew link usbmuxd`

`brew install --HEAD libimobiledevice`

`brew unlink libimobiledevice && brew link libimobiledevice`

`brew install --HEAD  ideviceinstaller`

`brew unlink ideviceinstaller && brew link ideviceinstaller`

`sudo chmod -R 777 /var/db/lockdown/`

After installed edit deviceM.py

enter bot token on line 7

replace `BOT_TOKEN` with your token.

`TOKEN = 'BOT_TOKEN'`

then list your devices here

@client.event
async def on_message(message):
    devices={`'iphone1':'UUID',
             'iphone2':'UUID'`}

you can also add a listen channel to restrict access if you want.

##### Start the bot #####

`python3 deviceM.py`


