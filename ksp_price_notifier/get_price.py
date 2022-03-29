import requests


class GetPriceFromKSP:
    def __init__(self, url='https://ksp.co.il/m_action/api/item/', provider=requests) -> None:
        self._provider = provider

    def get_price_from_ksp(self, uin: int) -> int:
        resp = self._provider.get(f'https://ksp.co.il/m_action/api/item/{uin}')
        return int(resp.json()['result']['data']['price'])