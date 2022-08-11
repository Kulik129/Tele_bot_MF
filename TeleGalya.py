from email import message
import telebot
from telebot import types
bot = telebot.TeleBot('5310541428:AAFcIkPbzL3KueVcTkREI7sFHsNRY0Tx0Rk')

# Добавление кнопок
@bot.message_handler(commands=['clock'])
def button(call): 
    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton('Я с 10 🕚', callback_data='knopka1') 
    item2 = types.InlineKeyboardButton('Я с 11 🕚', callback_data='knopka2') 
    item3 = types.InlineKeyboardButton('Я с 12 🕛', callback_data='knopka3') 
    markup.add(item1, item2, item3)
    bot.send_message(call.chat.id, 'Доброго времени суток господа!🤠👋\nПрошу выбрать время 🚶', reply_markup=markup)

# Вызов кнопок
@bot.callback_query_handler(func=lambda call:True)
def callback(call):
       if call.message:
        user_chat = call.from_user.first_name #эта переменная показывает имя отправителя в группе
        if call.data == 'knopka1':
            bot.send_message(call.message.chat.id, '{}, дорогой вы с 10 🕚'.format(user_chat))
        elif call.data == 'knopka2':
            bot.send_message(call.message.chat.id, '{}, сладкий мой ты с 11 🕚'.format(user_chat))
        elif call.data == 'knopka3':
            bot.send_message(call.message.chat.id, ' {}, брат завтра с 12 🕛'.format(user_chat))
        elif call.data == 'knopka4':
            bot.send_message(call.message.chat.id, ' {} Подтвердил ✅'.format(user_chat))


#Текст 
@bot.message_handler(content_types=['text'])
def text(call):
    # user = call.chat.first_name #эта переменная показывает имя отправителя в лс
    text = call.text #эта переменная показывает sms отправителя
    user_chat = call.from_user.first_name #эта переменная показывает имя отправителя в группе
    important = text.lower()

    if call.text.lower() == "да":
        bot.send_message(call.chat.id, 'Да так да!'.format(user_chat))   

    elif call.text.lower() == "спасибо":
        bot.send_message(call.chat.id, 'Можешь не благодарить 😘\nМой сладкий круасанчик 🥐')

    elif call.text.lower() == "с 10":
        markup = types.InlineKeyboardMarkup(row_width=2)
        item2 = types.InlineKeyboardButton('Я с 11 🕚', callback_data='knopka2') 
        item3 = types.InlineKeyboardButton('Я с 12 🕛', callback_data='knopka3')
        markup.add(item2, item3)
        bot.send_message(call.chat.id, 'Остальные?', reply_markup=markup)
        bot.send_message(call.chat.id, '{} братишка завта с 10 🕚'.format(user_chat))


    elif call.text.lower() == "с 11": 
        markup = types.InlineKeyboardMarkup(row_width=2)
        item1 = types.InlineKeyboardButton('Я с 10 🕚', callback_data='knopka1') 
        item3 = types.InlineKeyboardButton('Я с 12 🕛', callback_data='knopka3')
        markup.add(item1, item3)
        bot.send_message(call.chat.id, 'Остальные?', reply_markup=markup)
        bot.send_message(call.chat.id, '{} братишка завта с 11 🕚'.format(user_chat))

    elif call.text.lower() == "с 12":  
        markup = types.InlineKeyboardMarkup(row_width=2)
        item1 = types.InlineKeyboardButton('Я с 10 🕚', callback_data='knopka1') 
        item2 = types.InlineKeyboardButton('Я с 11 🕚', callback_data='knopka2') 
        markup.add(item1, item2)
        bot.send_message(call.chat.id, 'Остальные?', reply_markup=markup) 
        bot.send_message(call.chat.id, '{} братишка завта с 12 🕛'.format(user_chat)) 

    elif "важно" in important:
        markup = types.InlineKeyboardMarkup(row_width=2)
        item_important = types.InlineKeyboardButton('❕❕❕ Подтверждаю❕❕❕', callback_data='knopka4')
        markup.add(item_important)
        bot.send_message(call.chat.id, 'Ну раз ВАЖНО, значит нужно подтверждать ❕', reply_markup=markup) 

    elif "пожалуйста" in important:
        bot.send_message(call.chat.id, 'Пожалуйста?! Ты даешь конечно 😄')

    elif "пизда" in important:
        bot.send_message(call.chat.id, 'Я б на твоем месте так не выражалась! 🤬')

    elif "залупа" in important:
        bot.send_message(call.chat.id, 'Фу как не красиво 🤮')

    elif "дима приехал" in important:
        bot.send_message(call.chat.id, 'Не забудтье:\nQR отплату ❕\nКредиты ❕\nРассрочки ❕\nРуберу ❕\nСимки ❕\nАкционное железо ❕\nПлан дня ❕\nDress Code❕\nДоп предложения на кассе ❕\nПроверьте ценники ❕\n\nХрани Вас Бог 🤞')

    # print(call)

    # user_chat = call.from_user.first_name #эта переменная показывает имя отправителя в группе
    # print(user_chat)
    
bot.polling()


