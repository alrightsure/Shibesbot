from dotenv import load_dotenv
load_dotenv()

import os
import discord
import requests

class ShibesBot(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        if message.content.lower().strip() == "!shib" or message.content.lower().strip() == "!shibe":
            try:
                shibImage = requests.get(os.environ.get('API_URL'))
                await message.channel.send(shibImage.json()[0])
            except:
                await message.channel.send("Could not connect to API :(")

client = ShibesBot()
client.run(os.environ.get('DISCORD_TOKEN'))