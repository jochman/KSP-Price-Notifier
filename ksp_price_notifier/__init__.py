import pkg_resources

from .get_price import GetPriceFromKSP as GetPriceFromKSP  # noqa: F401

__version__ = pkg_resources.get_distribution("ksp_price_notifier").version
