import telebot
# from telebot import apihelper
from telebot import types
# import setings as set

# apihelper.proxy = {'https':'https://188.216.77.95:8118'}
bot = telebot.TeleBot('781098537:AAEGQ7-kRv6Pt8KGs5CfW9RiPRLU8lKHp58')

@bot.message_handler(commands=['start'])
def fun_start(m):
    keyboard = telebot.types.ReplyKeyboardMarkup(True, False)
    keyboard.row('iphone', 'ipad', 'watch', 'macbook')
    keyboard.row('контакты', 'наш сайт', 'группа ВК')
    keyboard.row('/stop', '/start')
    bot.send_message(m.from_user.id, 'welkam', reply_markup=keyboard)

@bot.message_handler(commands=['stop'])
def fun_stop(m):
    hide_btn = telebot.types.ReplyKeyboardRemove()
    bot.send_message(m.from_user.id, 'показать клавиатуру /start', reply_markup=hide_btn)

@bot.message_handler(content_types=['text'])
def fun_answer(m):
    if m.text == 'iphone':
        bot.send_message(m.from_user.id, 'price replase glass iphone')
    if m.text == 'ipad':
        bot.send_message(m.from_user.id, 'price replase glass ipad')
    if m.text == 'watch':
        bot.send_message(m.from_user.id, 'price replase glass watch')
    if m.text == 'macbook':
        bot.send_message(m.from_user.id, 'price replase glass macbook')

bot.polling()
