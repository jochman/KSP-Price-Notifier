from functools import partial

import typer

from . import KSP


def main(
    uin: int = typer.Argument(
        ...,
        help='The uin of the product, can be found in the url.'
    ),
    target_price: int = typer.Argument(
        ...,
        help='Target price. if the price is below, will let you know'
    ),
):
    getter = KSP()
    price = getter.get_price(uin)
    if int(price) <= target_price:
        print(f"The price is lower than the target price, it is now {price}")
        print(f"Go and buy! https://ksp.co.il/web/item/{uin}")
    else:
        print("The price is higher than target price.")


app = partial(typer.run, main)

if __name__ == "__main__":
    typer.run(main)
