from dotenv import load_dotenv
load_dotenv()

import os
import discord
import requests

class ShibesBot(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        if message.content == "!shib" or message.content == "!shibe":
            try:
                shibImage = requests.get("http://shibe.online/api/shibes?count=1&urls=true&httpsUrls=true")
                await message.channel.send(shibImage.json()[0])
            except:
                await message.channel.send("Could not connect to API :(")

client = ShibesBot()
client.run(os.environ.get('DISCORD_TOKEN'))