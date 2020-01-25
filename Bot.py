import discord 
from discord.ext import commands
from discord.ext.commands import Bot
from discord import utils
import os
import random

Bot = commands.Bot(command_prefix = "!")
ukr = False
ukrl = ["героям слава", "героям слава!", "смерть ворогам"]
mafia_roles = ["мафия", "врач", "путана", "мирный", "шериф"]
money = [[], [], [], [], [], [], [], []]
mafia_gamer = []
mafia_kill = []
list_golos = []
mafia_kill = []
mafia_game = False
mafia_start = False
mafia = False
list_goloskill = []
list_gamer = []
mafia_role = []
mafia_role2 = []
mafia_heal = ""
mafia_sherif = ""
mafia_putana = ""
save = False
music = ["music", "музыка", "включи музыку", "врубай шарманку", "шансон"]
music_list = ["Opa gagnam style"]
rol = [["Аутист", "Бронзовый аутист", "Серебряный аутист", "Золотой аутист", "Повелитель аутистов"],
       ["Голубь", "Резиновый голубь", "Пластмасовый голубь", "Роботизированый голубь", "Голубь-терминатор"]]


@Bot.event
async def on_ready():
	print("Bot is working...")

@Bot.event
async def on_raw_reaction_add(payload):
	if str(payload.emoji) == '😀':
		print("true is emoji " + utils.get(Bot.get_all_members(), id=str(payload.user_id)).name)

