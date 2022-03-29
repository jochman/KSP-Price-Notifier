from collections import namedtuple



def test_get_price(requests_mock):
    from ksp_price_notifier import GetPriceFromKSP
    import requests
    requests_mock.get('https://ksp.co.il/m_action/api/item/187019', json={'result': {'data': {'price': 670}}})
    getter = GetPriceFromKSP(provider=requests)
    assert getter.get_price_from_ksp(187019) == 670

def test_api_is_alive():
    from ksp_price_notifier import GetPriceFromKSP
    getter = GetPriceFromKSP()
    getter.get_price_from_ksp(187019)