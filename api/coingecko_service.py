from pycoingecko import CoinGeckoAPI
from api import api_extensions

cg = CoinGeckoAPI()

def get_price(tickers):
    return cg.get_price(ids=tickers, vs_currencies='usd')

def get_coin(ticker):
    return cg.get_coin_by_id(ticker)

def get_market(ticker):
    data = cg.get_coins_markets('usd', ids='bitcoin')
    return api_extensions.dict2obj(data[0])