import datetime
import AnswerHandler
from BotHandler import  BotHandler


token = "581420263:AAERFSZuDKnTNMQeWtO4v9beNz-OfjV792s"

greet_bot = BotHandler(token)
greetings = ('здравствуй', 'привет', 'ку', 'здорово')
now = datetime.datetime.now()

def main():
    new_offset = None
    today = now.day
    hour = now.hour

    while True:
        greet_bot.get_updates(new_offset)

        result, last_update = greet_bot.get_last_update()

        if(result):
            last_update_id = last_update['update_id']
            last_chat_text = last_update['message']['text']
            last_chat_id = last_update['message']['chat']['id']
            last_chat_name = last_update['message']['chat']['first_name']

            result_text = AnswerHandler.answer_handler(last_chat_text, last_chat_name)

            greet_bot.send_message(last_chat_id, result_text)

            new_offset = last_update_id + 1

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()


