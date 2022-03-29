class providerMock:
    @staticmethod
    def get(*args, **kwargs):
        return {'result': {'data': {'price': 670}}}


def find_price_test():
    from ksp_price_notifier import GetPriceFromKSP
    getter = GetPriceFromKSP('', providerMock)
    getter.get_price_from_ksp(187019)
