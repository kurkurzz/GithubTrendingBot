import discord
from discord.utils import get
from github_api import get_top_repo
import os

client = discord.Client()

@client.event
async def on_ready():
    for guild in client.guilds:
        channel =  get(guild.text_channels,name='💌share-your-tech')
        if channel is not None:
            top_repo = get_top_repo()
            display_text = f'Top GitHub repo for today is **{top_repo.name}** by **{top_repo.author}**.' \
                f'\nLink: {top_repo.url}'
            message = await channel.send(display_text)
            await message.add_reaction('💻')
            await client.close()
            await client.close()

client.run(os.environ['TOKEN'])