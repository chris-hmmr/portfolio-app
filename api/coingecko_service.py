from pycoingecko import CoinGeckoAPI
from api import api_extensions

cg = CoinGeckoAPI()


def get_price(tickers):
    coins_as_string = ','.join(tickers)
    return cg.get_price(ids=coins_as_string, vs_currencies='usd')


def get_coin(ticker):
    return cg.get_coin_by_id(ticker)


def get_market(tickers):
    coins_as_string = ','.join(tickers).lower()
    data = cg.get_coins_markets('usd', ids=coins_as_string)
    return api_extensions.dict2obj(data)
