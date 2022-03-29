import requests


class KSP:
    def __init__(
        self,
        url='https://ksp.co.il/m_action/api/item/',
        provider=requests
    ) -> None:
        self._provider = provider
        self._url = url

    def get_price(self, uin: int) -> int:
        resp = self._provider.get(f'{self._url.rstrip("/")}/{uin}')
        return int(resp.json()['result']['data']['price'])
