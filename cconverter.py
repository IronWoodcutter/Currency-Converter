import requests

currency_code = input().lower()
r = requests.get(f'http://www.floatrates.com/daily/{currency_code}.json')
data_json = r.json()
my_cache = {}
if currency_code == 'usd':
    pass
else:
    my_cache['usd'] = data_json['usd']
if currency_code == 'eur':
    pass
else:
    my_cache['eur'] = data_json['eur']

while True:
    exchange_code = input().lower()
    if exchange_code == '':
        exit()
    while True:
        money = float(input())
        if money > 0:
            break

    if str(f'{exchange_code}') in my_cache:
        print('Checking the cache...')
        print('Oh! It is in the cache!')
        print(f"You received {round(money * float(my_cache[exchange_code]['rate']), 2)} {exchange_code.upper()}.")
    else:
        r = requests.get(f'http://www.floatrates.com/daily/{currency_code}.json')
        data_json = r.json()
        my_cache[exchange_code] = data_json[exchange_code]
        print('Checking the cache...')
        print('Sorry, but it is not in the cache!')
        print(f"You received {round(money * float(my_cache[exchange_code]['rate']), 2)} {exchange_code.upper()}.")
