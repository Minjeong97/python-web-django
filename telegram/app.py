# username: mj
# bot_name: CminJ_bot


import requests
import random

token = '5914498259:AAGXg7FyuSUGXyIOnV58teCYLlvTczR7tXk'
# me = '5919490213'
output_message = 'wow'


update_url = f'https://api.telegram.org/bot{token}/getUpdates'
response = requests.get(update_url).json()
input_message = response['result'][-1]['message']['text']
chat_id = response['result'][-1]['message']['from']['id']

if input_message == '로또':
    output_message = random.sample(range(1, 46), 6)

elif input_message == '안녕':
    output_message = '안녕하세요'
else:
    output_message = '처리할 수 없습니다'
send_url = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={output_message}'
requests.get(send_url)