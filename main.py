from api import coingecko_service as cgapi

ticker = 'bitcoin'
market = cgapi.get_market(ticker)

print(market.symbol)

