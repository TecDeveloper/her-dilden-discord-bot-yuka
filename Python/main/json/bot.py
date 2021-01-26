import discord
import json

def getJSON(filePathAndName):
    with open(filePathAndName, 'r') as fp:
        return json.load(fp)

client = discord.Client();
token = getJSON('./Python/main/json/seçenekler.json').get('token',token_bulunamadı)

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

client.run(token)
