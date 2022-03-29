# KSP-Price-Notifier

Use to get notified for change of price in KSP.

## Installation

```shell
pip install ksp-price-notifier
```

## Usage

just give it the uin (can be found the link, as <https://ksp.co.il/?uin=109332>).
target price the the path to chromedriver:

```shell
ksp-price-notifier 109332 5990
```

result:

```text
The price is lower than the target price, it is now 5549
Go and buy! https://ksp.co.il/?uin=109332
```

## In-Code usage

```python
from ksp_price_notifier import GetPriceFromKSP

getter = GetPriceFromKSP()
getter.get_price(109332)

> 4690
```
