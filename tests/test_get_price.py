def test_get_price(requests_mock):
    import requests

    from ksp_price_notifier import KSP
    requests_mock.get('https://ksp.co.il/m_action/api/item/187019',
                      json={'result': {'data': {'price': 670}}})
    getter = KSP(provider=requests)
    assert getter.get_price(187019) == 670


def test_api_is_alive():
    from ksp_price_notifier import KSP
    getter = KSP()
    getter.get_price(187019)
