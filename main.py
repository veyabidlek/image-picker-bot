import telebot
import requests

telegram_key = ""
unsplashapi = ""  

bot = telebot.TeleBot(telegram_key)

@bot.message_handler(commands=['start'])
def hello(message):
    bot.send_message(message.chat.id, 'Hello! Describe what you want and I will send a picture.')

@bot.message_handler(content_types=['text'])
def main(message):
    user_input = message.text
    generate_and_send_image(message.chat.id, user_input)

def generate_and_send_image(chat_id, user_input):
    url = 'https://api.unsplash.com/search/photos'
    params = {
        'query': user_input,  
        'per_page': 1,        
    }

    headers = {
        'Authorization': f'Client-ID {unsplashapi}',
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        if data['results']:
            photo_url = data['results'][0]['urls']['regular']
            bot.send_photo(chat_id, photo=photo_url)
        else:
            bot.send_message(chat_id, 'No photos found for the given query.')
    else:
        bot.send_message(chat_id, f'Error: {response.status_code}')

bot.polling(none_stop=True)
