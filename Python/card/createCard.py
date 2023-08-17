from card.API import API

from bot import bot
from telebot import types
from defaultFunc import wrapper_next
from forAdmin.log import log


name = "none"
text = "none"

def update_kb():
    kb = types.InlineKeyboardMarkup(row_width=2)
    kb.row(types.InlineKeyboardButton(f"name: {name}", callback_data="name"), types.InlineKeyboardButton(f"text: {text}", callback_data="text"))
    kb.row(types.InlineKeyboardButton("Створити", callback_data="complite"))
    return kb

def create_wrapper(message):
    global name, text, kb
    name = "none"
    text = "none"
    bot.send_message(message.chat.id, "Для створення картки потрібно ввести імя та текст", reply_markup=update_kb())


@bot.callback_query_handler(func=lambda call: call.data in ["name", "text", "complite"])
def callback(call):
    global name, text
    if call.data == "name":
        @log
        def wr(message):
            global name
            name = message.text
            bot.send_message(message.chat.id, "Для продовження ви повинні ввести текст", reply_markup=update_kb())

        bot.send_message(call.message.chat.id, "Введіть ім'я")
        bot.register_next_step_handler(call.message, wr)

    if call.data == "text":
        @log
        def wr(message):
            global text
            text = message.text
            bot.send_message(message.chat.id, "Щоб підтвердити натисніть кнопку створити", reply_markup=update_kb())

        bot.send_message(call.message.chat.id, "Введіть текст")
        bot.register_next_step_handler(call.message, wr)

    if call.data == "complite":
        if name != "none" and text != "none":
            API.post(name, text)
            bot.send_message(call.message.chat.id, "Ви створили статтю")
            wrapper_next(call.message)
        else:
            bot.send_message(call.message.chat.id, "Спочатку заповніть дані", reply_markup=update_kb())