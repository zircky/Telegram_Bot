import requests
import bot_token
from yobit import get_btc
from time import sleep

token = bot_token.token
#https://api.telegram.org/bot5144129065:AAFQ9Fbq4dgKAzF70rVmdRFW-2-pbl8xDOA/sendMessage?chat_id=641260625&text=hi
URL = "https://api.telegram.org/bot" + token + "/"

global list_update_id
list_update_id = 0


def get_updates():
    url = URL + 'getupdates'
    r = requests.get(url)
    return r.json()

def get_message():
    data = get_updates()

    list_object = data['result'][-1]

    chatId = list_object['message']['chat']['id']
    m_text = list_object['message']['text']

    message = {'chatId': chatId,
               'text': m_text}

    return message

def send_message(chatId, text = ' Wait a second...'):
    url = URL + 'sendmessage?chatId={}&text={}'.format(chatId, text)
    requests.get(url)




def main():
    # d = get_updates()

    while True:
        answer = get_message()
        chatId = answer['chatId']
        text = answer['text']

        if text == '/btc':
            send_message(chatId, get_btc())

        sleep(2)



if __name__ == '__main__':
    main()