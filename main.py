import requests
import json
import sys
import uuid
import os
import time
from datetime import datetime
from colorama import Style, Fore, init

init(autoreset=True)

if requests.get('https://pastefy.app/ATu39Cpn/raw').json() == 1.1:
    pass
else:
    print(requests.get('https://pastefy.app/gx2dbjJx/raw').text)
    print('Update it here https://github.com/JustAScripts/Flower')
    sys.exit()

with open('config.json', 'r') as file:
    config = json.load(file)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

clear()

tag = """⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣴⡦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡟⣳⣿⣰⢄⠀⠀⠀⣠⣤⣤⣶⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣉⠷⠿⣾⠁⠀⣼⣿⣿⣿⣿⣿⡃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⣿⣷⣄⠹⣷⡀⣿⡿⠋⣹⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⣷⣦⡀⠀⠀⠀⠀⠀
⠀⠀⠀⢠⣿⣿⣿⣿⣆⠀⣠⣤⣀⠀⠀⠀⠀⣴⣿⣿⣿⣿⠉⢻⣧⢿⣷⢿⠃⣴⡿⢟⣋⣁⡀⠀⠀⠀⠀⠀⢀⡀⢸⣿⣿⣿⣿⡇⣴⣿⣿⣶⣤
⠀⢠⣦⣜⢿⣿⣟⢻⣿⣾⣿⣿⣿⣿⡆⠀⠀⠈⣩⣽⣿⣛⣻⣦⡙⢸⣿⡇⢸⡵⠾⢿⣿⣿⣿⡇⠀⠀⠀⠀⠘⢿⣲⣿⣿⣧⢹⣿⡿⣿⣿⣿⣿
⠀⢀⣭⣭⣽⣿⣿⣼⡿⠛⣹⣿⣿⠿⠁⠀⠀⠸⣿⣿⣿⣿⠉⠉⢁⠈⠉⠁⣩⣤⣀⡘⠻⣿⣿⣿⣿⣦⠀⠀⣾⣿⣿⠿⢿⣻⣿⡏⠰⣿⣛⡋⠁
⢀⣾⣿⣿⣉⣭⣷⠛⣻⣄⢻⣷⣦⣄⠀⠀⠀⣴⣿⣿⣿⣿⣀⣴⣫⣶⠂⠀⠻⢿⣽⣿⣿⣿⣿⣿⡿⠏⠀⠸⣿⣿⣿⣿⣿⣿⣰⣿⣷⣽⣿⣿⣷
⠈⠻⢿⣿⠟⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⢿⣿⣿⣿⣿⡿⣱⣿⣧⣠⡄⠰⣾⣿⣿⣯⠻⠿⠟⠁⠀⠀⠀⠈⠙⠋⢸⣿⣿⣿⣿⠹⣿⣿⣿⠿
⠀⠀⠀⠀⠸⣿⣿⣿⣿⡇⠻⠿⠟⠋⠀⠀⠀⠀⠈⠙⠛⠋⠀⣿⣿⣿⣿⣷⣴⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⡿⠀⠈⠉⠀⠀
⠀⠀⠀⠀⠀⠻⠿⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠿⠿⠿⢿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"""

for line in tag.splitlines():
    print(Fore.MAGENTA + Style.BRIGHT + line.center(os.get_terminal_size().columns))

def warnings(message):
    print(Fore.CYAN + Style.BRIGHT + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + Style.RESET_ALL + Fore.YELLOW + Style.BRIGHT + ' [WARNING]' + Style.RESET_ALL + Style.BRIGHT + ' ' + message)

def error(error, message):
    print(Fore.CYAN + Style.BRIGHT + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + Style.RESET_ALL + Fore.RED + Style.BRIGHT + ' [' + error + ']' + Style.RESET_ALL + Style.BRIGHT + ' ' + message)

def success(success, message):
    print(Fore.CYAN + Style.BRIGHT + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + Style.RESET_ALL + Fore.GREEN + Style.BRIGHT + ' [' + success + ']' + Style.RESET_ALL + Style.BRIGHT + ' ' + message)

