import telebot
import openai 

telegram_key="6521674801:AAETYtmB1ZggvPlMQuukDPbT88bjXK3HalM"
openai.api_key="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"


bot = telebot.TeleBot(telegram_key) 

@bot.message_handler(commands=['start'])

def hello(message):
  bot.send_message(message.chat.id,'Hello! I am Toktar AI, a virtual assistant, who was created by Bektas. I am ready to help.')

@bot.message_handler(content_types=['text'])
def main(message):
  # user_input= message.text
  # answer=''
  # prompt=f"Mental Health expert: {user_input}\n"
  response = openai.Completion.create(
    engine='text-davinci-003',
    prompt=message.text,
    max_tokens=150,
    temperature=0,
    n=1,
    stop = None
                                      )
  if response and response.choices:
    answer = response.choices[0].text.strip()
  else:
    answer = 'Something is wrong :('
  bot.send_message(message.chat.id, answer)



bot.polling(none_stop=True)
