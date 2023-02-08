import requests
import json
from config import token_apilayer

class APIException (Exception):
    pass

headers= {
          "apikey": token_apilayer
        }
spisok={}

helping = 'список доступных комманд:\n/help - помощь\n/values - список конвертируемых валют\n/conv - конвертация, пример: /conv 8 EUR RUB (восемь евро в рубли)'
class ConverterValyut :
    @staticmethod
    def list_valyuta():
        url = "https://api.apilayer.com/currency_data/list"
        payload = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        status_code = response.status_code
        result = json.loads(response.content)
        global spisok
        spisok = result['currencies']
        vivod = 'доступные валюты'
        for i in result['currencies']:
            vivod = '\n'.join((vivod, (i + ':' + str(result['currencies'][i]))))
        return vivod

    @staticmethod
    def get_price(base, quote, amount):
        ConverterValyut.list_valyuta()
        try:
            if base.upper() not in spisok.keys() or quote.upper() not in spisok.keys():
                raise APIException ('проверьте  наименование валюты')
            if not amount.isdigit():
                raise APIException('введите название валюты')
        except APIException as e:
            return e
        url = f"https://api.apilayer.com/currency_data/convert?to={quote}&from={base}&amount={amount}"
        payload = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        status_code = response.status_code
        result = json.loads(response.content)
        vivod = f"согласно курсу валют\n {amount} {base} = {round(result['result'], 2)} {quote}"
        return vivod