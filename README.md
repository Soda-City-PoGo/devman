# devman
this is a bot to control devices thru discord, using USB only atm, wifi support soon!


I did not make this, i found it on discord and put it on github for others to use.

clone this to the pc/vm that phones are running on

Create a discord bot here -> https://discordapp.com/developers/applications/me

make sure bot has admin access and invite it to your server.


############## INSTRUCTIONS to install discord py for python 3.7 ############

python3 -m pip install discord.py==0.16.12
python3 -m pip install -U https://github.com/Rapptz/discord.py/archive/async.zip#egg=discord.py[voice]
pip3 install --upgrade aiohttp
pip3 install --upgrade websockets

############## INSTRUCTIONS to install libmobiledevice ############
brew update
brew uninstall --ignore-dependencies libimobiledevice
brew uninstall --ignore-dependencies usbmuxd
brew install --HEAD usbmuxd
brew unlink usbmuxd
brew link usbmuxd
brew install --HEAD libimobiledevice
brew unlink libimobiledevice && brew link libimobiledevice
brew install --HEAD  ideviceinstaller
brew unlink ideviceinstaller && brew link ideviceinstaller
sudo chmod -R 777 /var/db/lockdown/
