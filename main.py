from api import coingecko_service as cgapi
from tkinter import *

my_coins = [
    {
        "id": "ethereum",
        "amount_owned": 10
    },
    {
        "id": "bitcoin",
        "amount_owned": 2
    }
]

pycrypto = Tk()
pycrypto.title("My Crypto Portfolio")
pycrypto.iconbitmap('favicon.ico')

name = Label(pycrypto, text="Coin Name", bg="#142E54",
             fg="white", font="Lato 12 bold", padx="5", pady="5", borderwidth=2, relief="groove")
name.grid(row=0, column=0, sticky=N+S+E+W)

name = Label(pycrypto, text="Price", bg="#142E54", fg="white",
             font="Lato 12 bold", padx="5", pady="5", borderwidth=2, relief="groove")
name.grid(row=0, column=1, sticky=N+S+E+W)

name = Label(pycrypto, text="Coins Owned", bg="#142E54", fg="white",
             font="Lato 12 bold", padx="5", pady="5", borderwidth=2, relief="groove")
name.grid(row=0, column=2, sticky=N+S+E+W)

name = Label(pycrypto, text="Total Amount Paid", bg="#142E54", fg="white",
             font="Lato 12 bold", padx="5", pady="5", borderwidth=2, relief="groove")
name.grid(row=0, column=3, sticky=N+S+E+W)

name = Label(pycrypto, text="Current Value", bg="#142E54", fg="white",
             font="Lato 12 bold", padx="5", pady="5", borderwidth=2, relief="groove")
name.grid(row=0, column=4, sticky=N+S+E+W)

name = Label(pycrypto, text="P/L per Coin", bg="#142E54", fg="white",
             font="Lato 12 bold", padx="5", pady="5", borderwidth=2, relief="groove")
name.grid(row=0, column=5, sticky=N+S+E+W)

name = Label(pycrypto, text="Total P/L With coin", bg="#142E54", fg="white",
             font="Lato 12 bold", padx="5", pady="5", borderwidth=2, relief="groove")
name.grid(row=0, column=6, sticky=N+S+E+W)


def my_portfolio(portfolio):
    coin_row = 1
    symbols = list(x['id'] for x in portfolio)
    markets = cgapi.get_market(symbols)

    for market in markets:
        name = Label(pycrypto, text=market.symbol, bg="#F3F4F6", fg="black",
                     font="Lato 12 bold", padx="2", pady="2", borderwidth=2, relief="groove")
        name.grid(row=coin_row, column=0, sticky=N+S+E+W)

        name = Label(pycrypto, text=market.current_price,
                     bg="#F3F4F6", fg="black", font="Lato 12 bold", padx="2", pady="2", borderwidth=2, relief="groove")
        name.grid(row=coin_row, column=1, sticky=N+S+E+W)

        name = Label(pycrypto, text="0", bg="#F3F4F6", fg="black", font="Lato 12 bold",
                     padx="2", pady="2", borderwidth=2, relief="groove")
        name.grid(row=coin_row, column=2, sticky=N+S+E+W)

        name = Label(pycrypto, text="0",
                     bg="#F3F4F6", fg="black", font="Lato 12 bold", padx="2", pady="2", borderwidth=2, relief="groove")
        name.grid(row=coin_row, column=3, sticky=N+S+E+W)

        name = Label(pycrypto, text="0", bg="#F3F4F6", fg="black", font="Lato 12 bold",
                     padx="2", pady="2", borderwidth=2, relief="groove")
        name.grid(row=coin_row, column=4, sticky=N+S+E+W)

        name = Label(pycrypto, text="0", bg="#F3F4F6", fg="black",
                     font="Lato 12 bold", padx="2", pady="2", borderwidth=2, relief="groove")
        name.grid(row=coin_row, column=5, sticky=N+S+E+W)

        name = Label(pycrypto, text="0", bg="#F3F4F6", fg="black",
                     font="Lato 12 bold", padx="2", pady="2", borderwidth=2, relief="groove")
        name.grid(row=coin_row, column=6, sticky=N+S+E+W)
        coin_row = coin_row + 1


my_portfolio(portfolio=my_coins)
pycrypto.mainloop()
