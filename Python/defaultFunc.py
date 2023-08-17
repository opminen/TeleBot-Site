import re
from bot import bot
from telebot import types
from card.API import API
from forAdmin.log import log

stati = ""

def wrapper_next(message):
    global stati
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton(text="Створити")
    kb.add(btn1)

    stati = API.getAll()

    bot.send_message(message.chat.id, "Статтів покищо нема" if str(stati) == "{}" else "\n\n".join([f'id: {k}\nname: {v["name"]}\ntext: {v["text"] if len(v["text"]) <= 30 else v["text"][0:30] + "..."}' for k, v in stati.items()]), reply_markup=kb)
    bot.register_next_step_handler(message, handler_next)

@log
def handler_next(message):
    global stati
    stati = API.getAll()
    from card.createCard import create_wrapper
    from card.updateCard import update_wrapper
    try:
        if message.text == "Створити":
            create_wrapper(message)
        elif len(message.text) == len(re.search("[0-9]+", message.text).group()) and str(stati) != "{}":
            if int(message.text) in [int(k) for k, _ in stati.items()]:
                update_wrapper(message, int(message.text))
            else:
                bot.send_message(message.chat.id, "Статтю з таким айді не знайдено, попробуйте знову")
                bot.register_next_step_handler(message, handler_next)
        else:
            bot.send_message(message.chat.id, "Ви не можете редактувати статтю томущо її нема. Для продовження введіть команду /start")
    except AttributeError:
        bot.send_message(message.chat.id, "Введіть коректне значення!")
        bot.register_next_step_handler(message, handler_next)
