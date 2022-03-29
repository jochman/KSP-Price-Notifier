from pkg_resources import DistributionNotFound, get_distribution

from .get_price import KSP as KSP  # noqa: F401

try:
    __version__ = get_distribution("ksp_price_notifier").version
except DistributionNotFound:
    __version__ = 'dev'
