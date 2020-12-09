import discord
from discord.utils import get
from github_api import get_top_repo
from credentials import TOKEN

client = discord.Client()

@client.event
async def on_message(message):
    if message.author!=client.user:
        for guild in client.guilds:
            channel =  get(guild.text_channels,name='💌share-your-tech')
            if channel is not None:
                top_repo = get_top_repo()
                display_text = f'Top GitHub repo for today is **{top_repo.name}** by **{top_repo.author}**' \
                    f'Link: {top_repo.url}'
                await channel.send(display_text)


client.run(TOKEN)