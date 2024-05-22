import telebot
from config import keys, TOKEN
from extensions import ConvertionException, CurrencyCoverter

#import currencyapicom

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def help(message):
    bot.reply_to(message, "'Что бы начать работу введите комманду боту в следующем формате:\n<имя Валюты> \
<в какую валюту перевести> \
<колличество переводимой валюты>\nУвидить список всех доступных валют: /values ")


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text = '\n'.join((text, key, ))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text',])
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(' ')

        if len(values) != 3:
            raise ConvertionException('Слишком много параметров.')

        quote, base, amount = values
        headers = CurrencyCoverter.convert(quote, base, amount)
    except ConvertionException as e:
        bot.reply_to(message, f'Ошибка пользователя.\n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду\n{e}')
    else:
        response = f'Цена {amount} {quote} в {base} - {headers}'
        bot.send_message(message.chat.id,response )



bot.polling()



#import requests

#url = "https://api.fastforex.io/convert?from=USD&to=RUB&amount=10&api_key=9396b960c9-cc1815f8d1-sde8xd"

#headers = {"accept": "application/json"}

#response = requests.get(url, headers=headers)

#print(response.text)
