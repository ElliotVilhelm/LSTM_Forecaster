from discord import Client

CHANNEL_ID = 733516071289487460

client = Client()


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
