from pathlib import Path

import pytest
from pytest_localserver.http import WSGIServer
from selenium.webdriver import Edge
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from ksp_price_notifier import KSP


@pytest.fixture(scope="module")
def provider():
    webdriver = EdgeChromiumDriverManager().install()
    return Edge(service=Service(webdriver))


@pytest.fixture()
def getter(provider):
    return KSP(provider=provider)


def app(environ, start_response):
    """Simplest possible WSGI application."""
    page = Path(__file__).parent / "page.html"
    with page.open() as f:
        data = f.read()
    status = "200 OK"
    response_headers = [("Content-type", "text/plain")]
    start_response(status, response_headers)
    return [data.encode()]


def setup_module(module):
    """setup any state specific to the execution of the given module."""


@pytest.mark.skip(
    "Need to find a good way to mock the selenium response. It does not work"
)
def test_get_price(getter: KSP, testserver: WSGIServer):
    getter._url = testserver.url
    assert getter.get_price(187019) == 670


def test_api_is_alive(getter: KSP):
    getter.get_price(244025)
