# bot.py
import os
import discord


client = discord.Client()

@client.event
async def on_ready():
   print("BOT ESTÁ ONLINE")


@client.event
async def on_message(message):
    content = message.content.lower()
    channel = message.channel
    author = message.author.name
    mention =  message.author.mention
    # Previnir erro  
    if author == "GG!":
        return

    if content == "bom dia":
        await channel.send("bom dia" + mention)

    if content == "ping":
        await channel.send("pong"  + mention)

    if content == "f":
        await channel.send("Press F to pay respect!  "+ '😞  ' + mention, file=discord.File('Midia/Press_F.gif'))

    if content == "que fome":
        await channel.send("Que tal uma sopinha  " + mention)

    if content == "que vontade":
        await channel.send("De comer um Bolo?  " + mention)

    if content == " ":
        await channel.send(" " + mention)


client.run('ODUxNjEzMjkzNjgzNTQwMDEw.YL60rw.CbI9xckllqZVtqB0oS7KwRM5vrQ')