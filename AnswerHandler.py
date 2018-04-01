import datetime
from site_parser import SiteParser


bitcoin = ('bitcoin','биткоин')
ethereum = ('ethereum',"эфир")
hello_list_ru = ('здравствуй', 'привет', 'ку', 'здорово',)
hello_list_eng = ('hi','hi!',"hello","hello!")



def answer_handler(message, name):

    message_lower = message.lower()
    print(message)
    if message_lower == "/start":
        return "Hi, {}!This is test bot. Just say hello to him. И конечно можно по русски".format(name)

    hour = datetime.datetime.now().hour

    if message_lower in hello_list_ru:
        if(6 <= hour < 12): return 'Доброе утро, {}'.format(name)
        elif(12 <= hour < 17): return 'Добрый день, {}'.format(name)
        elif(17 <= hour < 23): return 'Добрый вечер, {}'.format(name)
        elif(hour > 23 or hour < 6): return 'Доброй ночи, {}'.format(name)

    if message_lower in hello_list_eng :
        if(6 <= hour < 12): return 'Good morning, {}'.format(name)
        elif(12 <= hour < 17): return 'Good day, {}'.format(name)
        elif(17 <= hour < 23): return 'Good evening, {}'.format(name)
        elif(hour > 23 or hour < 6): return 'Goodnight, {}'.format(name)

    if message_lower in bitcoin:
        return 'Bitcoin:' + SiteParser.get_price('https://coinmarketcap.com/currencies/bitcoin/')

    if message_lower in ethereum:
        return 'Ethereum:' + SiteParser.get_price('https://coinmarketcap.com/currencies/ethereum/')

    return 'Прошу прощения, {}, но кажется я еще не знаю ответа на ваш запрос'.format(name)
