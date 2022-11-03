from api import coingecko_service as cgapi

portfolio = [
    {
        "symbol": "Ethereum",
        "amount_owned": 10
    },
    {
        "symbol": "Bitcoin",
        "amount_owned": 2
    }
    ]

symbols = list(x['symbol'] for x in portfolio)

markets = cgapi.get_market(symbols)

for market in markets:    
    print(market.symbol)
    print("{0:.2f}".format(market.current_price))
    print("-----------------------------")
