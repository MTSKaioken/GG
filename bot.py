# bot.py
import os
import discord

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'{client.user} está conectado ao gg!')

@client.event
async def on_member_join(Member):
    channel = client.get_channel(851624894784339991)
    await channel.send("bem vindo!!!" +Member.mention)

client.run('ODUyMzYzMDI0NjQ2OTMwNDYy.YMFu7Q.jj1MMCW0zbaXgxYwkR_As2X6rM8')
