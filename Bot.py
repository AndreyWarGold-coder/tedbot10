import discord 
from discord.ext import commands
from discord.ext.commands import Bot

Bot = commands.Bot(command_prefix = "!")
ukr = False
ukrl = ["Героям слава", "Героям слава!", "Смерть ворогам"]
money = [[], []]
rol = [["Аутист", "Бронзовый аутист", "Серебряный аутист", "Золотой аутист", "Повелитель аутистов"],
       ["Голубь", "Резиновый голубь", "Пластмасовый голубь", "Роботизированый голубь", "Голубь-терминатор"]]

@Bot.event
async def on_ready():
	print("Bot is working...")

@Bot.event
async def on_message(message):
	global ukr, ukrl
	if message.author == Bot.user:
		return
	if ukr == True:
		if message.content in ukrl :
			await message.channel.send("Наш козак!")
			ukr = False
		else:
			await message.channel.send("Москаль!")
			ukr = False
			return
	if message.content == "Hello":
		await message.channel.send("Хеллоу енглишмэн!")
	if message.content == "Привет":
		await message.channel.send("Привет!")
	if message.content == "Привіт":
		await message.channel.send("Здоровенькі були! Слава Україні!")
		ukr = True
	if message.content == "!баланс":
		global money
		if message.author.name in money[0]:
			print(123)

		else:
			money[0].append(message.author.name)
			money[1].append(100)
		await message.channel.send("Баланс " + message.author.name + ": "+ str(money[1][money[0].index(message.author.name)]) + "$" )
	if message.content.startswith("!передать"):
		msg = message.content.split(" ")
		if msg[1] in money[0]:
			if money[1][money[0].index(message.author.name)] >= int(msg[2]):
				money[1][money[0].index(message.author.name)] -= int(msg[2])
				money[1][money[0].index(msg[1])] += int(msg[2])
				await message.channel.send("Пользователю " + msg[1] + " передано " + msg[2] + "$") 
		else:
			await message.channel.send("Такого пользователя в системе нету!")
	if message.content == "!апгрейд":
		l = str(message.author.roles).split("'")
		if l[3] in rol[0]:
			print(message.author.roles)
		elif l[3] in rol[1]:
			print(message.author.roles)



Bot.run("NjQ1MjM2OTk5MDQwNTMyNTAw.XdrDdA.d6OKaf5kTIQIPHIho6MeUjuw4ms")
