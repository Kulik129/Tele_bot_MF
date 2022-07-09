import telebot
from telebot import types

bot = telebot.TeleBot('5310541428:AAFcIkPbzL3KueVcTkREI7sFHsNRY0Tx0Rk')

@bot.message_handler(commands=['button'])
def button(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    item = types.InlineKeyboardButton('Принято‼', callback_data='knopka1') # Принято‼ - Текст в кнопке; knopka1- Название кнопки
    item1 = types.InlineKeyboardButton('Не принято😄', callback_data='knopka2') # Не принято😄 - Текст в кнопке; knopka2- Название кнопки
    markup.add(item, item1)
    bot.send_message(message.chat.id, 'Hi LOL', reply_markup=markup)

@bot.callback_query_handler(func=lambda call:True)
def callback(call):
    if call.message:
        if call.data == 'knopka1':
            bot.send_message(call.message.chat.id, 'В смысле блять? ')
        elif call.data == 'knopka2':
            bot.send_message(call.message.chat.id, 'Серьезно блять?!! ')


bot.polling()