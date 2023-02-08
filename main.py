import telebot
from extensions import ConverterValyut, helping
from config import token_tlg
Token = token_tlg
bot = telebot.TeleBot(Token)


@bot.message_handler(commands=['start', 'help', 'values', 'conv'])
def help_and_list(message: telebot.types.Message):
    if message.text.lower() == '/help' or message.text == '/start':
        bot.reply_to(message, helping)
    elif message.text == '/values':
        s = ConverterValyut.list_valyuta()
        bot.reply_to(message, f'{message.chat.username}, \n {s}')
    elif message.text.split()[0] == '/conv':
        s = ConverterValyut.get_price(message.text.split()[2], message.text.split()[3], message.text.split()[1])
        bot.reply_to(message, s)

@bot.message_handler(content_types=['text', 'voice'])
def privetstvie(message: telebot.types.Message):
    if message.text.lower() == 'привет':
        bot.reply_to(message, 'Приветствую!')
    else:
        bot.reply_to(message, f'введена неверная команда, проверьте регистр.\n введена неверная команда, проверьте регистр {helping}')

bot.polling(none_stop=True)