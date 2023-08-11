import pandas as pd
import requests

proxies = {
    'https': 'http://2503085-all-country-DE:295udraxu1@93.190.138.107:13569',
}


def get_category():
    url = "https://catalog.wb.ru/catalog/electronic22/catalog?appType=1&curr=rub&dest=12358070&regions=80,38,83,4,64,33,68,70,30,40,86,69,22,1,31,66,110,48,114&sort=popular&spp=0&subject=515"

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        'Origin': 'https://www.wildberries.ru',
        'Referer': 'https://www.wildberries.ru/catalog/elektronika/smartfony-i-telefony/vse-smartfony?bid=59697b7c-22b7-461d-a2ed-23340a909d4e',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Not(A:Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': 'Windows',
    }

    response = requests.get(url=url, headers=headers, proxies=proxies)
    return response.json()


def prepare_items(response):
    products = []

    products_raw = response.get('data', {}).get('products', None)

    if products_raw is not None and len(products_raw) > 0:
        for product in products_raw:
            products.append({
                'brand': product.get('brand', None),
                'name': product.get('name', None),
                'sale': product.get('sale', None),
                'priceU': product.get('priceU', None) / 100 if product.get('priceU', None) is not None else None,
                'salePriceU': product.get('salePriceU', None) / 100 if product.get('salePriceU', None) is not None else None,
                'id': product.get('id', None),
                'reviewRating': product.get('reviewRating', None),
            })

    return products


def main():
    response = get_category()
    products = prepare_items(response)

    pd.DataFrame(products).to_csv('products.csv', index=False)


if __name__ == '__main__':
    main()
