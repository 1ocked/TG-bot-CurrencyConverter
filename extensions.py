import requests
import json
from config import keys


class ConvertionException(Exception):
    pass

class CurrencyCoverter:
    @staticmethod
    def convert(quote: str, base: str, amount:str):
        if quote == base:
            raise ConvertionException(f'Невозможно перевести одинаковые валюты {base}.')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {quote}')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f'Не удалось обработать количество {amount}')

        url = f"https://api.fastforex.io/convert?from={quote_ticker}&to={base_ticker}&amount={amount}&api_key=bf16833f41-7779b33300-sdsxta"
        headers = {"accept": "application/json"}
        r = requests.get(url, headers=headers)
        resp = json.loads(r.content)
        result = resp['result']

        return result