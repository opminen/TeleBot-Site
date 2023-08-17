from bot import bot

allow_user = [5550813695, 2047069038, 1753697164]

def checkAdmin(function):
    def wraper(*args):
        if args[0].from_user.id in allow_user:
            function(*args)
        else:
            bot.send_message(args[0].chat.id, "У вас нема достопу напишіть @GigaTea")
    return wraper