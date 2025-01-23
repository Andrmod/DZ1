import requests
from bs4 import BeautifulSoup

def get_book_prices():
    base_url = "http://books.toscrape.com"
    prices = []

    for page in range(1, 51):
        url = base_url.format(page)
        response = requests.get(url)

        if response.status_code != 200:
            print(f"Помилка при доступі до сторінки {page}: {response.status_code}")
            continue

        soup = BeautifulSoup(response.text, 'html.parser')

        price_elements = soup.find_all('p', class_='price_color')
        for price in price_elements:
            prices.append(price.text)

    return prices

if __name__ == "__main__":
    book_prices = get_book_prices()

    print("Ціни книг:")
    for price in book_prices:
        print(price)