@Bot.event
async def on_message(message):
	global  money, music_list, jg, save, save_msg, list_gamer, mafia, mafia_start, mafia_role, mafia_roles, mafia_hod, mafia_game, mafia_gamer, mafia_kill, mafia_night, mafia_putana, mafia_heal, mafia_sherif, list_golos, list_goloskill, mafia_role2
	if message.author == Bot.user:
		if save == True:
			save = False
			save_msg = message
		return
	mgg = message.content.lower()
	if mafia_game == True and mgg =="!цифра":
		kk = ""
		for v in range(len(mafia_gamer)):
			kk += '\n' + mafia_gamer[v] + " - " + str(v)
		await message.channel.send(kk)
	if mgg == "!мафия выкл":
		await message.channel.send("Игра отключена")
		mafia = False
		mafia_start = False
		mafia_game = False
		mafia_hod = ""
		mafia_kill = []
		mafia_role = []
		mafia_role2 = []
		mafia_sherif = ""
		mafia_gamer = []
		mafia_heal = ""
		mafia_night = 0
		list_gamer = []
		list_golos = []
		list_goloskill = []
	if mafia_game == True and not mgg in mafia_gamer and int(mgg) < len(mafia_gamer) :
		mgg = mafia_gamer[int(mgg)]	
	if mafia_game == True:
		if mgg in mafia_gamer and message.author.name.lower() in mafia_gamer and mgg !=message.author.name.lower() and mafia_hod == "голосование" and list_golos.count(message.author.name.lower()) == 0:
			list_golos.append(message.author.name.lower())
			list_goloskill.append(mgg)
			await jg.send("Засчитан голос против " + mgg + ". Против него " + str(list_goloskill.count(mgg)) + " голосов")
			if len(list_golos) >= len(mafia_gamer):
				jj = 0
				gkill = ""
				for r in range(len(list_goloskill)):
					if list_goloskill.count(list_goloskill[r]) > jj:
						jj = list_goloskill.count(list_goloskill[r])
						gkill = list_goloskill[r]
				#await jg.send("Сегодне город решил убить " + gkill)
				mafia_gamer.remove(gkill)
				mafia_role.remove(money[5][money[0].index(gkill)])
				#await jg.send("Его роль была: " + money[5][money[0].index(gkill)])
				emb = discord.Embed(title = "Город решил казнить " + gkill , color = 0xe74c3c)
				emb.add_field(name = "Его роль:", value = money[5][money[0].index(gkill)])
				emb.set_thumbnail(url=money[6][money[0].index(gkill)].avatar_url)
				await jg.send(embed = emb)
				list_goloskill = []
				list_golos = []
				gkill = ""
				jj = 0
				mafia_night +=1
				#await jg.send("Начинается " + str(mafia_night) + " ночь")
				await save_msg.delete()
				emb = discord.Embed(title = str(mafia_night) + " ночь. Город засыпает..." , color = 0xe74c3c)
				emb.add_field(name = "Живые игроки:", value = mafia_gamer)
				emb.set_thumbnail(url="https://moika78.ru/news2/2019/02/1111-246.jpg")
				save = True
				await jg.send(embed = emb)
				await jg.send("Просыпается мафия...")
				mafia_hod = "мафия"
				if mafia_role.count("мафия") >= len(mafia_role)- mafia_role.count("мафия"):
					#await jg.send("Мафия выиграла!")
					emb = discord.Embed(title ="Мафия выиграла!" , color = 0xe74c3c)
					emb.add_field(name = "Мафией был: ", value = mafia_gamer[mafia_role.index("мафия")])
					emb.set_thumbnail(url="https://imgtest.mir24.tv/uploaded/images/crops/2017/September/870x489_0x244_detail_crop_ec6c59acb9fff1edae8eb73d4159301f.jpg")
					await jg.send(embed = emb)
					mafia_game = False
					list_gamer = []
					mafia_role = []
					mafia_gamer = []
				if mafia_role.count("мафия") == 0  and len(mafia_role) != 0:
					#await jg.send("Победа мирных!")
					emb = discord.Embed(title ="Победа мирных!" , color = 0xe74c3c)
					emb.add_field(name = "Живые игроки: ", value = mafia_gamer)
					emb.set_thumbnail(url="https://cs8.pikabu.ru/post_img/big/2017/12/06/4/1512538652128363705.jpg")
					await jg.send(embed = emb)
					mafia_game = False
					list_gamer = []
					mafia_role = []
					mafia_gamer = []



		if mgg in mafia_gamer and message.author.name.lower() in mafia_gamer and mgg !=message.author.name.lower() and money[5][money[0].index(message.author.name.lower())] == "шериф" and mafia_hod == "шериф":
			if money[5][money[0].index(mgg)] == "мафия":
				mafia_sherif = mgg
			else:
				mafia_sherif = ""
			await jg.send("Шериф сделал свой выбор")
			mafia_hod = "голосование"
			#await jg.send("Город просыпается... Голосование, пишите в чат на кого думаете, что он мафия")
			#await jg.send(mafia_gamer)
			await save_msg.delete()
			emb = discord.Embed(title ="Город просыпается... И голосует, кто же мафия?" , color = 0xe74c3c)
			emb.add_field(name = "Живые игроки:", value = mafia_gamer)
			emb.set_thumbnail(url="https://static.mk.ru/upload/entities/2019/03/20/09/articles/detailPicture/34/50/5e/e2/e759dd8b2ed88f24f30646e7009e5e44.jpg")
			save = True
			await jg.send(embed = emb)
			for b in range (len(mafia_kill)):
				if mafia_kill[b] == mafia_heal:
					mafia_kill.remove(mafia_heal)
					mafia_heal = ""
			if mafia_putana == mafia_sherif:
				mafia_sherif =""
				mafia_putana = ""
			if mafia_role.count("мафия") >= len(mafia_role)- mafia_role.count("мафия"):
				#await jg.send("Мафия выиграла!")
				emb = discord.Embed(title ="Мафия выиграла!" , color = 0xe74c3c)
				emb.add_field(name = "Мафией был: ", value = mafia_gamer[mafia_role.index("мафия")])
				emb.set_thumbnail(url="https://imgtest.mir24.tv/uploaded/images/crops/2017/September/870x489_0x244_detail_crop_ec6c59acb9fff1edae8eb73d4159301f.jpg")
				await jg.send(embed = emb)
				mafia_game = False
				list_gamer = []
				mafia_role = []
				mafia_gamer = []
			else:
			#	await jg.send("Убито: "+ mafia_kill[0] + "  Его роль была: "+ money[5][money[0].index(mafia_kill[0])])
				mafia_role.remove(money[5][money[0].index(mafia_kill[0])])
				mafia_gamer.remove(mafia_kill[0])
				emb = discord.Embed(title = "Сегодня ночью было убито " + mafia_kill[0] , color = 0xe74c3c)
				emb.add_field(name = "Его роль:", value = money[5][money[0].index(mafia_kill[0])])
				emb.set_thumbnail(url=money[6][money[0].index(mafia_kill[0])].avatar_url)
				await jg.send(embed = emb)


				if mafia_sherif != "":
					await jg.send("Раскрыто мафию: " + mafia_sherif)
					mafia_role.remove("мафия")
					mafia_gamer.remove(mafia_sherif)
					mafia_sherif =""
				if mafia_role.count("мафия") == 0  and len(mafia_role) != 0:
						#await jg.send("Победа мирных!")
						emb = discord.Embed(title ="Победа мирных!" , color = 0xe74c3c)
						emb.add_field(name = "Живые игроки: ", value = mafia_gamer)
						emb.set_thumbnail(url="https://cs8.pikabu.ru/post_img/big/2017/12/06/4/1512538652128363705.jpg")
						await jg.send(embed = emb)
						mafia_game = False
						list_gamer = []
						mafia_role = []
						mafia_gamer = []

		if mgg in mafia_gamer and message.author.name.lower() in mafia_gamer and mgg !=message.author.name.lower() and money[5][money[0].index(message.author.name.lower())] == "врач" and mafia_hod == "врач":
			mafia_heal = mgg
			await jg.send("Врач сделал свой выбор")
			if "шериф" in mafia_role:
				mafia_hod = "шериф"
				await jg.send("Шериф проверяет кого-то из жителей...")
			else:
				mafia_hod = "голосование"
				#await jg.send("Город просыпается... Голосование, пишите в чат на кого думаете, что он мафия")
				#await jg.send(mafia_gamer)
				await save_msg.delete()
				emb = discord.Embed(title ="Город просыпается... И голосует, кто же мафия?" , color = 0xe74c3c)
				emb.add_field(name = "Живые игроки:", value = mafia_gamer)
				emb.set_thumbnail(url="https://static.mk.ru/upload/entities/2019/03/20/09/articles/detailPicture/34/50/5e/e2/e759dd8b2ed88f24f30646e7009e5e44.jpg")
				save = True
				await jg.send(embed = emb)
				for b in range (len(mafia_kill)):
					if mafia_kill[b] == mafia_heal:
						mafia_kill.remove(mafia_heal)
						mafia_heal = ""
				if mafia_putana == mafia_sherif:
					mafia_sherif =""
					mafia_putana = ""
				if mafia_role.count("мафия") >= len(mafia_role)- mafia_role.count("мафия"):
					#await jg.send("Мафия выиграла!")
					emb = discord.Embed(title ="Мафия выиграла!" , color = 0xe74c3c)
					emb.add_field(name = "Мафией был: ", value = mafia_gamer[mafia_role.index("мафия")])
					emb.set_thumbnail(url="https://imgtest.mir24.tv/uploaded/images/crops/2017/September/870x489_0x244_detail_crop_ec6c59acb9fff1edae8eb73d4159301f.jpg")
					await jg.send(embed = emb)
					mafia_game = False
					list_gamer = []
					mafia_role = []
					mafia_gamer = []
				else:
					#await jg.send("Убито: "+ mafia_kill[0] + "  Его роль была: "+ money[5][money[0].index(mafia_kill[0])])
					mafia_role.remove(money[5][money[0].index(mafia_kill[0])])
					mafia_gamer.remove(mafia_kill[0])
					emb = discord.Embed(title = "Сегодня ночью было убито " + mafia_kill[0] , color = 0xe74c3c)
					emb.add_field(name = "Его роль:", value = money[5][money[0].index(mafia_kill[0])])
					emb.set_thumbnail(url=money[6][money[0].index(mafia_kill[0])].avatar_url)
					await jg.send(embed = emb)


					if mafia_sherif != "":
						await jg.send("Раскрыто мафию: " + mafia_sherif)
						mafia_role.remove("мафия")
						mafia_gamer.remove(mafia_sherif)
						mafia_sherif =""
					if mafia_role.count("мафия") == 0  and len(mafia_role) != 0:
							#await jg.send("Победа мирных!")
							emb = discord.Embed(title ="Победа мирных!" , color = 0xe74c3c)
							emb.add_field(name = "Живые игроки: ", value = mafia_gamer)
							emb.set_thumbnail(url="https://cs8.pikabu.ru/post_img/big/2017/12/06/4/1512538652128363705.jpg")
							await jg.send(embed = emb)
							mafia_game = False
							list_gamer = []
							mafia_role = []
							mafia_gamer = []

		if mgg in mafia_gamer and message.author.name.lower() in mafia_gamer and mgg !=message.author.name.lower() and money[5][money[0].index(message.author.name.lower())] == "путана" and mafia_hod == "путана":
			mafia_putana = mgg
			await jg.send("Путана сделала свой выбор")
			if "врач" in mafia_role:
				mafia_hod = "врач"
				await jg.send("Врач выберает кого спасти...")
			elif "шериф" in mafia_role:
				mafia_hod = "шериф"
				await jg.send("Шериф проверяет кого-то из жителей...")
			else:
				mafia_hod = "голосование"
				#await jg.send("Город просыпается... Голосование, пишите в чат на кого думаете, что он мафия")
				#await jg.send(mafia_gamer)
				await save_msg.delete()
				emb = discord.Embed(title ="Город просыпается... И голосует, кто же мафия?" , color = 0xe74c3c)
				emb.add_field(name = "Живые игроки:", value = mafia_gamer)
				emb.set_thumbnail(url="https://static.mk.ru/upload/entities/2019/03/20/09/articles/detailPicture/34/50/5e/e2/e759dd8b2ed88f24f30646e7009e5e44.jpg")
				save = True
				await jg.send(embed = emb)
				for b in range (len(mafia_kill)):
					if mafia_kill[b] == mafia_heal:
						mafia_kill.remove(mafia_heal)
						mafia_heal = ""
				if mafia_putana == mafia_sherif:
					mafia_sherif =""
					mafia_putana = ""
				if mafia_role.count("мафия") >= len(mafia_role)- mafia_role.count("мафия"):
					#await jg.send("Мафия выиграла!")
					emb = discord.Embed(title ="Мафия выиграла!" , color = 0xe74c3c)
					emb.add_field(name = "Мафией был: ", value = mafia_gamer[mafia_role.index("мафия")])
					emb.set_thumbnail(url="https://imgtest.mir24.tv/uploaded/images/crops/2017/September/870x489_0x244_detail_crop_ec6c59acb9fff1edae8eb73d4159301f.jpg")
					await jg.send(embed = emb)
					mafia_game = False
					list_gamer = []
					mafia_role = []
					mafia_gamer = []
				else:
					#await jg.send("Убито: "+ mafia_kill[0] + "  Его роль была: "+ money[5][money[0].index(mafia_kill[0])])
					mafia_role.remove(money[5][money[0].index(mafia_kill[0])])
					mafia_gamer.remove(mafia_kill[0])
					emb = discord.Embed(title = "Сегодня ночью было убито " + mafia_kill[0] , color = 0xe74c3c)
					emb.add_field(name = "Его роль:", value = money[5][money[0].index(mafia_kill[0])])
					emb.set_thumbnail(url=money[6][money[0].index(mafia_kill[0])].avatar_url)
					await jg.send(embed = emb)


					if mafia_sherif != "":
						await jg.send("Раскрыто мафию: " + mafia_sherif)
						mafia_role.remove("мафия")
						mafia_gamer.remove(mafia_sherif)
						mafia_sherif =""
					if mafia_role.count("мафия") == 0  and len(mafia_role) != 0:
							#await jg.send("Победа мирных!")
							emb = discord.Embed(title ="Победа мирных!" , color = 0xe74c3c)
							emb.add_field(name = "Живые игроки: ", value = mafia_gamer)
							emb.set_thumbnail(url="https://cs8.pikabu.ru/post_img/big/2017/12/06/4/1512538652128363705.jpg")
							await jg.send(embed = emb)
							mafia_game = False
							list_gamer = []
							mafia_role = []
							mafia_gamer = []

		if mgg in mafia_gamer and message.author.name.lower() in mafia_gamer and mgg !=message.author.name.lower() and money[5][money[0].index(mgg)] != "мафия" and money[5][money[0].index(message.author.name.lower())] == "мафия" and mafia_hod == "мафия":
			mafia_kill = []
			mafia_kill.append(mgg)
			await jg.send("Мафия сделала свой выбор")
			if 'путана' in mafia_role:
				mafia_hod = "путана"
				await jg.send("Путана заходит к кому-то в гости...")
			elif 'врач' in mafia_role:
				mafia_hod = "врач"
				await jg.send("Врач выберает кого спасти...")
			elif 'шериф' in mafia_role:
				mafia_hod = "шериф"
				await jg.send("Шериф проверяет кого-то из жителей...")
			else:
				mafia_hod = "голосование"
				#await jg.send("Город просыпается... Голосование, пишите в чат на кого думаете, что он мафия")
				#await jg.send(mafia_gamer)
				await save_msg.delete()
				emb = discord.Embed(title ="Город просыпается... И голосует, кто же мафия?" , color = 0xe74c3c)
				emb.add_field(name = "Живые игроки:", value = mafia_gamer)
				emb.set_thumbnail(url="https://static.mk.ru/upload/entities/2019/03/20/09/articles/detailPicture/34/50/5e/e2/e759dd8b2ed88f24f30646e7009e5e44.jpg")
				save = True
				await jg.send(embed = emb)
				for b in range (len(mafia_kill)):
					if mafia_kill[b] == mafia_heal:
						mafia_kill.remove(mafia_heal)
						mafia_heal = ""
				if mafia_putana == mafia_sherif:
					mafia_sherif =""
					mafia_putana = ""
				if mafia_role.count('мафия') >= len(mafia_role)- mafia_role.count('мафия'):
					#await jg.send('Мафия выиграла!')
					emb = discord.Embed(title ="Мафия выиграла!" , color = 0xe74c3c)
					emb.add_field(name = "Мафией был: ", value = mafia_gamer[mafia_role.index("мафия")])
					emb.set_thumbnail(url="https://imgtest.mir24.tv/uploaded/images/crops/2017/September/870x489_0x244_detail_crop_ec6c59acb9fff1edae8eb73d4159301f.jpg")
					await jg.send(embed = emb)
					mafia_game = False
					list_gamer = []
					mafia_role = []
					mafia_gamer = []
				else:
					#await jg.send("Убито: "+ mafia_kill[0] + "  Его роль была: "+ money[5][money[0].index(mafia_kill[0])])
					mafia_role.remove(money[5][money[0].index(mafia_kill[0])])
					mafia_gamer.remove(mafia_kill[0])
					emb = discord.Embed(title = "Сегодня ночью было убито " + mafia_kill[0] , color = 0xe74c3c)
					emb.add_field(name = "Его роль:", value = money[5][money[0].index(mafia_kill[0])])
					emb.set_thumbnail(url=money[6][money[0].index(mafia_kill[0])].avatar_url)
					await jg.send(embed = emb)


					if mafia_sherif != "":
						await jg.send("Раскрыто мафию: " + mafia_sherif)
						mafia_role.remove("мафия")
						mafia_gamer.remove(mafia_sherif)
						mafia_sherif =""
					if mafia_role.count("мафия") == 0 and len(mafia_role) != 0:
							#await jg.send("Победа мирных!")
							emb = discord.Embed(title ="Победа мирных!" , color = 0xe74c3c)
							emb.add_field(name = "Живые игроки: ", value = mafia_gamer)
							emb.set_thumbnail(url="https://cs8.pikabu.ru/post_img/big/2017/12/06/4/1512538652128363705.jpg")
							await jg.send(embed = emb)
							mafia_game = False
							list_gamer = []
							mafia_role = []
							mafia_gamer = []


	if mafia_start == True:
		if message.channel != jg and mgg == "+" and message.author.name.lower() in list_gamer and not message.author.name.lower() in mafia_gamer:
			mafia_gamer.append(message.author.name.lower())
			await jg.send(message.author.name + " Готов!  " + str(len(mafia_gamer)) + " | " + str(len(list_gamer)) )
			await save_msg.delete()
			emb = discord.Embed(title = "Все готовы?! + мне в личку", color = 0xe74c3c)
			emb.add_field(name = "Игроки готовы:", value = str(len(mafia_gamer)) + " | " + str(len(list_gamer)))
			emb.set_thumbnail(url="https://www.epicwar.com/assets/p/1106/276465.jpg")
			save = True
			await jg.send(embed = emb)
			a = 0
			a = random.randint(0, len(mafia_role)-1)
			print(a)
			print(len(mafia_role))
			print(mafia_role[a])
			money[5][money[0].index(message.author.name.lower())] = mafia_role[a]
			del mafia_role[a]
			await message.channel.send("Ваша роль:  "+money[5][money[0].index(message.author.name.lower())])
			if len(mafia_role) == 0:
				mafia_game = True
				mafia_start = False
				await jg.send("Игра начата!")
				mafia_night = 1
				await save_msg.delete()
				emb = discord.Embed(title = str(mafia_night) + " ночь. Город засыпает..." , color = 0xe74c3c)
				emb.add_field(name = "Живые игроки:", value = mafia_gamer)
				emb.set_thumbnail(url="https://moika78.ru/news2/2019/02/1111-246.jpg")
				save = True
				await message.channel.send(embed = emb)
				await jg.send("Просыпается мафия... И делает свой выбор... (напиши имя жертвы в ЛИЧКУ боту)")
				mafia_hod = "мафия"
				mafia_role = mafia_role2

	if mafia == True:
		if mgg == "!роли":
			await jg.send(mafia_role)
		if mgg == "!?роли":
			await jg.send(mafia_roles)
		if mgg.startswith("!+роль"):
			h = mgg.split(" ")
			del h[0]
			for d in range(len(h)):
				if h[d] in mafia_roles:
					if message.author.name.lower() == list_gamer[0]:
						mafia_role.append(h[d])
						mafia_role2.append(h[d])
			await save_msg.delete()
			emb = discord.Embed(title = "Лобби. Создатель: " + list_gamer[0], color = 0xe74c3c)
			emb.add_field(name = "Игроки:", value = list_gamer)
			emb.add_field(name = "Роли в игре:", value= mafia_role)
			emb.set_thumbnail(url="https://www.epicwar.com/assets/p/1106/276465.jpg")
			save = True
			await message.channel.send(embed = emb)
		if mgg == "!старт" and list_gamer[0] == message.author.name.lower() :
			if len(list_gamer) >= 1 and len(list_gamer) == len(mafia_role):
				mafia_start = True
				mafia = False
				#await jg.send("Игра началась! Проверим, все ли на месте. Напишите в ЛИЧКУ боту + , и он выдаст вам вашу роль.")
				await save_msg.delete()
				emb = discord.Embed(title = "Все готовы?! + мне в личку", color = 0xe74c3c)
				emb.add_field(name = "Игроки готовы:", value = "0 | " + str(len(list_gamer)))
				emb.set_thumbnail(url="https://www.epicwar.com/assets/p/1106/276465.jpg")
				save = True
				await message.channel.send(embed = emb)
			else:
				await jg.send("Недостаточно игроков или ролей для них! Требуется, как минимум 5 игроков!")
		if mgg == "+" and not message.author.name.lower() in list_gamer:
			if not message.author.name.lower() in money[0]:
				money[0].append(message.author.name.lower())
				money[1].append(100)   # gold
				money[4].append("нету класса")
				money[2].append(0)   # lvl
				money[3].append(-1)   # Exp
				money[5].append("role")
				money[6].append(message.author) #user
			list_gamer.append(message.author.name.lower())
			if len(list_gamer) < 5:
				await message.channel.send(message.author.name+" присоединился к игре! Для старта необходимо ещё " + str(5-len(list_gamer)) + " игроков.")
			if len(list_gamer) >= 5:
				await message.channel.send(message.author.name + " присоединился к игре! Для старта нужно написать в чат !СТАРТ игроку, который запустил игру.")
			await message.delete()
			await save_msg.delete()
			emb = discord.Embed(title = "Лобби. Создатель: " + list_gamer[0], color = 0xe74c3c)
			emb.add_field(name = "Игроки:", value = list_gamer)
			emb.add_field(name = "Роли в игре:", value= mafia_role)
			emb.set_thumbnail(url="https://www.epicwar.com/assets/p/1106/276465.jpg")
			save = True
			await message.channel.send(embed = emb)
	if mgg == "!мафия":
		mafia = True
		jg = message.channel
		list_gamer = []
		if message.author.name.lower() in money[0]:
			print(123)

		else:
			money[0].append(message.author.name.lower())
			money[1].append(100)   # gold
			money[4].append("нету класса")
			money[2].append(0)   # lvl
			money[3].append(-1)   # Exp
			money[5].append("role") #role
			money[6].append(message.author) #user
		list_gamer.append(message.author.name.lower())
		emb = discord.Embed(title="пользователь " + message.author.name + " запустил игру 'Мафия'", color = 0xc27c0e)
		emb.add_field(name="Команды:", value = "Для добавления ролей используйте команду !+роль <название роли>. Для того, чтобы узнать какие роли добавлены используйте !роли. Какие вообще есть роли для добавления, пишите !?роли.")
		emb.add_field(name="Что нужно для игры: ", value = "Для игры необходимо, как минимум, 5 игроков. Ставьте + в чат, кто будет играть.")
		emb.set_thumbnail(url="https://www.epicwar.com/assets/p/1106/276465.jpg")
		#await message.channel.send("Пользователь " + message.author.name + " запустил игру МАФИЯ." + '\n Для добавления ролей используйте команду !+роль <название роли>.')
		#await message.channel.send(" Для того, чтобы узнать какие роли добавлены используйте !роли. Какие вообще есть роли для добавления, пишите !?роли. Для игры необходимо, как минимум, 5 игроков. Ставьте + в чат, кто будет играть.")
		await message.channel.send(embed = emb)
		emb = discord.Embed(title = "Лобби. Создатель: " + list_gamer[0], color = 0xe74c3c)
		emb.add_field(name = "Игроки:", value = list_gamer)
		emb.add_field(name = "Роли в игре:", value= mafia_role)
		emb.set_thumbnail(url="https://www.epicwar.com/assets/p/1106/276465.jpg")
		save = True
		await message.channel.send(embed = emb)
	if mgg == "паспорт":
		kk = ""
		if message.author.name.lower() in money[0]:
			print(123)

		else:
			money[0].append(message.author.name.lower())
			money[1].append(100)   # gold
			money[4].append("нету класса")
			money[2].append(0)   # lvl
			money[3].append(-1)   # Exp
			money[5].append("role")
			money[6].append(message.author) #user
		emb = discord.Embed(title="Name: " + message.author.name, color = 0xc27c0e)
		emb.add_field(name="Level: " + str(money[2][money[0].index(message.author.name.lower())]), value='Exp: ' + str(money[3][money[0].index(message.author.name.lower())]) + " / " + str(money[2][money[0].index(message.author.name.lower())]*10))
		emb.add_field(name="Баланс:", value=str(money[1][money[0].index(message.author.name.lower())]) +"$")
		emb.set_thumbnail(url=money[6][money[0].index(message.author.name.lower())].avatar_url)
		await message.channel.send(embed = emb)
		kk += '\n Name: ' + message.author.name
		kk += '\n Class: ' + money[4][money[0].index(message.author.name.lower())]
		kk += '\n Level: ' + str(money[2][money[0].index(message.author.name.lower())])
		kk += '\n Exp: ' + str(money[3][money[0].index(message.author.name.lower())]) + " / " + str(money[2][money[0].index(message.author.name.lower())]*10)
		#await message.channel.send(kk)
	if mgg == "заработать":
		
		if message.author.name.lower() in money[0]:
			print(123)

		else:
			money[0].append(message.author.name.lower())
			money[1].append(100)
		money[1][money[0].index(message.author.name.lower())] += 1
		await message.delete()
	if mgg == "hello":
		await message.add_reaction('😀')
		await message.channel.send("Хеллоу енглишмэн!")
	if mgg == "!дебаг":
		await message.channel.send("mas Money[0]")
		await message.channel.send(money[0])
		await message.channel.send("mas Money[1]")
		await message.channel.send(money[1])
		await message.channel.send("mas music_list[]")
		await message.channel.send(music_list)
		await message.channel.send("mas money 5")
		await message.channel.send(money[5])
	if mgg == "привет":
		await message.channel.send("Привет!")
	if mgg == "привіт":
		await message.channel.send("Здоровенькі були! Слава Україні!")
	if mgg == "!баланс":
		if message.author.name.lower() in money[0]:
			print(123)

		else:
			money[0].append(message.author.name.lower())
			money[1].append(100)
		await message.channel.send("Баланс " + message.author.name + ": "+ str(money[1][money[0].index(message.author.name.lower())]) + "$" )
	if mgg.startswith("!передать"):
		msg = message.content.split(" ")
		if msg[1] in money[0]:
			if money[1][money[0].index(message.author.name.lower())] >= int(msg[2]):
				money[1][money[0].index(message.author.name.lower())] -= int(msg[2])
				money[1][money[0].index(msg[1])] += int(msg[2])
				await message.channel.send("Пользователю " + msg[1] + " передано " + msg[2] + "$") 
		else:
			await message.channel.send("Такого пользователя в системе нету!")
	if mgg == "!апгрейд":
		l = str(message.author.roles).split("'")
		if l[3] in rol[0]:
			await Bot.add_role(message.author, rol[0][rol[0].index(l[3])+1])
			
		elif l[3] in rol[1]:
			print(message.author.roles)



Bot.run(os.environ.get("Bot_Token"))
#Bot.run("NjQ1MjM2OTk5MDQwNTMyNTAw.XiBEKg.0bz4aMfUwzQgLhpUygjx-hu38ag")
