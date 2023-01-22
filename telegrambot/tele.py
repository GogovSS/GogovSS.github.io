from telegram.ext import *
from random import *
import requests

wrd = {}

idd = 0
def write(x, upd):
    nm = upd['message']['chat']['id']
    fnm = 'id'+ str(nm) + '.txt'
    with open(fnm, 'a') as f:
        f.write(x + '\n')

def hello(update, context):
    x = update.message.text
    write(x, update)
    update.message.reply_text("Hello! I'm GogovBot!")

def add(update, context):
    nm = update['message']['chat']['id']
    x = update.message.text
    write(x, update)
    x = x.split(' ', maxsplit=1)[1]
    if nm not in wrd:
        wrd[nm] = set()
    wrd[nm].add(x)
    with open('words'+str(nm) + '.txt', 'a') as f:
        f.write(x + '\n')
    update.message.reply_text('OK')

def mw(update, context):
    nm = update['message']['chat']['id']
    x = update.message.text
    write(x, update)
    if nm in wrd and wrd[nm] is not None:
        update.message.reply_text(str(wrd[nm]))
    else:
        update.message.reply_text('Ты ещё не добавил ни одного слова!')

def dw(update, context):
    nm = update['message']['chat']['id']
    x = update.message.text
    write(x, update)
    if nm in wrd and wrd[nm] is not None:
        x = update.message.text.split(' ', maxsplit=1)[1]
        if x in wrd[nm]:
            wrd[nm].remove(x)
            if len(wrd[nm]) < 1:
                wrd.pop(nm)
            update.message.reply_text('OK')
        else:
            update.message.reply_text('Такого слова нет!')
    else:
        update.message.reply_text('Ты ещё не добавил ни одного слова!')

def ret(update, context):
    nm = update['message']['chat']['id']
    x = update.message.text
    write(x, update)
    if nm in wrd and wrd[nm] is not None:
        rnd = choice(list(wrd[nm]))
        update.message.reply_text(rnd)
    else:
        update.message.reply_text('Ты ещё не добавил ни одного слова!')

def rp(update, context):
    nm = update['message']['chat']['id']
    x = update.message.text
    global idd
    write(x, update)
    x = x.split(' ', maxsplit=1)[1]
    r = requests.get(x)
    fnm = 'result' + str(idd) + '.txt'
    with open (fnm,'w') as f:
        f.write(r.text)
    context.bot.send_document(chat_id = nm, document = open(fnm,'rb'))
    #update.message.reply_text(r.text)
    idd = idd + 1

def all(update, context):
    nm = update['message']['chat']['id']
    x = update.message.text
    write(x,update)
    update.message.reply_text(str(wrd))

def dup(update, context):
    x = update.message.text
    write(x, update)
    x = x.lower()
    fl = True
    if (fl):
        update.message.reply_text(x+'\n'+x)


def main():
    mybot = Updater("5888468999:AAGXVZ_npsUB8SaHraz1s5_-wKj-ICfKe8Y", use_context=True)
    dp = mybot.dispatcher
    global idd

    dp.add_handler(CommandHandler("start", hello))
    dp.add_handler(CommandHandler("add", add))
    dp.add_handler(CommandHandler("words", all))
    dp.add_handler(CommandHandler("mywords", mw))
    dp.add_handler(CommandHandler("random", ret))
    dp.add_handler(CommandHandler("randomword", ret))
    dp.add_handler(CommandHandler("del", dw))
    dp.add_handler(CommandHandler("delword", dw))
    dp.add_handler(CommandHandler("read_page", rp))
    dp.add_handler(CommandHandler("send_page", rp))
    dp.add_handler(CommandHandler("page", rp))
    dp.add_handler(MessageHandler(Filters.text, dup))

    mybot.start_polling()
    mybot.idle()

if __name__ == '__main__':
    main()