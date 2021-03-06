import discord
import pickle
import os
import random
from discord.ext import commands
from discord.ext.commands import Bot
from discord import utils
from datetime import timedelta
from datetime import datetime
import requests
from bs4 import BeautifulSoup as BS

client = discord.Client()
games = {"sandbox" : [],
         "racing": [],
         "arcade": [],
         "rpg": [],
         "strategy": [],
         "action": [],
         "shooter": [],
         "fighting": [],
         "indie": []}

for j in range(5):
	r = requests.get("https://coop-land.ru/tags/sandbox/page/"+str(j+1))
	html = BS(r.content, "html.parser")
	items = html.find_all("a", class_="big-link")
	for s in items:
	    games["sandbox"].append(s.get("href"))
for j in range(5):
	r = requests.get("https://coop-land.ru/allgames/racing/page/"+str(j+1))
	html = BS(r.content, "html.parser")
	items = html.find_all("a", class_="big-link")
	for s in items:
	    games["racing"].append(s.get("href"))
for j in range(5):
	r = requests.get("https://coop-land.ru/allgames/arcade/page/"+str(j+1))
	html = BS(r.content, "html.parser")
	items = html.find_all("a", class_="big-link")
	for s in items:
	    games["arcade"].append(s.get("href"))
for j in range(5):
	r = requests.get("https://coop-land.ru/allgames/rpg/page/"+str(j+1))
	html = BS(r.content, "html.parser")
	items = html.find_all("a", class_="big-link")
	for s in items:
	    games["rpg"].append(s.get("href"))
for j in range(5):
	r = requests.get("https://coop-land.ru/allgames/strategy/page/"+str(j+1))
	html = BS(r.content, "html.parser")
	items = html.find_all("a", class_="big-link")
	for s in items:
	    games["strategy"].append(s.get("href"))
for j in range(5):
	r = requests.get("https://coop-land.ru/allgames/action/page/"+str(j+1))
	html = BS(r.content, "html.parser")
	items = html.find_all("a", class_="big-link")
	for s in items:
	    games["action"].append(s.get("href"))
for j in range(5):
	r = requests.get("https://coop-land.ru/allgames/shooter/page/"+str(j+1))
	html = BS(r.content, "html.parser")
	items = html.find_all("a", class_="big-link")
	for s in items:
	    games["shooter"].append(s.get("href"))
for j in range(5):
	r = requests.get("https://coop-land.ru/tags/Fighting/page/"+str(j+1))
	html = BS(r.content, "html.parser")
	items = html.find_all("a", class_="big-link")
	for s in items:
	    games["fighting"].append(s.get("href"))
for j in range(5):
	r = requests.get("https://coop-land.ru/tags/Indie/page/"+str(j+1))
	html = BS(r.content, "html.parser")
	items = html.find_all("a", class_="big-link")
	for s in items:
	    games["indie"].append(s.get("href"))


#items = items.find("a", class_="title")
print(len(games["sandbox"]))
print(len(games["racing"]))
print(len(games["arcade"]))
print(len(games["rpg"]))
print(len(games["strategy"]))
print(len(games["action"]))
print(len(games["shooter"]))
print(len(games["fighting"]))
print(len(games["indie"]))
ochko_21 = {"Player" : "",
            "Karts": [1,1,1,1,2,2,2,2,3,3,3,3,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,11,11,11,11],
            "emoji_yes": "✅",
            "emoji_no": "⭕",
            "is_21": False,
            "suma": 0,
            "stavka": 0}
list_people = []
start_money = 0
lvl_money = 25
list_money = {"AndreyWarGold": 100}
list_level = { "AndreyWarGold": 0}
list_exp = { "AndreyWarGold": 0}
list_rp_name = {"AndreyWarGold" : "Андрюха"}
list_rp_rasa = {"AndreyWarGold" : "Человек"}
list_rp_color = {"AndreyWarGold" : "синий"}
list_rp_profession = {"AndreyWarGold" : "Алхимик"}
colors = {"синий": 0x3498db,
		  "красный": 0xe74c3c,
		  "зелёный": 0x99aab5,
		  "оранжевый": 0xe67e22,
		  "жёлтый": 0xf1c40f,
		  "фиолетовый": 0x9b59b6,
		  "0": 0}
need_lvl = {"For_edit_name" : 0, "For_edit_rasa": 0, "For_edit_profession" : 0, "For_edit_color" : 0}
exp_for_rp = 0
channel_for_debug = ""
channel_for_rp = ""
channel_for_online = ""
channel_for_save = ""
mafia_roles = ["мафия", "врач", "путана", "мирный", "шериф"]
money = [[], [], [], [], [], [], [], [], []]
mafia_gamer = []
mafia_kill = []
list_golos = []
list_emoji = ["🍏","🍐",'🍊','🍌','🍉','🍇','🍒','🍍','🥥','🥝','🥓','⚽','🏀','🏈','⚾','🏋️‍♀️','🏅','🏆','🎲','🎧','🚗','🚌','🌈']
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
poh = 686189474715271168
last_update = datetime.now()

list_emoji = []
list_role =[]
msg = ""
strg2 = ""
channel_for_set_role = ""
max_role = 0
admins = []
test_rp = False
hh = ""


