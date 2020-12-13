# KSP-Price-Notifier
Use to get notified for change of price in KSP.

You must have [chromedriver](https://chromedriver.chromium.org/).

Usage:
just give it the uin (can be found the link, as https://ksp.co.il/?uin=109332). target price the the path to chromedriver:
```
python price-notifier.py 109332 5990 --chromedriver E:\dev\chromedriver.exe
```
result:
```
The price is lower than the target price, it is now 5549
Go and buy! https://ksp.co.il/?uin=109332
```