import telebot
from telebot import types

token = '5174603497:AAH19VzpEmeR-WpfpFKNBF9qVcHuMmHXgbI'
bot = telebot.TeleBot(token)


def craete_keyboard():
    keybord = types.InlineKeyboardMarkup()
    tank = types.InlineKeyboardMarkup()
    drink_btn = types.InlineKeyboardButton(text='Хочу пить', callback_data='1')
    eat_btn = types.InlineKeyboardButton(text='Хочу есть', callback_data='2')
    back_btn = types.InlineKeyboardButton(text='Назад', callback_data='3')
    keybord.add(drink_btn)
    keybord.add(eat_btn)
    tank.add(back_btn)
    return keybord
    return tank


@bot.message_handler(commands=['start'])
def start_bot(message):
    keybord = craete_keyboard()
    bot.send_message(
        message.chat.id,
        'Добрый день! Выберите, что вы хотите?',
        reply_markup=keybord
    )


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    keyboard = craete_keyboard()
    if call.message:
        if call.data == '1':
            img = open('вода.jpg', 'rb')
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo=img,
                caption='Картинка воды',
                reply_markup=keyboard
            )
            img.close()
        if call.data == '2':
            img = open('еда.jpg', 'rb')
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo=img,
                caption='Картинка еды',
                reply_markup=keyboard
            )
            img.close()
        # if call.data == '3'


if __name__ == '__main__':
    bot.polling(none_stop=True)
