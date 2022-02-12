import requests
import bot_token

token = bot_token.token
#https://api.telegram.org/bot5144129065:AAFQ9Fbq4dgKAzF70rVmdRFW-2-pbl8xDOA/sendMessage?chat_id=641260625&text=hi
URL = "https://api.telegram.org/bot" + token + "/"



def get_updates():
    url = URL + 'getupdates'
    r = requests.get(url)
    return r.json()

def get_message():
    data = get_updates()

    chatId = data['result'][-1]['message']['chat']['id']
    m_text = data['result'][-1]['message']['text']

    message = {'chatId': chatId,
               'text': m_text}

    return message

def send_message(chatId, text = ' Wait a second...'):
    url = URL + 'sendmessage?chatId={}&text={}'.format(chatId, text)
    requests.get(url)




def main():
    # d = get_updates()

    # with open('updatas.json', 'w') as file:
    #      json.dump(d, file, indent=2, ensure_ascii=False)
    answer = get_message()
    chatId = answer['chatId']

    send_message(chatId, 'test нпвппакмк')



if __name__ == '__main__':
    main()