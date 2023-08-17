
from bot import bot
from forAdmin.log import log
from forAdmin.checkUser import checkAdmin
from time import sleep
from defaultFunc import wrapper_next

print("Бот запущено")

@bot.message_handler(commands=["start", "help"])
@checkAdmin
@log
def start(message):
    bot.send_message(message.chat.id, f"Привіт {message.from_user.username} цей бот створений в цілях перевірити навички розробника і якщо ви бачите це повідомлення то це означає що ви маєте доступ такщо потрудітся і зробимо цей проект разом")
    sleep(0.3)
    bot.send_message(message.chat.id, "Давайте продовжимо тут весь список статів, якщо хочете редактувати то введіть id:")
    wrapper_next(message)

bot.infinity_polling()