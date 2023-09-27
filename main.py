import discord

TOKEN = 'MTE1NjU1MTgzMDc0MzAzNTk5Ng.GeMglO.lnaZMCFoQk2fYd9numItL3Qg9-eVaTdfh2pDHM'

intents = discord.Intents.default()
intents.message_content = True

bot = discord.Client(intents=intents)

@bot.event
async def on_message(message):
    if message.author.bot:
        return ()
    
    if "https://" in message.content.lower():
        await message.channel.send(f"{message.author.mention}Link is not ALLOWED!!!")
        await message.delete()

    await bot.process_commands(message)

@bot.event
async def on_ready():
    print(f"{bot.user} is ready.")

bot.run(TOKEN)