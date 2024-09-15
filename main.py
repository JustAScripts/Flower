import requests, json, uuid
from time import sleep

with open('config.json', 'r') as file:
    config = json.load(file)

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

bar = None
while True:
    try:
        baz = requests.get("https://pastefy.app/Pq7EfNmH/raw")
        qux = baz.json()
        quux = qux['Paid']['id'] if value else qux['Web']['id']

        if bar is not None and quux != bar:
            asset = quux
            print(asset)
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
                    if respond['purchaseResult'] == "Purchase transaction success":
                        print(f'Successfully bought {info["Name"]}')
                    else:
                        print(respond)

                if value:
                    if info['PriceInRobux'] in config['Setting']['Prices']:
                        Post()
                    else:
                        print("Price Doesn't Match")
                else:
                    if info['PriceInRobux'] == 0:
                        for _ in range(5):
                            Post()
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")

    bar = quux
