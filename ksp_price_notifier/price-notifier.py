from pathlib import Path
from selenium import webdriver
from bs4 import BeautifulSoup
import argparse
import typer 

def build_options():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--log-level=3')
    return chrome_options

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


def main(uin: int, target_price: int, chromedriver: Path):
    """"Give uid and price, will notify if the price is lower than wanted price

    Args:
        uin (int): the uin of the product, can be found in the url.
        target_price (int): Target price. if the price is below, will let you know.
        chromedriver (Path): Path to the chromedriver
    """

    url = url = f"https://ksp.co.il/?uin={uin}"
    price = get_price(url, chromedriver)
    if int(price) <= target_price:
        print(f"The price is lower than the target price, it is now {price}")
        print(f"Go and buy! {url}")
    else:
        print("The price is higher than target price.")

if __name__ == "__main__":
    typer.run(main)

