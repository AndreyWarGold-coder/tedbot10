import discord
import pickle

client = discord.Client()

list_people = []
list_level = { "AndreyWarGold": 0}
list_exp = { "AndreyWarGold": 0}
exp_for_rp = 0
channel_for_debug = ""
channel_for_rp = ""

list_emoji = []
list_role =[]
msg = ""
strg2 = ""
channel_for_set_role = ""
max_role = 0
admins = []


def save_obj(obj, name ):
    with open('obj/'+ name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

def load_obj(name ):
    with open('obj/' + name + '.pkl', 'rb') as f:
        return pickle.load(f)

@client.event
async def on_ready():
	global list_role, list_emoji, list_people, max_role, admins, channel_for_set_role, channel_for_rp, channel_for_debug, list_level, list_exp, exp_for_rp
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
async def on_raw_reaction_add(payload):
	global list_role, list_emoji, list_people, msg, strg2, file, channel_for_set_role, max_role, channel_for_debug, exp_for_rp, list_level, list_exp
	channel = client.get_channel(payload.channel_id)
	msg = await channel.fetch_message(payload.message_id)
	emoji = str(payload.emoji)
	user = client.get_user(payload.user_id)
	memb = payload.member
	if user == client.user:
		return
	if str(payload.emoji) in list_emoji and payload.channel_id == channel_for_set_role.id and len(memb.roles) < max_role:
		await memb.add_roles(discord.utils.get(msg.guild.roles, id=int(list_role[list_emoji.index(str(payload.emoji))]) ))


@client.event
async def on_message(message):
	global list_role, list_emoji, list_people, msg, strg2, file, channel_for_set_role, max_role, admins, list_level, list_exp, exp_for_rp, channel_for_debug, channel_for_rp
	if message.author == client.user:
		return
	msg = message.content.lower()
	if not message.author.name in list_people :
		list_people.append(str(message.author.name))
		list_exp[message.author.name] = 0
		list_level[message.author.name] = 0
	if message.channel == channel_for_rp and not msg.startswith("/"):
		max_exp = 5*list_level.get(message.author.name)+(10 + (2*list_level.get(message.author.name)))
		if max_exp <= list_exp.get(message.author.name) + exp_for_rp:
			list_level[message.author.name] +=1
			list_exp[message.author.name] = list_exp.get(message.author.name) + exp_for_rp - max_exp
			await channel_for_debug.send("Получен уровень " + str(list_level.get(message.author.name)) + " учасником " + message.author.name)
		else:
			list_exp[message.author.name] += exp_for_rp
			await channel_for_debug.send("Получено за РП опыта: " + str(exp_for_rp)+ " учасником " + message.author.name)
	if message.channel == channel_for_rp:
		return
	if message.content.startswith('hello'):
		await message.channel.send('Hello!')
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
	if msg == "!инфа":
		emb = discord.Embed(title="Имя: " +  message.author.name, color = 0xc27c0e)
		emb.add_field(name="Уровень РП: " + str(list_level.get(message.author.name)), value='Опыт: ' + str(list_exp.get(message.author.name)) + " / " + str(5*list_level.get(message.author.name)+(10 + (2*list_level.get(message.author.name)))))
		emb.add_field(name="Баланс:", value=str(0) +"$")
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
	if msg == "!for debug" and message.author.name in admins:
		channel_for_debug = message.channel
	if msg == "!for rp" and message.author.name in admins:
		channel_for_rp = message.channel
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

client.run('NjgxNTgxMDQwMTU3ODUxNjU3.XlQh3A.sNLA86FYPqgONBaiGjqcEfe8Flc')