import random
import telebot
import os
API_TOKEN = '8180012580:AAFb_TkRbWetr1Q5Gv0jqsMMkeytBBVZhM0'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я бот помощник помогаю решить проблему с загрязнением! !" + '\n' + "/help - команды бота")

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "Команды бота:"+ '\n' + "/create - одна подделка из бытового пластика "+ '\n' + '/horror - страшные последствия от загрязнений ')

@bot.message_handler(commands=['horror'])
def send_horror(message):
    img_name = random.choice(os.listdir("images"))
    with open(f'images/{img_name}', 'rb') as f:  
        bot.send_photo(message.chat.id, f)





@bot.message_handler(commands=['create'])
def send_horror(message):
    with open(f'images/{create}', 'rb') as f:  
        bot.send_photo(message.chat.id, f)





bot.polling()