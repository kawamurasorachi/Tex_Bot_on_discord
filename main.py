import os
import discord
from dotenv import load_dotenv
import manage_tex
import datetime
from PIL import Image

load_dotenv(override=True)
client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_message(message):
    if '```tex' in message.content:
        now = datetime.datetime.now()
        manage_tex.get_tex_image(message.content[7:-3],now)
        im = Image.open(f'data/{now}.png')
        manage_tex.add_margin(im,25,50,25,50,(255,255,255)).save(f'data/{now}.png', quality=95)
        with open(f'data/{now}.png', 'rb') as f:
            image = discord.File(f)
            await message.channel.send(file=image)
        os.remove(f'data/{now}.png')

client.run(os.environ.get("DISCORD_TOKEN"))