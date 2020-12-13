from selenium import webdriver
from bs4 import BeautifulSoup
import argparse


def is_price_lower_than_target(uin: int, target_price: int, chrome_driver: str):
    driver = webdriver.Chrome(chrome_driver)
    price: int
    url = f"https://ksp.co.il/?uin={uin}"
    driver.get(url)
    content = driver.page_source
    soup = BeautifulSoup(content, features="html.parser")
    items = soup.find_all('span', {'class': 'span-new-price-get-item'})
    for item in items:
        price = item.text[:-2].replace(',', '')
    if int(price) <= target_price:
        print(f"The price is lower than the target price, it is now {price}")
        print(f"Go and buy! {url}")
    else:
        print("The price is higher than target price.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Give uid and price, will notify if the price is lower than wanted price"
    )
    parser.add_argument('uin', type=int, help="the uin of the product, can be found in the url.")
    parser.add_argument('target_price', type=int, help="Target price. if the price is below, will let you know.")
    parser.add_argument('--chromedriver', help="Path to the chromedriver")
    args = parser.parse_args()
    is_price_lower_than_target(args.uin, args.target_price, args.chromedriver)
