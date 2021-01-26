import discord

client = discord.Client();

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

client.run(your_token_here)