def thumbnail(asset):
    request = requests.get(f"https://thumbnails.roblox.com/v1/assets?assetIds={asset}&returnPolicy=PlaceHolder&size=75x75&format=Png&isCircular=false")
    return request.json()['data'][0]['imageUrl']

def hookweb(c, asset):
    return {
        "content": f"<@{config['Discord']['ping']}>",
        "embeds": [
            {
                "title": f"Successfully Bought {c}",
                "url": f"https://www.roblox.com/catalog/{asset}",
                "description": "",
                "thumbnail": {
                    "url": thumbnail(asset)
                },
                "footer": {
                    "text": "Flower Limited Sniper V1.1",
                    "icon_url": "https://cdn.discordapp.com/attachments/1175613436483350609/1285372373465567252/12640030.jpg?ex=66ea07ce&is=66e8b64e&hm=fc2520fcfea4a3a8c399d1e6ae81fe43f769a9a24cab2746f2f750a87dc10ccd&"
                },
                "color": 16761035
            }
        ]
    }

def validating():
    r = requests.get("https://users.roblox.com/v1/users/authenticated", headers={"Cookie": f".ROBLOSECURITY={config['Roblox']['Cookies']}"})
    if r.ok:
        success('WORK', 'Roblox Cookies Working')
    else:
        error('Failed', 'Your Roblox token isn\'t valid, please get it again.')
        sys.exit()

validating()

def xcrsf():
    response = requests.post(
        "https://auth.roblox.com/v2/logout",
        cookies={".ROBLOSECURITY": security}
    )
    return response.headers.get("x-csrf-token")

def userId():
    response = requests.get(
        "https://users.roblox.com/v1/users/authenticated",
        cookies={".ROBLOSECURITY": security}
    )
    if response.ok:
        return response.json().get('id')

security = config['Roblox']['Cookies']
value = config['Setting']['Boolean']
user_id = userId()
xcrsf_token = xcrsf()

if value:
    success('RUNNING', 'Watching Paid Limited!')
else:
    success('RUNNING', 'Watching Web Limited!')

bar = None
while True:
    baz = requests.get("https://pastefy.app/Pq7EfNmH/raw")
    qux = baz.json()
    quux = qux['Paid']['id'] if value else qux['Web']['id']

    if bar is not None and quux != bar:
        asset = quux
        economy = requests.get(f'https://economy.roblox.com/v2/assets/{asset}/details')
        if economy.ok:
            info = economy.json()
            payload = {
                "collectibleItemId": str(info['CollectibleItemId']),
                "collectibleProductId": str(info['CollectibleProductId']),
                "expectedCurrency": 1,
                "expectedPrice": str(info['PriceInRobux']),
                "idempotencyKey": str(uuid.uuid4()),
                "expectedSellerId": str(info['Creator']['Id']),
                "expectedSellerType": str(info['Creator']['CreatorType']),
                "expectedPurchaserType": "User",
                "expectedPurchaserId": user_id
            }

            def Post():
                global xcrsf_token
                Purchase = requests.post(
                    f'https://apis.roblox.com/marketplace-sales/v1/item/{info["CollectibleItemId"]}/purchase-item',
                    headers={'x-csrf-token': xcrsf_token},
                    cookies={'.ROBLOSECURITY': security},
                    json=payload
                )
                
                respond = Purchase.json()
                if respond.get('purchased'):
                    success('SUCCESS', f'Successfully bought {info["Name"]}')
                    if config['Discord']['webhook']:
                        requests.post(config['Discord']['url'], json=hookweb(info['Name'], asset))
                else:
                    error('FAILED', respond.text)
                    
            if value:
                if info['PriceInRobux'] in config['Setting']['Prices']:
                    Post()
                else:
                    warnings("Price Doesn't Match")
            else:
                if info['PriceInRobux'] == 0:
                    for _ in range(5):
                        Post()
        else:
            error('ERROR', 'RateLimit on economy API.')
            
    bar = quux               
