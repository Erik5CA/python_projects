from pprint import PrettyPrinter
from requests import get
from api_key import API_KEY


URL_API = "https://currency-conversion-and-exchange-rates.p.rapidapi.com"

headers = {
	"X-RapidAPI-Key": API_KEY,
	"X-RapidAPI-Host": "currency-conversion-and-exchange-rates.p.rapidapi.com"
}

printer = PrettyPrinter()

def get_currencies():
    response = get(f'{URL_API}/symbols', headers=headers, timeout=5).json()['symbols']
    # printer.pprint(response)
    data = list(response.items())
    data.sort()
    return data

def print_currencies(currencies):
    for currency in currencies:
        _id = currency[0]
        name = currency[1]
        print(f'{_id} - {name}')
        
def exchange_rate(currency1, currency2):
    querystring = {"from": currency1 ,"to": currency2, "amount": '1'}
    # print(querystring)
    response = get(f'{URL_API}/convert', headers=headers, timeout=5, params=querystring)
    data = response.json()
    
    if not data['success']:
        print('Invalid currencies.')
        return
    rate = data['info']['rate']
    print(f'{currency1} -> {currency2} = {rate}')

def convert(currency1, currency2, amount):
    try:
        amount = float(amount)
    except:
        print('Invalid amount')
        return
    
    querystring = {"from": currency1 ,"to": currency2, "amount": str(amount)}
    # print(querystring)
    response = get(f'{URL_API}/convert', headers=headers, timeout=5, params=querystring)
    data = response.json()
    
    if not data['success']:
        print('Invalid currencies.')
        return
    rate = data['info']['rate']
    print(f'{currency1} -> {currency2} = {rate}')
    converted_amount = data['result']
    print(f'{amount} {currency1} is to equal to {round(converted_amount,2)} {currency2}')
    # return converted_amount    


def main():
    currencies = get_currencies()
    print('Welcome to the currency converter!')
    print('List - list the different currencies.')
    print('Convert - convert from one currency to another.')
    print('Rate - get the convert rate of two currencies.')
    print()

    while True:
        command = input('Enter a command (q to quit): ').lower()
        if command == 'q':
            break
        elif command == 'list':
            print_currencies(currencies)
        elif command == 'convert':
            currency1 = input('Enter a base currency: ').upper()
            amount = input(f'Enter the amount in {currency1}: ')
            currency2 = input('Enter a currency to convert to: ').upper()
            convert(currency1, currency2, amount)
            # print(converted_amount)
        elif command == 'rate':
            currency1 = input('Enter a base currency: ').upper()
            currency2 = input('Enter a currency to convert to: ').upper()
            exchange_rate(currency1, currency2)
        else:
            print('Invalid command.')

main()