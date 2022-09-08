import requests
import json
from config import keys

class ConvertionException(Exception):
    pass

class CurrencyConverter:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):
        if quote == base:
            raise ConvertionException(f'Введена одинаковая валюта: {base}.')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionException(f'Не правильно указана валюта: {quote}\nСписок доступной валюты: /values')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionException(f'Не правильно указана валюта: {base}\nСписок доступной валюты: /values')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f'Введено не корректное значение: {amount}\nКоличество вводится числом')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = json.loads(r.content)[keys[base]]

        return total_base