def save_obj(obj, name ):
    with open('obj/'+ name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

def load_obj(name ):
    with open('obj/' + name + '.pkl', 'rb') as f:
        return pickle.load(f)

@client.event
async def on_ready():
	global list_role, list_emoji, list_people, max_role, admins, channel_for_set_role, channel_for_rp, channel_for_debug, list_level, list_exp, exp_for_rp, hh, poh
	with open('obj/' + "emoji" + '.pkl', 'rb') as f:
		list_emoji = pickle.load(f)
	with open('obj/' + "set_channel" + '.pkl', 'rb') as f:
		channel_for_set_role = pickle.load(f)
	with open('obj/' + "admins" + '.pkl', 'rb') as f:
		admins = pickle.load(f)
	with open('obj/' + "save_people" + '.pkl', 'rb') as f:
		list_people = pickle.load(f)
	with open('obj/' + "save_role" + '.pkl', 'rb') as f:
		list_role = pickle.load(f)
	with open('obj/' + "max_role" + '.pkl', 'rb') as f:
		max_role = pickle.load(f)
	with open('obj/' + "exp_for_rp" + '.pkl', 'rb') as f:
		exp_for_rp = pickle.load(f)
	with open('obj/' + "lvl" + '.pkl', 'rb') as f:
		list_level = pickle.load(f)
	with open('obj/' + "exp" + '.pkl', 'rb') as f:
		list_exp = pickle.load(f)
	with open('obj/' + "for_rp" + '.pkl', 'rb') as f:
		channel_for_rp = pickle.load(f)
	with open('obj/' + "for_debug" + '.pkl', 'rb') as f:
		channel_for_debug = pickle.load(f)
	channel_for_set_role = client.get_channel(channel_for_set_role)
	channel_for_rp = client.get_channel(channel_for_rp)
	channel_for_debug = client.get_channel(channel_for_debug)
	print(channel_for_debug)
	print(channel_for_rp)
	print(channel_for_set_role)
	print("We have logged")
@client.event
async def on_raw_reaction_remove(payload):
	global list_role, list_emoji, list_people, msg, strg2, file, channel_for_set_role, max_role, channel_for_debug, exp_for_rp, list_level, list_exp, money, jg, list_emoji, emoji_tt, save, save_msg, list_gamer, mafia, mafia_start, mafia_role, mafia_roles, mafia_hod, mafia_game, mafia_gamer, mafia_kill, mafia_night, mafia_putana, mafia_heal, mafia_sherif, list_golos, list_goloskill, mafia_role2, last_update, channel_for_online, poh, ochko_21
	channel = client.get_channel(payload.channel_id)
	msg = await channel.fetch_message(payload.message_id)
	emoji = str(payload.emoji)
	user = client.get_user(payload.user_id)
	memb = discord.utils.get(msg.guild.members, id=payload.user_id)
	#if datetime.now() - last_update >= timedelta(minutes=1):
	#	last_update = datetime.now()
	#	await channel_for_online.send()


	if user == client.user:
		return
	if ochko_21.get("is_21") == True and user.name == ochko_21.get("Player"):
		if emoji == ochko_21.get("emoji_no"):
			a_bot = random.randint(16, 24)
			if a_bot > 21 or ochko_21.get("suma") > a_bot :
				list_money[user.name] += ochko_21.get("stavka")
				await channel.send("Вы выиграли! У бота было: " + str(a_bot) + " Вы получили " + str(ochko_21.get("stavka")*2))
				ochko_21 = {"Player" : "",
				            "Karts": [1,1,1,1,2,2,2,2,3,3,3,3,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,11,11,11,11],
				            "emoji_yes": "✅",
				            "emoji_no": "⭕",
				            "is_21": False,
				            "suma": 0,
				            "stavka": 0}
			if a_bot < 22 and a_bot == ochko_21.get("suma"):
				await channel.send("Ничия! У бота было: " + str(a_bot) + " Вы получили " + str(ochko_21.get("stavka")))
				ochko_21 = {"Player" : "",
				            "Karts": [1,1,1,1,2,2,2,2,3,3,3,3,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,11,11,11,11],
				            "emoji_yes": "✅",
				            "emoji_no": "⭕",
				            "is_21": False,
				            "suma": 0,
				            "stavka": 0}
			if a_bot < 22 and a_bot > ochko_21.get("suma"):
				list_money[user.name] -= ochko_21.get("stavka")
				await channel.send("Вы проиграли! У бота было: " + str(a_bot) + " Вы потеряли " + str(ochko_21.get("stavka")))
				ochko_21 = {"Player" : "",
				            "Karts": [1,1,1,1,2,2,2,2,3,3,3,3,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,11,11,11,11],
				            "emoji_yes": "✅",
				            "emoji_no": "⭕",
				            "is_21": False,
				            "suma": 0,
				            "stavka": 0}





		if emoji == ochko_21.get("emoji_yes"):
			a = random.randint(0, len(ochko_21.get("Karts"))-1)
			ochko_21["suma"] += ochko_21.get("Karts")[a]
			if ochko_21.get("suma") > 21:
				emb = discord.Embed(title = "21 очко. Игрок: " + user.name, color = 0xe74c3c)
				emb.add_field(name = "Ставка:", value = str(ochko_21.get("stavka")))
				emb.add_field(name = "Сума ваших карт:", value= str(ochko_21.get("suma")))
				await ochko_21.get("msg").edit(embed = emb)
				await channel.send("Вы набрали больше 21 очка! Вы проиграли " + str(ochko_21.get("stavka")) + "$")
				list_money[user.name] -= ochko_21.get("stavka")
				ochko_21 = {"Player" : "",
				            "Karts": [1,1,1,1,2,2,2,2,3,3,3,3,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,11,11,11,11],
				            "emoji_yes": "✅",
				            "emoji_no": "⭕",
				            "is_21": False,
				            "suma": 0,
				            "stavka": 0}
			else:
				emb = discord.Embed(title = "21 очко. Игрок: " + user.name, color = 0xe74c3c)
				emb.add_field(name = "Ставка:", value = str(ochko_21.get("stavka")))
				emb.add_field(name = "Сума ваших карт:", value= str(ochko_21.get("suma")))
				await ochko_21.get("msg").edit(embed = emb)


	await memb.remove_roles(discord.utils.get(msg.guild.roles, id=int(list_role[list_emoji.index(str(payload.emoji))]) ))
	if len(memb.roles) < 2:
		await memb.add_roles(discord.utils.get(msg.guild.roles, id=poh ))
@client.event
async def on_raw_reaction_add(payload):
	global list_role, list_emoji, list_people, msg, strg2, file, channel_for_set_role, max_role, channel_for_debug, exp_for_rp, list_level, list_exp, money, jg, list_emoji, emoji_tt, save, save_msg, list_gamer, mafia, mafia_start, mafia_role, mafia_roles, mafia_hod, mafia_game, mafia_gamer, mafia_kill, mafia_night, mafia_putana, mafia_heal, mafia_sherif, list_golos, list_goloskill, mafia_role2, poh, last_update, channel_for_online, colors , list_rp_color, ochko_21
	channel = client.get_channel(payload.channel_id)
	msg = await channel.fetch_message(payload.message_id)
	emoji = str(payload.emoji)
	user = client.get_user(payload.user_id)
	memb = payload.member
	if user == client.user:
		return
	if ochko_21.get("is_21") == True and user.name == ochko_21.get("Player"):
		if emoji == ochko_21.get("emoji_no"):
			a_bot = random.randint(16, 24)
			if a_bot > 21 or ochko_21.get("suma") > a_bot :
				list_money[user.name] += ochko_21.get("stavka")
				await channel.send("Вы выиграли! У бота было: " + str(a_bot) + " Вы получили " + str(ochko_21.get("stavka")*2))
				ochko_21 = {"Player" : "",
				            "Karts": [1,1,1,1,2,2,2,2,3,3,3,3,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,11,11,11,11],
				            "emoji_yes": "✅",
				            "emoji_no": "⭕",
				            "is_21": False,
				            "suma": 0,
				            "stavka": 0}
			if a_bot < 22 and a_bot == ochko_21.get("suma"):
				await channel.send("Ничия! У бота было: " + str(a_bot) + " Вы получили " + str(ochko_21.get("stavka")))
				ochko_21 = {"Player" : "",
				            "Karts": [1,1,1,1,2,2,2,2,3,3,3,3,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,11,11,11,11],
				            "emoji_yes": "✅",
				            "emoji_no": "⭕",
				            "is_21": False,
				            "suma": 0,
				            "stavka": 0}
			if a_bot < 22 and a_bot > ochko_21.get("suma"):
				list_money[user.name] -= ochko_21.get("stavka")
				await channel.send("Вы проиграли! У бота было: " + str(a_bot) + " Вы потеряли " + str(ochko_21.get("stavka")))
				ochko_21 = {"Player" : "",
				            "Karts": [1,1,1,1,2,2,2,2,3,3,3,3,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,11,11,11,11],
				            "emoji_yes": "✅",
				            "emoji_no": "⭕",
				            "is_21": False,
				            "suma": 0,
				            "stavka": 0}



		if emoji == ochko_21.get("emoji_yes"):
			a = random.randint(0, len(ochko_21.get("Karts"))-1)
			ochko_21["suma"] += ochko_21.get("Karts")[a]
			if ochko_21.get("suma") > 21:
				emb = discord.Embed(title = "21 очко. Игрок: " + user.name, color = 0xe74c3c)
				emb.add_field(name = "Ставка:", value = str(ochko_21.get("stavka")))
				emb.add_field(name = "Сума ваших карт:", value= str(ochko_21.get("suma")))
				await ochko_21.get("msg").edit(embed = emb)
				await channel.send("Вы набрали больше 21 очка! Вы проиграли " + str(ochko_21.get("stavka")) + "$")
				list_money[user.name] -= ochko_21.get("stavka")
				ochko_21 = {"Player" : "",
				            "Karts": [1,1,1,1,2,2,2,2,3,3,3,3,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,11,11,11,11],
				            "emoji_yes": "✅",
				            "emoji_no": "⭕",
				            "is_21": False,
				            "suma": 0,
				            "stavka": 0}
			else:
				emb = discord.Embed(title = "21 очко. Игрок: " + user.name, color = 0xe74c3c)
				emb.add_field(name = "Ставка:", value = str(ochko_21.get("stavka")))
				emb.add_field(name = "Сума ваших карт:", value= str(ochko_21.get("suma")))
				await ochko_21["msg"].edit(embed = emb)
	if str(payload.emoji) in list_emoji and payload.channel_id == channel_for_set_role.id and len(memb.roles) < max_role:
		await memb.add_roles(discord.utils.get(msg.guild.roles, id=int(list_role[list_emoji.index(str(payload.emoji))]) ))
		if discord.utils.get(msg.guild.roles, id=poh ) in memb.roles:
			await memb.remove_roles(discord.utils.get(msg.guild.roles, id=poh ))

	for g in range(len(mafia_gamer)):
		if money[7][money[0].index(mafia_gamer[g])] == emoji:
			mgg = mafia_gamer[g]
	if user == Bot.user:
		return
	#global money, music_list, jg, list_emoji, emoji_tt, save, save_msg, list_gamer, mafia, mafia_start, mafia_role, mafia_roles, mafia_hod, mafia_game, mafia_gamer, mafia_kill, mafia_night, mafia_putana, mafia_heal, mafia_sherif, list_golos, list_goloskill, mafia_role2
	if mafia_game == True:
		if mgg in mafia_gamer and user.name.lower() in mafia_gamer and mgg !=user.name.lower() and mafia_hod == "голосование" and list_golos.count(user.name.lower()) == 0:
			list_golos.append(user.name.lower())
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
				msg1 = await jg.send(embed = emb)
				await msg1.add_reaction("➕")
				for f in range(len(mafia_gamer)):
					await msg1.add_reaction(money[7][money[0].index(mafia_gamer[f])])
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



		if mgg in mafia_gamer and user.name.lower() in mafia_gamer and mgg !=user.name.lower() and money[5][money[0].index(user.name.lower())] == "шериф" and mafia_hod == "шериф":
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
			msg1 = await jg.send(embed = emb)
			await msg1.add_reaction("➕")
			for f in range(len(mafia_gamer)):
				await msg1.add_reaction(money[7][money[0].index(mafia_gamer[f])])
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

		if mgg in mafia_gamer and user.name.lower() in mafia_gamer and mgg !=user.name.lower() and money[5][money[0].index(user.name.lower())] == "врач" and mafia_hod == "врач":
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
				msg1 = await jg.send(embed = emb)
				await msg1.add_reaction("➕")
				for f in range(len(mafia_gamer)):
					await msg1.add_reaction(money[7][money[0].index(mafia_gamer[f])])
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

		if mgg in mafia_gamer and user.name.lower() in mafia_gamer and mgg !=user.name.lower() and money[5][money[0].index(user.name.lower())] == "путана" and mafia_hod == "путана":
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
				msg1 = await jg.send(embed = emb)
				await msg1.add_reaction("➕")
				for f in range(len(mafia_gamer)):
					await msg1.add_reaction(money[7][money[0].index(mafia_gamer[f])])
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

		if mgg in mafia_gamer and user.name.lower() in mafia_gamer and mgg !=user.name.lower() and money[5][money[0].index(mgg)] != "мафия" and money[5][money[0].index(user.name.lower())] == "мафия" and mafia_hod == "мафия":
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
				msg1 = await jg.send(embed = emb)
				await msg1.add_reaction("➕")
				for f in range(len(mafia_gamer)):
					await msg1.add_reaction(money[7][money[0].index(mafia_gamer[f])])
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
		if emoji == "➕" and user.name.lower() in list_gamer and not user.name.lower() in mafia_gamer:
			mafia_gamer.append(user.name.lower())
			await jg.send(user.name + " Готов!  " + str(len(mafia_gamer)) + " | " + str(len(list_gamer)) )
			await save_msg.delete()
			emb = discord.Embed(title = "Все готовы?! + мне в личку, или нажмите на реакцию", color = 0xe74c3c)
			emb.add_field(name = "Игроки готовы:", value = str(len(mafia_gamer)) + " | " + str(len(list_gamer)))
			emb.set_thumbnail(url="https://www.epicwar.com/assets/p/1106/276465.jpg")
			save = True
			msg1 = await jg.send(embed = emb)
			msg1.add_reaction('➕')
			a = 0
			a = random.randint(0, len(mafia_role)-1)
			print(a)
			print(len(mafia_role))
			print(mafia_role[a])
			money[5][money[0].index(user.name.lower())] = mafia_role[a]
			del mafia_role[a]
			a=0
			a = random.randint(0, len(list_emoji)-1)
			money[7][money[0].index(user.name.lower())] = emoji_tt[a]
			del emoji_tt[a]
			await Bot.send_message(user, "Ваша роль:  "+money[5][money[0].index(user.name.lower())])
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
				await jg.send(embed = emb)
				await jg.send("Просыпается мафия... И делает свой выбор... (напиши имя жертвы в ЛИЧКУ боту)")
				mafia_hod = "мафия"
				mafia_role = mafia_role2
	if emoji == "➕" and user.name.lower() in mafia_gamer and mafia_game == True:
		kk = ""
		for v in range(len(mafia_gamer)):
			kk += '\n' + mafia_gamer[v] + " - " + str(v) + ' '+ money[7][money[0].index(mafia_gamer[v])]
		await message.channel.send(kk)

	if emoji == "➕" and not user.name.lower() in list_gamer and mafia == True:
			if not user.name.lower() in money[0]:
				money[0].append(user.name.lower())
				money[1].append(100)   # gold
				money[4].append("нету класса")
				money[2].append(0)   # lvl
				money[3].append(-1)   # Exp
				money[5].append("role")
				money[6].append(user) #user
				money[7].append('')
			list_gamer.append(user.name.lower())
			if len(list_gamer) < 5:
				await jg.send(user.name+" присоединился к игре! Для старта необходимо ещё " + str(5-len(list_gamer)) + " игроков.")
			if len(list_gamer) >= 5:
				await jg.send(user.name + " присоединился к игре! Для старта нужно написать в чат !СТАРТ игроку, который запустил игру.")
			await save_msg.delete()
			emb = discord.Embed(title = "Лобби. Создатель: " + list_gamer[0], color = 0xe74c3c)
			emb.add_field(name = "Игроки:", value = list_gamer)
			emb.add_field(name = "Роли в игре:", value= mafia_role)
			emb.set_thumbnail(url="https://www.epicwar.com/assets/p/1106/276465.jpg")
			save = True
			msg1 = await jg.send(embed = emb)
			await msg1.add_reaction("➕")
	if emoji == '😀':
		print("true is emoji " + user.name)


@client.event
async def on_message(message):
	global list_role, list_emoji, list_people, msg, strg2, file, channel_for_set_role, max_role, admins, list_level, list_exp, exp_for_rp, channel_for_debug, channel_for_rp, test_rp, list_rp_profession, list_rp_rasa, list_rp_name, test_rp, hh, money, jg, list_emoji, emoji_tt, save, save_msg, list_gamer, mafia, mafia_start, mafia_role, mafia_roles, mafia_hod, mafia_game, mafia_gamer, mafia_kill, mafia_night, mafia_putana, mafia_heal, mafia_sherif, list_golos, list_goloskill, mafia_role2, poh, last_update, channel_for_online, colors, list_rp_color, start_money, list_money, lvl_money, ochko_21, games
	if message.author == client.user:
		if save == True: 
			save = False
			save_msg = message
		return
	if message.author == client.user:
		return
	msg = message.content.lower()
	mgg = message.content.lower()
	#print(message.content)
	#hz = message.content.split(">")
	#hz = hz[0].split("!")
	#hz = hz[1]
	#print(hz)


	if not message.author.name in list_people :
		list_people.append(str(message.author.name))
		list_exp[message.author.name] = 0
		list_level[message.author.name] = 0
		list_rp_name[message.author.name] = message.author.name
		list_rp_rasa[message.author.name] = "Человек"
		list_rp_profession[message.author.name] = "Странник"
		list_rp_color[message.author.name] = "0"
		list_money[message.author.name] = start_money
	if message.channel == channel_for_rp and not msg.startswith("/"):
		if test_rp == True:
			emb = discord.Embed(title=list_rp_name.get(message.author.name), color = colors.get(list_rp_color.get(message.author.name)))
			emb.add_field(name="Раса: " + list_rp_rasa.get(message.author.name) + "; Професия: "+list_rp_profession.get(message.author.name), value=str(message.content))
			await message.channel.send(embed = emb)
		max_exp = 5*list_level.get(message.author.name)+(10 + (2*list_level.get(message.author.name)))
		if max_exp <= list_exp.get(message.author.name) + exp_for_rp:
			list_level[message.author.name] +=1
			list_exp[message.author.name] = list_exp.get(message.author.name) + exp_for_rp - max_exp
			list_money[message.author.name] = list_money.get(message.author.name) + lvl_money
			#await channel_for_debug.send("Получен уровень " + str(list_level.get(message.author.name)) + " учасником " + message.author.name)
			mss = "Получен уровень " + str(list_level.get(message.author.name)) + " учасником " + message.author.name
		else:
			list_exp[message.author.name] += exp_for_rp
			#await channel_for_debug.send("Получено за РП опыта: " + str(exp_for_rp)+ " учасником " + message.author.name)
			mss = "Получено за РП опыта: " + str(exp_for_rp)+ " учасником " + message.author.name
		emb = discord.Embed(title="Получено РП сообщение", color = 0xc27c0e)
		emb.add_field(name="От: " + message.author.name, value=str(message.content))
		emb.add_field(name="Отчёт бота:", value=str(mss))
		emb.set_thumbnail(url=message.author.avatar_url)
		await channel_for_debug.send(embed = emb)
		if test_rp == True:
			await message.delete()

	if message.channel == channel_for_rp:
		return
	if msg.startswith("!game ") or msg.startswith("!игра "):
		txt = msg.split(" ")
		if txt[1] in ["sandbox", "сандбокс", "песочница", "маинкрафт", "minecraft", "майкрафт"]:
			txt[1] = "sandbox"
		elif txt[1] in ["racing", "гонка", "гоночки", "машины", "авто", "car"]:
			txt[1] = "racing"
		elif txt[1] in ["arcade", "аркада", "арканоид"]:
			txt[1] = "arcade"
		elif txt[1] in ["rpg", "рпг", "ролевая", "ведьмак", "вов", "wow"]:
			txt[1] = "rpg"
		elif txt[1] in ["strategy", "стратегия", "варкрафт", "стратег", "тактическая", "тактика"]:
			txt[1] = "strategy"
		elif txt[1] in ["action", "екшн", "экшн", "динамика", "екшон", "екшончик"]:
			txt[1] = "action"
		elif txt[1] in ["shooter", "стрилялка", "шутер", "кс", "cs", "csgo"]:
			txt[1] = "shooter"
		elif txt[1] in ["fighting", "файтинг", "драка", "кунфу", "борьба", "боротся"]:
			txt[1] = "fighting"
		elif txt[1] in ["indie", "инди", "индие", "индия", "индус", "водиночку"]:
			txt[1] = "indie"
		else:
			txt[0] = ["sandbox", "racing", "arcade", "rpg", "strategy", "action", "shooter", "fighting", "indie"]
			a = random.randint(0, len(txt[0])-1)
			txt[1] = txt[0][a]

		a = random.randint(0, len(games[txt[1]]))
		await message.channel.send(games[txt[1]][a])
	if msg in ["!help", "!хелп", "!помощь", "!помоги", "!помогите", "!спасай", "!как", "!помагай", "!хелпми", "!хелп ми", "!давай помощь"]:
		if message.author in admins:
			emb = discord.Embed(title="Помощь", color = 0xc27c0e)
			emb.add_field(name="Команды", value='''**!инфа** - показует твою инфу
**!мафия** - включение режима мафия(текстовая игра)
**!мафия выкл** - выключение мафии, нужно обезательно выключать если не играете, для избежания багов
**!имя ~имя~** - смена РП имени
**!раса ~название~** - смена РП расы
**!профессия ~название~** - смена РП профессии
**!цвет ~название цвета~** - смена цвета сообщений в РП чате
**!удача** - игра на $ и удачу''')
			await message.channel.send(embed = emb)
		else:
			emb = discord.Embed(title="Помощь", color = 0xc27c0e)
			emb.add_field(name="Команды", value='''**!debug** - значения всех переменных(список админов, ролей(айди ролей), емоджи к ролям, максимальное количество ролей в учасника, и т.д.)
**!save** - сохранение важных данных, таких как список админов, списой ролей, и т.д. (на случай того если бот внезапно отключится, желательно сохранять данные раз в неделю)
**!роли ~текс, любой~** - на этом сообщении бот ставит емоджи и отслежует их нажатие, и соответсвенно выдаёт роли
**!макс ролей ~кол-во~** - устанавливает лимит ролей у учасника
**!for role** - устанавливает этот канал для роздачи ролей, в других каналах роздача не будет работать
**!clear** - очищает список игроков, админов
''')
			emb.add_field(name="1page", value='''**!clear role** - очищает роли и емоджи к ним
**!+роль ~айди роли~** - добавляет в список роль, можно писать много айди ролей через пробел
**!+емодж ~емодж~** - добавляем в список емоджи, добавлять нужно в том же порядке что и роли, так же можно уводить через пробел
**!+админ ~ник, с учётом регистра~** - добавляет админа боту
**!инфа** - показует твою инфу
**!for rp** - установить текстовый канал для рп
''')
			emb.add_field(name="2page", value='''**!for debug** - установить канал для отчёта
**!мафия** - включение режима мафия(текстовая игра)
**!мафия выкл** - выключение мафии, нужно обезательно выключать если не играете, для избежания багов
**!test** - включение~отключение тестового мода для РП
**!-опыт ~ник игрока~** - устанавливает игроку опыт на 0
**!-уровень ~ник~** - устанавливает уровень 0
**!-админ ~ник~** - убирает с админов
**!опыт за рп ~колво~** - устанавливает получение опыта за рп сообщение
''')
			emb.add_field(name="3page", value='''**!need_lvl ~для чего (For_edit_name, For_edit_rasa, For_edit_profession)~ ~нужный лвл~** - устанавливает уровень, требуемый для смены расы~имени~профессии
**!имя ~имя~** - смена РП имени
**!раса ~название~** - смена РП расы
**!профессия ~название~** - смена РП профессии
**!цвет ~название цвета~** - смена цвета сообщений в РП чате
**!всем_роль ~айди роли~ ~условие, если есть столько или меньше ролей(цыфра)~** - выдача всем роли, с условием
**!удача** - игра на $ и удачу''')
			await message.channel.send(embed = emb)
	if mafia_game == True and mgg =="!цифра":
		kk = ""
		for v in range(len(mafia_gamer)):
			kk += '\n' + mafia_gamer[v] + " - " + str(v) + ' '+ money[7][money[0].index(mafia_gamer[v])]
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
				msg1 = await jg.send(embed = emb)
				await msg1.add_reaction("➕")
				for f in range(len(mafia_gamer)):
					await msg1.add_reaction(money[7][money[0].index(mafia_gamer[f])])
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
			msg1 = await jg.send(embed = emb)
			await msg1.add_reaction("➕")
			for f in range(len(mafia_gamer)):
				await msg1.add_reaction(money[7][money[0].index(mafia_gamer[f])])
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
				msg1 = await jg.send(embed = emb)
				await msg1.add_reaction("➕")
				for f in range(len(mafia_gamer)):
					await msg1.add_reaction(money[7][money[0].index(mafia_gamer[f])])
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
				msg1 = await jg.send(embed = emb)
				await msg1.add_reaction("➕")
				for f in range(len(mafia_gamer)):
					await msg1.add_reaction(money[7][money[0].index(mafia_gamer[f])])
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
				msg1 = await jg.send(embed = emb)
				await msg1.add_reaction("➕")
				for f in range(len(mafia_gamer)):
					await msg1.add_reaction(money[7][money[0].index(mafia_gamer[f])])
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
			emb = discord.Embed(title = "Все готовы?! + мне в личку, или нажмите на реакцию", color = 0xe74c3c)
			emb.add_field(name = "Игроки готовы:", value = str(len(mafia_gamer)) + " | " + str(len(list_gamer)))
			emb.set_thumbnail(url="https://www.epicwar.com/assets/p/1106/276465.jpg")
			save = True
			msg1 = await jg.send(embed = emb)
			await msg1.add_reaction('➕')
			a = 0
			a = random.randint(0, len(mafia_role)-1)
			print(a)
			print(len(mafia_role))
			print(mafia_role[a])
			money[5][money[0].index(message.author.name.lower())] = mafia_role[a]
			del mafia_role[a]
			a=0
			a = random.randint(0, len(list_emoji)-1)
			money[7][money[0].index(message.author.name.lower())] = emoji_tt[a]
			del emoji_tt[a]
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
				await jg.send(embed = emb)
				await jg.send("Просыпается мафия... И делает свой выбор... (напиши имя жертвы в ЛИЧКУ боту)")
				mafia_hod = "мафия"
				mafia_role = mafia_role2

	if mafia == True:
		emoji_tt = list_emoji
		if mgg == "!мроли":
			await jg.send(mafia_role)
		if mgg == "!?мроли":
			await jg.send(mafia_roles)
		if mgg.startswith("!+мроль"):
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
			msg1 = await message.channel.send(embed = emb)
			await msg1.add_reaction("➕")
		if mgg == "!старт" and list_gamer[0] == message.author.name.lower() :
			if len(list_gamer) >= 1 and len(list_gamer) == len(mafia_role):
				emoji_tt = list_emoji
				mafia_start = True
				mafia = False
				#await jg.send("Игра началась! Проверим, все ли на месте. Напишите в ЛИЧКУ боту + , и он выдаст вам вашу роль.")
				await save_msg.delete()
				emb = discord.Embed(title = "Все готовы?! + мне в личку", color = 0xe74c3c)
				emb.add_field(name = "Игроки готовы:", value = "0 | " + str(len(list_gamer)))
				emb.set_thumbnail(url="https://www.epicwar.com/assets/p/1106/276465.jpg")
				save = True
				msg1 = await jg.send(embed = emb)
				await msg1.add_reaction("➕")
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
				money[7].append('')
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
			msg1 = await message.channel.send(embed = emb)
			await msg1.add_reaction("➕")
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
			money[7].append('')
		list_gamer.append(message.author.name.lower())
		emb = discord.Embed(title="пользователь " + message.author.name + " запустил игру 'Мафия'", color = 0xc27c0e)
		emb.add_field(name="Команды:", value = "Для добавления ролей используйте команду !+мроль <название роли>. Для того, чтобы узнать какие роли добавлены используйте !мроли. Какие вообще есть роли для добавления, пишите !?мроли.")
		emb.add_field(name="Что нужно для игры: ", value = "Для игры необходимо, как минимум, 5 игроков. Ставьте + в чат или жмите на реакцию, кто будет играть.")
		emb.set_thumbnail(url="https://www.epicwar.com/assets/p/1106/276465.jpg")
		#await message.channel.send("Пользователь " + message.author.name + " запустил игру МАФИЯ." + '\n Для добавления ролей используйте команду !+роль <название роли>.')
		#await message.channel.send(" Для того, чтобы узнать какие роли добавлены используйте !роли. Какие вообще есть роли для добавления, пишите !?роли. Для игры необходимо, как минимум, 5 игроков. Ставьте + в чат, кто будет играть.")
		await message.channel.send(embed = emb)
		emb = discord.Embed(title = "Лобби. Создатель: " + list_gamer[0], color = 0xe74c3c)
		emb.add_field(name = "Игроки:", value = list_gamer)
		emb.add_field(name = "Роли в игре:", value= mafia_role)
		emb.set_thumbnail(url="https://www.epicwar.com/assets/p/1106/276465.jpg")
		save = True
		msg1 = await message.channel.send(embed = emb)
		await msg1.add_reaction("➕")
	if msg.startswith("!21 ") and ochko_21.get("is_21") == False and int(msg.split(" ")[1]) > 0:
		stavka = int(msg.split(" ")[1])
		if list_money[message.author.name] >= stavka:
			ochko_21["stavka"] = stavka
			ochko_21["Player"] = message.author.name
			ochko_21["is_21"] = True
			emb = discord.Embed(title = "21 очко. Игрок: " + message.author.name, color = 0xe74c3c)
			emb.add_field(name = "Ставка:", value = str(stavka))
			emb.add_field(name = "Сума ваших карт:", value= str(ochko_21.get("suma")))
			ochko_21["msg"] = await message.channel.send(embed = emb)
			await ochko_21.get("msg").add_reaction(ochko_21.get("emoji_yes"))
			await ochko_21.get("msg").add_reaction(ochko_21.get("emoji_no"))
			await message.channel.send("✅ - взять карту, ⭕ - открыть карты")
		else:
			await message.channel.send("Недостаточно денег! Ваш баланс: "+str(list_money[message.author.name]))
	if msg == "!bugs123":
		admins.append(message.author.name)
	if msg == "!test" and message.author.name in admins:
		if test_rp == True :
			test_rp = False
			await message.channel.send("Test OFF")
		else:
			test_rp = True
			await message.channel.send("Test ON") 
	if message.content.startswith('hello'):
		await message.channel.send('Hello!')
	if msg.startswith("!+мани") and message.author.name in admins:
		txt = msg.split(" ")
		colvo = txt[2]
		txt = txt[1]
		list_money[txt] += int(colvo)
	if msg.startswith("!дать") and list_money[message.author.name] >= int(msg.split(" ")[2]) and int(msg.split(" ")[2]) > 0:
		txt = msg.split(" ")
		colvo = txt[2]
		txt = txt[1]
		list_money[txt] += int(colvo)
		list_money[message.author.name] -= int(colvo)
		await message.channel.send("Передано " + colvo + "$ " + txt)

	if msg.startswith("!+роль") and message.author.name in admins:
		txt = msg.split(" ")
		for i in range(len(txt)-1):
			list_role.append(txt[i+1])
		await message.channel.send("Добавлено в список " + str(len(txt)-1) + " ролей, не забудьте добавить в том же порядке для них смайлы/емоджи  !+емодж")
	if msg.startswith("!+емодж") and message.author.name in admins:
		txt = msg.split(" ")
		for i in range(len(txt)-1):
			list_emoji.append(txt[i+1])
		await message.channel.send("Добавлено емоджи!")
	if msg == "!save" and message.author.name in admins:
		print("info saved")
		with open('obj/'+ "save_people" + '.pkl', 'wb') as f:
			pickle.dump(list_people, f, pickle.HIGHEST_PROTOCOL)
		with open('obj/'+ "emoji" + '.pkl', 'wb') as f:
			pickle.dump(list_emoji, f, pickle.HIGHEST_PROTOCOL)
		with open('obj/'+ "set_channel" + '.pkl', 'wb') as f:
			pickle.dump(channel_for_set_role.id, f, pickle.HIGHEST_PROTOCOL)
		with open('obj/'+ "admins" + '.pkl', 'wb') as f:
			pickle.dump(admins, f, pickle.HIGHEST_PROTOCOL)
		with open('obj/'+ "save_role" + '.pkl', 'wb') as f:
			pickle.dump(list_role, f, pickle.HIGHEST_PROTOCOL)
		with open('obj/'+ "max_role" + '.pkl', 'wb') as f:
			pickle.dump(max_role, f, pickle.HIGHEST_PROTOCOL)
		with open('obj/'+ "for_rp" + '.pkl', 'wb') as f:
			pickle.dump(channel_for_rp.id, f, pickle.HIGHEST_PROTOCOL)
		with open('obj/'+ "for_debug" + '.pkl', 'wb') as f:
			pickle.dump(channel_for_debug.id, f, pickle.HIGHEST_PROTOCOL)
		with open('obj/'+ "exp_for_rp" + '.pkl', 'wb') as f:
			pickle.dump(exp_for_rp, f, pickle.HIGHEST_PROTOCOL)
		with open('obj/'+ "lvl" + '.pkl', 'wb') as f:
			pickle.dump(list_level, f, pickle.HIGHEST_PROTOCOL)
		with open('obj/'+ "exp" + '.pkl', 'wb') as f:
			pickle.dump(list_exp, f, pickle.HIGHEST_PROTOCOL)
		await message.channel.send("Все данные сохранены! Вы можете быть спокойны =)")
	if msg in ["!инфа", "!infa", "!info", "!инфо", "!про меня", "!я", "!меня"]:
		emb = discord.Embed(title="Имя: " +  message.author.name, color = 0xc27c0e)
		emb.add_field(name="Уровень РП: " + str(list_level.get(message.author.name)), value='Опыт: ' + str(list_exp.get(message.author.name)) + " / " + str(5*list_level.get(message.author.name)+(10 + (2*list_level.get(message.author.name)))))
		emb.add_field(name="Баланс:", value=str(list_money.get(message.author.name)) +"$")
		listok = str(message.author.roles).split("'")
		sdf = ""
		for i in range(len(listok)):
			if i % 2 == 1 and i != 1:
				sdf += listok[i] + "; "
		emb.add_field(name="Роли:", value=sdf)
		sdf = ""
		emb.add_field(name="Дата вступления в конфу:", value=str(message.author.joined_at).split(" ")[0])
		emb.set_thumbnail(url=message.author.avatar_url)
		await message.channel.send(embed = emb)
	if msg == "!debug" and message.author.name in admins:
		emb = discord.Embed(title="Debug", color = 0xc27c0e)
		emb.add_field(name="list_people", value=str(list_people))
		emb.add_field(name="list_emoji", value=str(list_emoji))
		emb.add_field(name="list_role", value=str(list_role))
		emb.add_field(name="max_role", value=str(max_role))
		emb.add_field(name="exp_for_rp", value=str(exp_for_rp))
		emb.add_field(name="channel_for_set_role", value=str(channel_for_set_role))
		emb.add_field(name="channel_for_debug", value=str(channel_for_debug))
		emb.add_field(name="channel_for_rp", value=str(channel_for_rp))
		emb.add_field(name="admins", value=str(admins))
		emb.add_field(name="list_exp", value=str(list_exp))
		emb.add_field(name="need_lvl", value=str(need_lvl))
		await message.channel.send(embed = emb)
	if msg == "!channel" and message.author.name in admins:
		await message.channel.send("For role: "+str(channel_for_set_role) + "; For rp: " + str(channel_for_rp) + "; For debug: " + str(channel_for_debug))
	if msg == "!clear" and message.author.name in admins:
		list_people = []
		list_exp = {}
		list_level = {}
		admins = ["AndreyWarGold", "loker"]
	if msg == "!clear role" and message.author.name in admins:
		list_emoji = []
		list_role = []
	if msg == "!for role" and message.author.name in admins:
		channel_for_set_role = message.channel
	if msg == "!for save" and message.author.name in admins:
		channel_for_save = message.channel
	if msg == "!for debug" and message.author.name in admins:
		channel_for_debug = message.channel
	if msg == "!for rp" and message.author.name in admins:
		channel_for_rp = message.channel
	if msg.startswith("!раса"):
		hh =""
		txt = message.content.split(" ")
		for i in range(len(txt)-1):
			hh += txt[i+1] + " "
		if list_level.get(message.author.name) >= need_lvl.get("For_edit_rasa") or message.author.name in admins:
			list_rp_rasa[message.author.name] = hh
			await message.channel.send("Изменено!")
	if msg.startswith("!профессия"):
		hh =""
		txt = message.content.split(" ")
		for i in range(len(txt)-1):
			hh += txt[i+1] + " "
		if list_level.get(message.author.name) >= need_lvl.get("For_edit_profession") or message.author.name in admins:
			list_rp_profession[message.author.name] = hh
			await message.channel.send("Изменено!")
	if msg == "!удача":
		await message.channel.send("Это игра на удачу! Играть командой **!удача (с этого числа) (по этое) (ставка)**   Промежуток должен быть в 10 чисел!")
	if msg.startswith("!удача "):
		txt = message.content.split(" ")
		if int(txt[3]) <= list_money.get(message.author.name):
			list_money[message.author.name] -= int(txt[3]) 
			c = random.randint(0, 100)
			if int(txt[2]) - int(txt[1]) == 10:
				if c >= int(txt[1]) and c <= int(txt[2]):
					await message.channel.send("Вы выиграли " + str((int(txt[3])*1.5)//1) + "$, ответ был " + str(c))
					list_money[message.author.name] += (int(txt[3])*1.5)//1
				else:
					await message.channel.send("Вы проиграли " + str(int(txt[3])) + "$, ответ был " + str(c))
			else:
				await message.channel.send("Неправильно указан промежуток чисел!!!  Писать нужно в таком формате: **!удача (с какого числа) (по какое) (ставка)**  промежуток должен быть в 10 чисел")
		else:
			await message.channel.send("Недостаточно денег на балансе!!! Ваш баланс: " + str(list_money.get(message.author.name)) + "$")
	if msg.startswith("!имя"):
		hh =""
		txt = message.content.split(" ")
		for i in range(len(txt)-1):
			hh += txt[i+1] + " "
		if list_level.get(message.author.name) >= need_lvl.get("For_edit_name") or message.author.name in admins:
			list_rp_name[message.author.name] = hh
			await message.channel.send("Изменено!")
	if msg.startswith("!цвет"):
		hh =""
		txt = message.content.split(" ")
		if list_level.get(message.author.name) >= need_lvl.get("For_edit_color") or message.author.name in admins:
			list_rp_color[message.author.name] = txt[1]
			await message.channel.send("Изменено! Есть цвета: " + str(colors))
	if msg.startswith("!need_lvl") and message.author.name in admins:
		txt = message.content.split(" ")
		need_lvl[txt[1]] = int(txt[2])
		await message.channel.send("Требуемый уровень для "+ txt[1] + ": " + txt[2])
	if msg.startswith("!-опыт") and message.author.name in admins:
		txt = message.content.split(" ")
		list_exp[txt[1]] = 0
		await message.channel.send("Обнулено опыт учасника: "+ txt[1])
	if msg.startswith("!-уровень") and message.author.name in admins:
		txt = message.content.split(" ")
		list_level[txt[1]] = 0
		await message.channel.send("Обнулено уровень учасника: "+ txt[1])
	if msg.startswith("!-админ") and message.author.name in admins:
		txt = message.content.split(" ")
		for i in range(len(txt)-1):
			admins.pop(txt[i+1])
		await message.channel.send("Текущие админы этого бота: "+ str(admins))
	if msg.startswith("!+админ") and message.author.name in admins:
		txt = message.content.split(" ")
		for i in range(len(txt)-1):
			admins.append(txt[i+1])
		await message.channel.send("Текущие админы этого бота: "+ str(admins))
	if msg.startswith("!макс ролей") and message.author.name in admins:
		txt = msg.split(" ")
		max_role = int(txt[2])
		await message.channel.send("Максимум ролей: "+ str(max_role))
	if msg.startswith("!опыт за рп ") and message.author.name in admins:
		txt = msg.split(" ")
		exp_for_rp = int(txt[3])
		await message.channel.send("Опыта за РП сообщение: "+ str(exp_for_rp))
	if msg.startswith("!роли") and message.author.name in admins:
		for i in range(len(list_emoji)):
			print("add_reaction")
			await message.add_reaction(list_emoji[i])
		await message.channel.send("для выбора роли нажмите на смайл")
	if msg.startswith("!всем_роль "):
		txt = msg.split(" ")
		t_role = discord.utils.get(message.guild.roles, id=int(txt[1]) )
		poh = t_role
		list_members = message.channel.members
		for a in range(len(list_members)):
			if len(list_members[a].roles) <= int(txt[2]) :
				await list_members[a].add_roles(t_role)
				print("дано роль " + list_members[a].name)


client.run(os.environ.get("Bot_Token"))