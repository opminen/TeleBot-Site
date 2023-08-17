from bot import bot
from card.API import API
from telebot import types
from forAdmin.log import log

from defaultFunc import wrapper_next

id = 0
name = "none"
text = "none"

def update_kb():
    kb = types.InlineKeyboardMarkup(row_width=2)
    kb.row(types.InlineKeyboardButton("Підтвердити", callback_data="yes"))
    kb.row(types.InlineKeyboardButton(f"name: {name}", callback_data="name1"), types.InlineKeyboardButton(f"text: {text}", callback_data="text1"))
    kb.row(types.InlineKeyboardButton("Удалити", callback_data="delete"))
    return kb

def update_wrapper(message, _id) :
    global id, name, text
    card = API.get(_id)
    id = _id
    name = card["name"]
    text = card["text"]

    bot.send_message(message.chat.id, f'id: {id}\nname: {card["name"]}\ntext: {card["text"] if len(card["text"]) <= 30 else card["text"][0:30] + "..."}', reply_markup=update_kb())

@bot.callback_query_handler(func=lambda call: call.data in ["name1", "text1", "yes", "delete"])
def update_card(call):
    global name, text, id
    if call.data == "name1":
        @log
        def wr(message):
            global name
            name = message.text
            bot.send_message(message.chat.id, "Для продовження ви повинні ввести текст", reply_markup=update_kb())

        bot.send_message(call.message.chat.id, "Введіть ім'я")
        bot.register_next_step_handler(call.message, wr)

    if call.data == "text1":
        @log
        def wr(message):
            global text
            text = message.text
            bot.send_message(message.chat.id, "Щоб підтвердити натисніть кнопку створити", reply_markup=update_kb())

        bot.send_message(call.message.chat.id, "Введіть текст")
        bot.register_next_step_handler(call.message, wr)

    if call.data == "yes":
        API.put(id, name, text)
        bot.send_message(call.message.chat.id, "Ви обновили статтю")
        wrapper_next(call.message)

    if call.data == "delete":
        API.delete(id)
        bot.send_message(call.message.chat.id, "Ви удалили статтю")
        wrapper_next(call.message)