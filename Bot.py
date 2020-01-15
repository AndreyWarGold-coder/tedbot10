import discord 
from discord.ext import commands
from discord.ext.commands import Bot
import os
import random

Bot = commands.Bot(command_prefix = "!")
ukr = False
ukrl = ["героям слава", "героям слава!", "смерть ворогам"]
money = [[], []]
music = ["music", "музыка", "включи музыку", "врубай шарманку", "шансон"]
music_list = ["Opa gagnam style"]
rol = [["Аутист", "Бронзовый аутист", "Серебряный аутист", "Золотой аутист", "Повелитель аутистов"],
       ["Голубь", "Резиновый голубь", "Пластмасовый голубь", "Роботизированый голубь", "Голубь-терминатор"]]

@Bot.command(pass_context=True)
async def music(ctx):
	channel = ctx.message.author.voice.channel
	await channel.connect()


@Bot.event
async def on_ready():
	print("Bot is working...")

@Bot.event
async def on_message(message):
	global ukr, ukrl, money
	if message.author == Bot.user:
		return
	if ukr == True:
		if message.content.lower in ukrl :
			await message.channel.send("Наш козак!")
			ukr = False
		else:
			await message.channel.send("Москаль!")
			ukr = False
			return
	if message.content.lower == "заработать":
		
		if message.author.name in money[0]:
			print(123)

		else:
			money[0].append(message.author.name)
			money[1].append(100)
		money[1][money[0].index(message.author.name)] += 1
		await message.delete()
	if message.content == "hello":
		await message.channel.send("Хеллоу енглишмэн!")
	if message.content in music:
		ch = message.author.voice.channel
		await ch.connect()
		for gg in range(len(music_list)):
			await message.channel.send("-ph " + music_list[gg])
		await voice_client.disconnect()
	if message.content.lower == "привет":
		await message.channel.send("Привет!")
	if message.content.lower == "привіт":
		await message.channel.send("Здоровенькі були! Слава Україні!")
		ukr = True
	if message.content.lower == "!баланс":
		if message.author.name in money[0]:
			print(123)

		else:
			money[0].append(message.author.name)
			money[1].append(100)
		await message.channel.send("Баланс " + message.author.name + ": "+ str(money[1][money[0].index(message.author.name)]) + "$" )
	if message.content.lower.startswith("!передать"):
		msg = message.content.split(" ")
		if msg[1] in money[0]:
			if money[1][money[0].index(message.author.name)] >= int(msg[2]):
				money[1][money[0].index(message.author.name)] -= int(msg[2])
				money[1][money[0].index(msg[1])] += int(msg[2])
				await message.channel.send("Пользователю " + msg[1] + " передано " + msg[2] + "$") 
		else:
			await message.channel.send("Такого пользователя в системе нету!")
	if message.content.lower == "!апгрейд":
		l = str(message.author.roles).split("'")
		if l[3] in rol[0]:
			await Bot.add_role(message.author, rol[0][rol[0].index(l[3])+1])
			
		elif l[3] in rol[1]:
			print(message.author.roles)



Bot.run(os.environ.get("Bot_Token"))