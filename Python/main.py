import discord
import json 

client = discord.Client()
reader = open('seçenekler.json',) 

data = json.load(reader) 

reader.close();

@client.event
async def on_ready():

	guild_count = 0

	for guild in client.guilds:
		print(f" {guild.id} (name: {guild.name}) IDli sunucuya bağlanıldı")

		guild_count = guild_count + 1


@client.event
async def on_message(message):

	if message.content == "Sa":
		await message.channel.send("Aleyküm selam, hoşgeldin!")

client.run(data['token'])
# Eric Chi'ye teşekkürler. https://medium.com/better-programming/coding-a-discord-bot-with-python-64da9d6cade7
