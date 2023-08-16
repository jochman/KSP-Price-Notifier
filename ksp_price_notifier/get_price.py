import json

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class KSP:
    def __init__(
        self, url="https://ksp.co.il/m_action/api/item/", provider=None
    ) -> None:
        if provider is None:
            from selenium.webdriver.edge.options import Options

            op = Options()
            op.headless = True
            provider = webdriver.Edge(options=op)
        self._provider = provider
        self._url = url

    def get_price(self, uin: int) -> int:
        self._provider.get(f'{self._url.rstrip("/")}/{uin}')

        WebDriverWait(self._provider, 10).until(
            EC.text_to_be_present_in_element((By.TAG_NAME, "pre"), "price")
        )

        resp = self._provider.find_element(By.TAG_NAME, "pre")
        data = json.loads(resp.text)
        return int(data["result"]["data"]["price"])
