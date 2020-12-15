from selenium import webdriver
from bs4 import BeautifulSoup
import argparse

def build_options():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--log-level=3')

def get_price(url: str, chrome_driver: str) -> int:

    driver = webdriver.Chrome(chrome_driver, options=build_options())
    driver.get(url)
    content = driver.page_source
    soup = BeautifulSoup(content, features="html.parser")
    items = soup.find_all('span', {'class': 'span-new-price-get-item'})
    for item in items:
        price = item.text[:-2].replace(',', '')
        return int(price)
    else:
        raise KeyError('Could not find price or the product')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Give uid and price, will notify if the price is lower than wanted price"
    )
    parser.add_argument('uin', type=int, help="the uin of the product, can be found in the url.")
    parser.add_argument('target_price', type=int, help="Target price. if the price is below, will let you know.")
    parser.add_argument('--chromedriver', help="Path to the chromedriver")
    args = parser.parse_args()
    url = url = f"https://ksp.co.il/?uin={args.uin}"
    price = get_price(url, args.chromedriver)
    if int(price) <= args.target_price:
        print(f"The price is lower than the target price, it is now {price}")
        print(f"Go and buy! {url}")
    else:
        print("The price is higher than target price.")
