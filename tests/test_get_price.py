from collections import namedtuple


provider = namedtuple('requests', ['get', lambda x: {'result': {'data': {'price': 670}}}])

def test_find_price():
    from ksp_price_notifier import GetPriceFromKSP
    getter = GetPriceFromKSP('', provider)
    getter.get_price_from_ksp(187019)
