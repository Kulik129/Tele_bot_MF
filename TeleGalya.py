from email import message
import telebot
from telebot import types
bot = telebot.TeleBot('5310541428:AAFcIkPbzL3KueVcTkREI7sFHsNRY0Tx0Rk')

# Добавление кнопок
@bot.message_handler(commands=['clock'])
def button(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton('Я с 10 🕚', callback_data='knopka1') 
    item2 = types.InlineKeyboardButton('Я с 11 🕚', callback_data='knopka2') 
    item3 = types.InlineKeyboardButton('Я с 12 🕛', callback_data='knopka3') 
    item4 = types.InlineKeyboardButton('Я с 13 🕐', callback_data='knopka4') 
    markup.add(item1, item2, item3,item4)
    bot.send_message(message.chat.id, 'Шо ты жмякаешь?🤬\nНу выбирай во скока ты завтра 🚶', reply_markup=markup)

# Вызов кнопок
@bot.callback_query_handler(func=lambda call:True)
def callback(call):
    user = call.message.chat.first_name #эта переменная показывает имя отправителя
    if call.message:
        if call.data == 'knopka1':
            bot.send_message(call.message.chat.id,'Ага записала! ✅ {}, ты с 10 🕚'.format(user))
        elif call.data == 'knopka2':
            bot.send_message(call.message.chat.id, 'Так! Ага.. ✔{}, вы с 11 🕚'.format(user))
        elif call.data == 'knopka3':
            bot.send_message(call.message.chat.id, 'Чулы?! {}, завтра с 12 🕛'.format(user))
        elif call.data == 'knopka4':
            bot.send_message(call.message.chat.id, 'Ты шо дурной?!😯\nНе если начальник разрешить то {} вы завтра с 13 🕐'.format(user))

#Текст 
@bot.message_handler(content_types=['text'])
def text(message):
    user = message.chat.first_name #эта переменная показывает имя отправителя
    if message.text.lower() == "да":
     bot.send_message(message.chat.id, 'Ляяя...\nНу ладно, так и записала шо {} завтра с 13 🕐'.format(user))   
    elif message.text.lower() == "спасибо":
     bot.send_message(message.chat.id, 'Ага! Давай пака-пака👋👋👋') 
    
bot.polling()