import datetime

def log(func):
    def wraper(*args):
        time = datetime.datetime.now()
        print(f"[{time.date()}][{time.time()}] User with id: {args[0].from_user.id} writed text: {args[0].text}\n")
        func(*args)

    return wraper