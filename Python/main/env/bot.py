import discord
import os

from dotenv import load_dotenv

from discord.ext import commands

load_dotenv()

TOKEN = os.getenv("TOKEN")

client = discord.Client();

@client.event
async def on_message(message):
	if message.content == "Sa":
		await message.channel.send("Aleyküm selam, hoşgeldin.")

	await bot.process_commands(message)

client.run(TOKEN)
