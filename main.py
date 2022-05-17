import re
import telebot
import wikipedia

bot = telebot.TeleBot('')
wikipedia.set_lang("ru")
def getwiki(s):
    try:
        ny = wikipedia.page(s)
        wikitext=ny.content[:1000]
        wikimas=wikitext.split('.')
        wikimas = wikimas[:-1]
        wikitext2 = ''
        for x in wikimas:
            if not('==' in x):
                if(len((x.strip()))>3):
                   wikitext2=wikitext2+x+'.'
            else:
                break
        wikitext2=re.sub('\([^()]*\)', '', wikitext2)
        wikitext2=re.sub('\([^()]*\)', '', wikitext2)
        wikitext2=re.sub('\{[^\{\}]*\}', '', wikitext2)
        return wikitext2
    except Exception as e:
        return  'В энциклопедии нет информации об этом'

@bot.message_handler(commands=["start"])
def start(m, res=False):
    mess = f'Привет, <b>{m.from_user.first_name}</b>, я бот-википедия'
    bot.send_message(m.chat.id, mess, parse_mode='html')
    bot.send_message(m.chat.id, f'Отправьте мне любое слово, и я найду его значение на Wikipedia', parse_mode='html')

@bot.message_handler(content_types=["text"])
def handle_text(message):

    bot.send_message(message.chat.id, getwiki(message.text))

bot.polling(none_stop=True, interval=0)